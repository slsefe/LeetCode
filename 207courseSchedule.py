"""leetcode 207 课程表
n门课，记为0到n-1。记[i, j]为要完成课程i，需要先完成课程j。
给定课程总量n，以及课程向导条件，判断是否可能完成所有课程的学习。
思路：图的拓扑排序问题，判断给定的图是否为一个DAG。
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 构造邻接表保存图
        adj = [set() for _ in range(numCourses)]
        # 列表维护所有顶点的入度
        in_degree = [0 for _ in range(numCourses)]

        for cur, pre in prerequisites:
            adj[pre].add(cur)
            in_degree[cur] += 1

        # 队列维护入度为0的顶点
        q = []
        for i in range(numCourses):
            if in_degree[i] == 0:
                q.append(i)

        # 记录出队的次数
        num_dequeue = 0
        # 入度为0的顶点出队，并更新顶点的入度
        while q:
            pre = q.pop(0)
            num_dequeue += 1
            for cur in adj[pre]:
                in_degree[cur] -= 1
                if in_degree[cur] == 0:
                    q.append(cur)

        # 若所有顶点都入队并出队，则可完成
        return num_dequeue == numCourses


def my_test():
    n = 8
    prerequisites = [[1, 0],
                     [2, 6],
                     [1, 7],
                     [6, 4],
                     [7, 0],
                     [0, 5]
                     ]
    my_solution = Solution()
    print(my_solution.canFinish(n, prerequisites))


if __name__ == "__main__":
    my_test()
