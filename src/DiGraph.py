from random import random

from Node_data import Node_data, Geo_location


class DiGraph:

    def __init__(self):
        self.nodes = {}
        self.mode_count = 0
        self.edge_count = 0

    def v_size(self) -> int:
        return len(self.nodes.keys())

    def e_size(self) -> int:
        return self.edgecount

    def get_all_v(self) -> dict:
        get_v={}
        a=self.nodes
        b=self.nodes[0].get_key()
        for temp_node in self.nodes.keys():
            #get_v[temp_node]=len(self.nodes[temp_node].get_key())
            get_v[temp_node] = "|edges out|",len(self.nodes[temp_node].get_map())
        return get_v

    def get_mc(self) -> int:
        return self.mode_count

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if not self.nodes.__contains__(node_id):
            if pos is None:
                pos = Geo_location(random() * 100, random() * 100, 0)
            node_temp = Node_data(node_id, pos)
            self.nodes[node_id] = node_temp
            self.mode_count += 1
            return True
        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.nodes.__contains__(id1) and self.nodes.__contains__(id2):
            if not (self.nodes.get(id1)).map.__contains__(id2):
                (self.nodes.get(id1)).connect(id2, weight)
                self.edge_count += 1
                return True
        return False

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.nodes.__contains__(id1):
            temp_dict={}
            for temp in self.get_all_v().get(id1).map.keys():
                temp_dict[temp]=self.get_all_v().get(id1).map[temp]
            return temp_dict
            # return self.nodes.get(id1).map.keys()

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.nodes.__contains__(id1):
            temp_dict = {}
            for temp in self.nodes.values():
                if temp.map.__contains__(id1):
                    temp_dict[temp.get_key()] = temp.map.get(id1)
        return temp_dict

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.nodes.keys():
            temp_dict = self.all_in_edges_of_node(node_id)
            for temp in temp_dict.keys():
                self.remove_edge(temp, node_id)
            del self.nodes[node_id]
            return True
        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if self is None:
            return True
        if node_id1 in self.nodes.keys() and node_id2 in self.nodes.keys():
            if (node_id2 in self.nodes.get(node_id1).map):
                del self.nodes.get(node_id1).map[node_id2]
                self.edge_count-=1
                return True
        return False

    def __repr__(self):
        return f'Graph: |V|={self.nodes.__len__()},|E|={self.edge_count}'


if __name__ == '__main__':
    graph = DiGraph()
    graph.add_node(0)
    graph.add_node(1)
    graph.add_node(2)
    graph.add_node(3)
    graph.add_node(4)
    graph.add_node(5)
    print(graph.add_edge(0, 1, 5))
    print(graph.add_edge(2, 1, 2))
    print(graph.add_edge(0, 3, 2))
    print(graph.add_edge(5, 1, 2))
    print(graph.all_out_edges_of_node(0))
    print(graph.all_in_edges_of_node(1))
    print(graph.remove_node(1))
    print(graph.all_out_edges_of_node(0))
    print(graph.remove_node(1))
    print(graph.all_out_edges_of_node(1))
    print(graph.remove_edge(0, 7))
    print(graph)

# print(graph.add_edge(0,1,5))
