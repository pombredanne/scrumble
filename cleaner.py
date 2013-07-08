import re


class NaN(unicode):
    pass


class NaNError(Exception):
    pass


def keeper(s):
    if not(isinstance(s, basestring)):
        return s
    new = []
    for i in s:
        if i in '-0123456789.,()':
            new.append(i)
        else:
            new.append(' ')
    return ''.join(new).strip()


def brackets(s):
    """
    if there are brackets in a sensible place,
    remove them and slap a - before it all.
    """
    bracketted = re.findall('(.*)\((.*)\)(.*)', s)
    if len(bracketted) != 1:
        if "(" in s or ")" in s:
            raise NaNError(NaN(s))  # brackets, but not matching ones!
        else:
            return s  # do nothing
    before, middle, after = bracketted[0]
    if has_number(before) or has_number(after):
        raise NaNError(NaN(s))  # numbers outside of brackets!
    else:
        return "-" + middle


def has_number(s):
    return any(i in s for i in "0123456789")


def nocommas(s):
    return s.replace(',', '')

def nospaceafterhyphen(s):
    return re.sub('-\s*', '-', s)


def is_int(s, strict=False):
    return None


def is_float(s, strict=False):
    return None


def as_int(s, strict=False):
    f = as_float(s, strict)
    if f is None:
        return f
    else:
        return int(f)


def as_float(s, strict=False):
    if not(isinstance(s, basestring)):
        return float(s)
    if not has_number(s):
        return None
    print s
    s = brackets(s)
    s = keeper(s)
    s = nocommas(s)
    s = nospaceafterhyphen(s)
    return float(s)
