# encoding=utf-8

def match(s, pattern):
    """"""
    i = j = 0


def match_core(s, pattern):
    """"""
    if len(s) == 0 and len(pattern) == 0:
        return True

    if len(s) != 0 and len(pattern) == 0:
        return False

    if len(s) == 0:
        return False

    if pattern[1] == '*':
        if s[0] == pattern[0] or pattern[0] == '.':
            return match_core(s[1:], pattern) or match_core(s[1:], pattern[2:]) \
                   or match_core(s, pattern[2:])
        else:
            return match_core(s, pattern[2:])

    if s[0] == pattern[0] or pattern[0] == '.':
        return match_core(s[1:], pattern[1:])

    return False


if __name__ == '__main__':
    pass
