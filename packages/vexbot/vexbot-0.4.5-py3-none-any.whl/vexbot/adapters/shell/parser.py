def _is_kwarg(string: str):
    if string.startswith('-') or string.startswith('--') and not string == '-':
        return True
    return False


def parse(strings: list):
    args = []

    # Parse args first
    for string in strings:
        if _is_kwarg(string):
            break
        args.append(string)
    # Remove the args we've parsed
    strings = strings[len(args):]

    kwargs = {}
    while strings:
        string = strings.pop(0)
        if string.startswith('--'):
            string = string[2:]
        elif string.startswith('-'):
            string = string[1:]
        try:
            value = strings[0]
        except IndexError:
            kwargs[string] = True
            break

        if not _is_kwarg(value):
            kwargs[string] = strings.pop(0)
        else:
            kwargs[string] = True
            continue

        # Check for list by checking if the next value has `--` or `-`
        try:
            value = strings[0]
        except IndexError:
            continue

        while not _is_kwarg(value):
            # if we make it here, than we're in a list loop
            value = strings.pop(0)

            # try to append the value onto the reference for the string
            try:
                kwargs[string].append(value)
            # if we fail, then it's probably a string and needs to be converted
            # to a list
            except AttributeError:
                kwargs[string] = [kwargs[string], value]

            # Move on to the next one, checking to see if we're at the end
            try:
                value = strings[0]
            except IndexError:
                break

    for k, v in dict(kwargs).items():
        if v in ('true', 'True'):
            kwargs[k] = True
            continue
        if v in ('False', 'false'):
            kwargs[k] = False
            continue
        try:
            v = int(v)
            kwargs[k] = v
            continue
        except ValueError:
            pass
        try:
            v = float(v)
            kwargs[k] = v
        # NOTE: End of the line
        except ValueError:
            continue

    return args, kwargs
