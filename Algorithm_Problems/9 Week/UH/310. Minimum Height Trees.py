"""
Runtime: 396 ms, faster than 16.64% of Python3 online submissions for Minimum Height Trees.
Memory Usage: 18.4 MB, less than 73.32% of Python3 online submissions for Minimum Height Trees.
"""
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 :
            return [0]
        
        graph = collections.defaultdict(list)
        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        leaves = []
        for node in range(n+1):
            if len(graph[node]) == 1:
                leaves.append(node)
        
        while n > 2 :
            n -= len(leaves)
            new_leaves = []
            for node in leaves:
                neighbor = graph[node].pop()
                graph[neighbor].remove(node)
                
                if len(graph[neighbor]) == 1 :
                    new_leaves.append(neighbor)
            leaves = new_leaves
        
        return leaves
