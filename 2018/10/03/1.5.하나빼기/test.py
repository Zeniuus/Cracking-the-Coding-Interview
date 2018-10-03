from main import are_loosely_same


def test_same():
    assert are_loosely_same('same', 'same')


def test_one_delete_same():
    assert are_loosely_same('pale', 'ple')


def test_one_insert_same():
    assert are_loosely_same('pale', 'pales')


def test_one_change_same():
    assert are_loosely_same('pale', 'bale')


def test_not_same():
    assert not are_loosely_same('pale', 'bake')
