"""leetcode 210 课程表2
给定课程总数，以及课程之间的先修关系，判断是否可以完成课程，可以完成则返回课程学习顺序（任意一种），不能完成则返回空列表。
"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # 构造邻接表保存课程信息
        adj = [set() for _ in range(numCourses)]
        # 统计课程的入度
        in_degree = [0 for _ in range(numCourses)]

        for cur, pre in prerequisites:
            in_degree[cur] += 1
            adj[pre].add(cur)

        # 使用队列保存零入度课程
        q = [i for i in range(numCourses) if in_degree[i] == 0]

        # 对零入度课程出队，并更新入度表和队列
        res = []
        while q:
            pre = q.pop(0)
            res.append(pre)
            for cur in adj[pre]:
                in_degree[cur] -= 1
                if in_degree[cur] == 0:
                    q.append(cur)
        # 保存出队课程数，并返回结果
        if len(res) == numCourses:
            return res
        else:
            return []