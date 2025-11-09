'''你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

示例 1：
输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。

示例 2：
输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。'''

#入度表+邻接表（广度优先遍历），拓扑排序
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegress=[0 for _ in range(numCourses)]#用于存放每一个节点的入度
        adjacency=[[] for _ in range(numCourses)]#存储邻接表
        queue=deque()
        
        for cur,pre in prerequisites: #cur为当前课程，pre为应先修课程，也就是pre->cur
            indegress[cur]+=1 #入度
            adjacency[pre].append(cur)  #构建邻接表

        for i in range(len(indegress)):
            if not indegress[i]: #遍历所有课程，将入度为0的结点加入队列
                queue.append(i)
        #拓扑排序需要将入度为0的节点优先输出，而队列里放着入度为0的所有节点
        while queue:
            pre=queue.popleft() #出队pre
            numCourses-=1
            for cur in adjacency[pre]: #遍历邻接表，将pre邻接的所有课程cur的入度-1
                indegress[cur]-=1
                if not indegress[cur]:#若该门课程cur失去前驱节点pre之后的入度为0，则入队
                    queue.append(cur)
        return not numCourses #若最后课程数量不为0，则说明存在环，return False

#方法2：深度优先遍历（通过DFS判断是否有环）
class Solution:
    def a(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i,adjacency,flags):
            if flags[i]==-1:return True #表示当前访问节点已被其他节点启动的DFS访问，无需再重复搜索
            if flags[i]==1:return False #表示当前访问节点被当前节点启动的DFS访问，说明回到的当前节点，（在本轮DFS搜索中该节点被访问两次），即课程安排图有环，返回False
            flags[i]=1
            for j in adjacency[i]:#遍历i的邻接表
                if not dfs(j,adjacency,flags):return False
            flags[i]=-1 #只有一次DFS完整结束了，才能执行这一步，说明这条路没问题，在遇到不需要遍历了
            return True

        adjacency=[[] for _ in range(numCourses)] #邻接表
        flags=[0 for _ in range(numCourses)]
        for cur,pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i,adjacency,flags):return False #即当dfs返回的是False时，返回false
        return True
