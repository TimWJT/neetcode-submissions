class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        preMap = {}
        visited = set()
        
        for i in range(numCourses):
            preMap[i] = []

        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]
            preMap[course].append(prereq)
        
        
        def dfs(course):
            if course in visited:
                return False
            
            if preMap[course] == []:
                return True
            
            visited.add(course)
            
            for c in preMap[course]:
                
                if not dfs(c):
                    return False

            visited.remove(course)
            preMap[course] = []
            
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True