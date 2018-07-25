#!/bin/python3

from abc import abstractmethod
import itertools
from networkx import DiGraph
import networkx as nx


class Input:
    @abstractmethod
    def get(self) -> str:
        raise NotImplementedError

    def parse(self) -> DiGraph:
        graph = DiGraph()

        for line in self.get().strip('\n').split('\n')[1:]:
            road_from, road_to, road_weight = map(int, line.split(' '))
            graph.add_edge(road_from, road_to, weight=road_weight)
            graph.add_edge(road_to, road_from, weight=1000 - road_weight)

        return graph


class ExampleInput(Input):
    def get(self) -> str:
        return '3 3\n1 3 602\n1 2 256\n2 3 411\n'


class UserInput(Input):
    def get(self) -> str:
        output = input() + '\n'
        number_of_edges = int(output.split(' ')[1])

        for edge in range(number_of_edges):
            output.append(input() + '\n')

        return output


def modulo_add(*addends: int) -> int:
    return sum(addends) % 10


def weight_of_path(graph: nx.DiGraph, path: []) -> int:

    total_weight = 0
    for start_node, end_node in zip(path[:-1], path[1:]):
        total_weight += graph.succ[start_node][end_node]['weight']

    return total_weight


series_lookup = {}
for i in range(1, 9):
    series_lookup[i] = set([(number * i) % 10 for number in range(10)])


if __name__ == '__main__':
    input_mode = UserInput()

    graph = input_mode.parse()

    digits_by_node_pair = {}

    # use only cycles of lenght > 2 (others end in 0 and do not contribute anything)
    simple_cycles = list(filter(lambda cycle: len(cycle) > 2, nx.simple_cycles(graph)))

    for start_node in graph.nodes:
        for end_node in graph.nodes:

            if start_node == end_node: continue

            possible_weights = set()

            simple_paths = list(nx.all_simple_paths(graph, start_node, end_node))
            cycles_intersecting_paths = [
                filter(lambda cycle: len(set(cycle).intersection(path)) > 0, simple_cycles) for path in simple_paths
            ]

            for path, cycles in zip(simple_paths, cycles_intersecting_paths):
                path_modulo_weight = weight_of_path(graph, path) % 10
                cycle_modulo_weights = [weight_of_path(graph, cycle + [cycle[0]]) % 10 for cycle in cycles]

                cycle_combinations = list(itertools.product(*[series_lookup[weight] for weight in cycle_modulo_weights]))

                possible_weights.update([modulo_add(path_modulo_weight, *combination) for combination in cycle_combinations])

            digits_by_node_pair[(start_node, end_node)] = possible_weights

    for digit in range(10):
        print(sum([digit in digits for digits in digits_by_node_pair.values()]))
