import functools as _functools


def command(function=None,
            alias: list=None,
            hidden: bool=False,
            roles: list=None,
            utterances: list=None,
            short: str=None):

    if function is None:
        return _functools.partial(command,
                                  alias=alias,
                                  hidden=hidden,
                                  roles=roles,
                                  utterances=utterances,
                                  short=short)

    # https://stackoverflow.com/questions/10176226/how-to-pass-extra-arguments-to-python-decorator
    @_functools.wraps(function)
    def wrapper(*args, **kwargs):
        return function(*args, **kwargs)
    # TODO: check for string and convert to list
    if alias is not None:
        wrapper.alias = alias
    wrapper.hidden = hidden
    wrapper.command = True
    wrapper.roles = roles
    wrapper.utterances = utterances
    wrapper.short = short
    return wrapper
