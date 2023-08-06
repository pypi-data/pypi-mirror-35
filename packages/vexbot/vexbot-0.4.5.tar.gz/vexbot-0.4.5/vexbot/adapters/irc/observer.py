import sys
import inspect as _inspect
import logging

from vexmessage import Request
from vexbot.observer import Observer
from vexbot.extensions import develop, admin
from vexbot.extensions import help as vexhelp


class IrcObserver(Observer):
    extensions = (develop.get_code, vexhelp.help, admin.get_commands)
    def __init__(self, bot, messaging, irc_interface):
        super().__init__()
        self.bot = bot
        self.messaging = messaging
        self.irc_interface = irc_interface
        self._commands = self._get_commands()
        self.logger = logging.getLogger(__name__)

    def _get_commands(self) -> dict:
        result = {}
        for name, method in _inspect.getmembers(self):
            if name.startswith('do_'):
                result[name[3:]] = method

        return result

    def do_log_level(self, *args, **kwargs):
        if not args:
            # FIXME
            return self.irc_interface.root_logger.level

    def do_debug(self, *args, **kwargs):
        self.irc_interface.root_logger.setLevel(logging.DEBUG)
        self.irc_interface.root_handler.setLevel(logging.DEBUG)

    def do_info(self, *args, **kwargs):
        self.irc_interface.root_logger.setLevel(logging.INFO)
        self.irc_interface.root_handler.setLevel(logging.INFO)

    def do_MSG(self, message, channel, *args, **kwargs):
        msg_target = kwargs.get('msg_target')
        if msg_target:
            message = msg_target + ', ' + message
        self.bot.privmsg(channel, message)

    def do_join(self, *args, **kwargs):
        self.bot.join(*args)

    def do_part(self, *args, **kwargs):
        self.bot.part(*args)

    def do_kick(self, channel, target, reason=None, *args, **kwargs):
        self.bot.kick(channel, target, reason)

    def do_away(self, message=None, *args, **kwargs):
        self.bot.away(message)

    def do_unaway(self, *args, **kwargs):
        self.bot.unaway()

    def do_topic(self, channel, topic=None, *args, **kwargs):
        self.bot.topic(channel, topic)

    def do_get_nick(self, *args, **kwargs):
        return self.bot.get_nick()

    def do_get_ip(self, *args, **kwargs):
        return str(self.bot.ip)

    def on_next(self, item: Request):
        command = item.command
        args = item.args
        kwargs = item.kwargs
        self.logger.debug(' command recieved: %s %s %s', command, args, kwargs)
        try:
            callback = self._commands[command]
        except KeyError:
            self.logger.info(' command not found: %s', command)
            return

        try:
            result = callback(*args, **kwargs)
        except Exception as e:
            self.on_error(e, command, args)
            return

        if result is None:
            self.logger.info('no result for callback: %s', command)
            return

        source = item.source
        # NOTE: probably need more here
        self.logger.debug(' send command response %s %s %s', source, command, result)
        service = self.messaging._service_name
        self.messaging.send_command_response(source, command, result=result, service=service, *args, **kwargs)

    def on_completed(self, *args, **kwargs):
        pass

    def on_error(self, *args, **kwargs):
        self.logger.exception('command failed')
