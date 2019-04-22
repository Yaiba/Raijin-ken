#!/usr/env/bin python
#coding: utf-8

def dij(point):
    dis = graph[point]
    visited = [0] * len(graph)
    visited[point] = 1
    for x in range(len(graph) - 1):
        min_dis = inf
        for i, d in enumerate(dis):
            if d < min_dis and visited[i] == 0:
                min_dis = d
                nearest_point = i
        # unvisit nearest_point to expand
        visited[nearest_point] = 1
        for y in range(len(graph)):
            if graph[nearest_point][y] < inf:
                if dis[y] > dis[nearest_point] + graph[nearest_point][y]:
                    dis[y] = dis[nearest_point] + graph[nearest_point][y]

    print visited
    print dis

if __name__ == "__main__":
    inf = 999999
    #
    graph = [[0, 1, 12, inf, inf, inf],
             [inf, 0, 9, 3, inf, inf],
             [inf, inf, 0, inf, 5, inf],
             [inf, inf, 4, 0, 13, 15],
             [inf, inf, inf, inf , 0, 4],
             [inf, inf, inf, inf, inf, 0]]
    start_point = 0
    dij(start_point)
