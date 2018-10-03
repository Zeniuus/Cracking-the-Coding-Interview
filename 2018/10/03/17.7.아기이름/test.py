from main import merge_stats_by_name


def test_merge_stats_by_name():
    names_str = 'John (15), Jon (12), Chris (13), Kris (4), Christopher (19)'
    aliases_str = '(Jon, John), (John, Johnny), (Chris, Kris), (Chris, Christopher)'
    stats = merge_stats_by_name(names_str, aliases_str)
    assert len(stats) == 2
    assert any(stats[key] == 27 for key in ['John', 'Jon', 'Johnny'])
    assert any(stats[key] == 36 for key in ['Chris', 'Kris', 'Christopher'])