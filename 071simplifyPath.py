"""
leetcode 71 简化路径

给定一个Unix风格的文件的绝对路径，简化它。在Unix的文件系统中，‘.’表示当前目录本身，‘..’表示父目录。

思路：使用栈实现。三种操作：当前目录不为根目录时指向上级目录；指向当前目录；指向下级目录。时间复杂度O(N)，空间复杂度O(N)。
"""


class Solution:
    def simplify_path(self, path: str) -> str:
        # 将原始绝对路径按照分隔符进行切分
        path_list = list(path.split('/'))
        # 使用栈保存有效的路径
        stack = []
        for char in path_list:
            # 不是根目录时返回上级目录
            if stack and char == '..':
                stack.pop()
            # 根目录时返回上级目录，留在当前目录
            elif char == '..' or char == '.' or char == '':
                pass
            # 转到下级目录
            else:
                stack.append(char)
        # 目录拼接
        ans = '/'
        ans += '/'.join(char for char in stack)
        return ans


def my_test():
    my_solution = Solution()
    testcases = [
        ['/home/', '/home'],  # 相对路径最后无斜杠
        ['/../', '/'],  # 根目录无上一级目录
        ['/home//foo/', '/home/foo'],  # 多个连续斜杠用一个斜杠替换
        ['/a/./b/../../c/', '/c'],
        ['/a/../../b/../c//.//', '/c'],
        ['/a//b////c/d//././/..', '/a/b/c']
    ]
    for i in range(len(testcases)):
        assert my_solution.simplify_path(testcases[i][0]) == testcases[i][1]


if __name__ == '__main__':
    my_test()
