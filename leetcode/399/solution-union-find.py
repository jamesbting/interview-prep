class Solution:

    class UnionFind:
        def __init__():
            self.parents = defaultdict(set)

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parents = {}

        def find(node):
            if node not in parents:
                parents[node] = (node, 1)
            parent, weight = parents[node]

            if parent != node:
                new_parent, new_weight = find(parent)
                parents[node] = (new_parent, weight * new_weight)
            return parents[node]

        def union(a, b, value): # a / b
            a_parent, a_weight = find(a)
            b_parent, b_weight = find(b)

            if a_parent != b_parent:
                parents[a_parent] = (b_parent, b_weight * value / a_weight)

        for (a,b), value in zip(equations, values):
            union(a, b, value)

        results = []
        for a, b in queries:
            if a not in parents or b not in parents:
                results.append(-1.0)
            else:
                a_parent, a_weight = find(a)
                b_parent, b_weight = find(b)

                if a_parent != b_parent:
                    results.append(-1.0)
                else:
                    results.append(a_weight / b_weight)
        return results
            