# copied implementation of solution in the book
# start - 16:45
# end   - 17:37
import re
from functools import partial
from collections import defaultdict


class NameNode:
    _visited = False

    def __init__(self, name):
        self.name = name
        self.known_aliases = []

    @property
    def visited(self):
        return self._visited

    def mark_visited(self):
        self._visited = True

    def add_known_alias(self, alias):
        self.known_aliases.append(alias)


def merge_stats_by_name(names_str, aliases_str):
    name_stat_regex = re.compile(r'(?P<name>\w+) \((?P<num>\d+)\)')
    aliases_regex = re.compile(r'\((?P<name1>\w+), (?P<name2>\w+)\)')

    name_stats = re.split(r',\s*', names_str)
    name_stats = map(name_stat_regex.match, name_stats)
    name_stats = defaultdict(
        int,
        {name_stat.group('name'): int(name_stat.group('num'))
         for name_stat in name_stats}
    )
    aliases = aliases_regex.findall(aliases_str)

    # 1. With all alias sets, build alias graph.
    name_nodes = {}
    for alias in aliases:
        name1, name2 = alias
        name_node1 = name_nodes.get(name1, None)
        if not name_node1:
            name_node1 = NameNode(name1)
            name_nodes[name1] = name_node1
        name_node2 = name_nodes.get(name2, None)
        if not name_node2:
            name_node2 = NameNode(name2)
            name_nodes[name2] = name_node2
        name_node1.add_known_alias(name_node2)
        name_node2.add_known_alias(name_node1)

    for name in name_stats.keys():
        if not name in name_nodes:
            name_nodes[name] = NameNode(name)

    # 2. For each group of connected nodes, merge stats.
    for name, name_node in name_nodes.items():
        if name_node.visited:
            continue
        name_node.mark_visited()
        # map(partial(_merge_stats_for_connected_nodes,
        #             name_stats, name),
        #     name_node.known_aliases)
        for known_alias in name_node.known_aliases:
            _merge_stats_for_connected_nodes(name_stats, name, known_alias)

    return name_stats


def _merge_stats_for_connected_nodes(name_stats, real_name, name_node):
    if name_node.visited:
        return

    name_node.mark_visited()
    num_name = name_stats.pop(name_node.name, 0)
    name_stats[real_name] += num_name
    # map(partial(_merge_stats_for_connected_nodes,
    #             name_stats, real_name),
    #     name_node.known_aliases)
    for known_alias in name_node.known_aliases:
        _merge_stats_for_connected_nodes(name_stats, real_name, known_alias)
