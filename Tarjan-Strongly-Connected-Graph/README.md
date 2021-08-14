# Tarjan Strongly Connected Graph

Author: Michelle Loh<br>
Updated: 14/8/2021<br>
Descriptions:<br>
Five cities were selected randomly through [here](https://randomcity.net/stockholm) and a graph is formed with weighted edges representing the distances between each cities.
![Distances between each cities](https://github.com/Michelle-Lohwt/Algorithms/blob/main/Tarjan-Strongly-Connected-Graph/assets/visual_distance.png)

---

## Tarjan Introduction
Tarjan's strongly connected components algorithm is an algorithm in graph theory for finding the strongly connected components (SCCs) of a directed graph. Compare with Kosaraju's algorithm, Tarjan only goes through depth-first-search traversal once by implementing stack data structures.

## Time Complexity
O(n + m) where n is number of vertices and m is number of edges.

## Flowchart
The overview flowchart is shown below, read [here](https://github.com/Michelle-Lohwt/Algorithms/blob/main/Tarjan-Strongly-Connected-Graph/assets/tarjan_flowchart.png) for detailed flowchart:<br>
![Tarjan Overview](https://github.com/Michelle-Lohwt/Algorithms/blob/main/Tarjan-Strongly-Connected-Graph/assets/tarjan_overview.png)

## Conclusion
Although Kosaraju and Tarjan have the same time complexity, Tarjan only goes through the depth-first-search traversal once.

## References
- [GeeksforGeeks: Tarjan’s Algorithm to find Strongly Connected Components](https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/)
