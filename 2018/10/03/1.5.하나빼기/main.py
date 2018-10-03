# Problem solved in 20 min.
__all__ = ('are_loosely_same',)


def are_loosely_same(s1, s2):
    if abs(len(s1) - len(s2)) > 1:
        return False
    if len(s1) == len(s2):
        return _are_loosely_same_with_change(s1, s2)
    return _are_loosely_same_with_delete(s1 if len(s1) > len(s2) else s2,
                                         s2 if len(s1) > len(s2) else s1)


def _are_loosely_same_with_change(s1, s2):
    assert len(s1) == len(s2), \
        'Two args should have same length.'

    diff_counter = 0
    for c1, c2 in zip(iter(s1), iter(s2)):
        if c1 != c2:
            diff_counter += 1
        if diff_counter > 1:
            return False
    return True


def _are_loosely_same_with_delete(s1, s2):
    assert len(s1) - len(s2) == 1, \
        'First arg should be longer than second arg exactly by 1.'

    diff_counter = 0
    for i in range(len(s2)):
        if s1[i + diff_counter] != s2[i]:
            diff_counter += 1
        if diff_counter > 1:
            return False
    return True
