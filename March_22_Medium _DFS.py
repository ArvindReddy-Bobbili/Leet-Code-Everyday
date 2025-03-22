class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        visited = set()
        count = 0

        def dfs(node, component):
            component.add(node)
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    dfs(neighbour, component) 
        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                if all(len(graph[node]) == len(component) - 1 for node in component):
                    count += 1
        return count