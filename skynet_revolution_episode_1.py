import sys
import math
from collections import defaultdict


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def insert_edge_link(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def bfs_implementation(self, s):

        # first Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source  as
        # visited and enqueue it
        queue.append(s)
        visited[0] = True
        bfs_sequence = []
        while queue:

            # Dequeue a vertex and add to bfs_sequence
            s = queue.pop(0)
            bfs_sequence.append(s)

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then add it to
            # visited and enqueue it
            for i in self.graph[s]:
                if i not in visited:
                    queue.append(i)
                    visited.append(i)
        return bfs_sequence


# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
# This class represents a directed graph
# using adjacency list representation

# main
n, l, e = [int(i) for i in input().split()]
g = Graph()
link = []
for i in range(l):
    n1, n2 = [int(j) for j in input().split()]
    g.insert_edge_link(n1, n2)
    link.append([n1, n2])
getway = []
for i in range(e):
    # the index of a gateway node
    ei = int(input())
    getway.append(ei)

while True:
    # The index4 of the node on which the Skynet agent is positioned this turn
    si = int(input())
    # to store the path of bfs graph
    bfs_sequence = g.bfs_implementation(si)
    for i in getway:
        # if the postion of skynet nagent have a direct link to the getway node print/cut  the link
        if [si, i] in link:
            print(f"{si} {i}")
        elif [i, si] in link:
            print(f"{i} {si}")

    # if there is one getway
    if ((len(getway) == 1) and (bfs_sequence.index(si) != len(bfs_sequence) - 1)):

        # if there is no direct link between the  postion the agent and the getway print/cut the next link
        # with bfs graph
        if (([si, getway[0]] not in link) and ([getway[0], si] not in link)):
            print(f"{si} {bfs_sequence[bfs_sequence.index(si) + 1]}")
    # if there is 3 getway
    elif ((len(getway) == 3) and (bfs_sequence.index(si) != len(bfs_sequence) - 1)):
        (a, b, c) = getway
        # if there is no direct link between the  postion the agent and the one of the  getways print/cut the next link
        # with bfs graph
        if ((([si, a] not in link) and ([si, b] not in link) and ([si, c] not in link)) and (
                ([a, si] not in link) and ([b, si] not in link) and ([c, si] not in link))):
            print(f"{si} {bfs_sequence[bfs_sequence.index(si) + 1]}")
    # print("0 1")
