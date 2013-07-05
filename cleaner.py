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


def nocommas(s):
    return s.replace(',', '')


def is_int(s, strict=False):
    return None


def is_float(s, strict=False):
    return None


def as_int(s, strict=False):
    return int(as_float(s, strict))


def as_float(s, strict=False):
    print s
    s = keeper(s)
    s = nocommas(s)
    return float(s)
