class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegree ={}
        available = set(supplies)
        result =[]

        for i, recipe in enumerate(recipes):
            indegree[recipe]= len(ingredients[i])
            for ingre in ingredients[i]:
                graph[ingre].append(recipe)
        queue = deque(supplies)

        while queue:
            item = queue.popleft()
            if item not in graph:
                continue
            for recipe in graph [item]:
                indegree[recipe] -=1
                if indegree[recipe] == 0:
                    result.append(recipe)
                    queue.append(recipe)
        return result