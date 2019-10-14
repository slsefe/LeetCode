"""
leetcode 242 有效的字母异位词

给定两个字符串s和t，判断两个字符串是否互为字母异位词。
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 使用哈希表保存
        d1, d2 = dict(), dict()
        for char in s:
            if char in d1:
                d1[char] += 1
            else:
                d1[char] = 1
        for char in t:
            if char in d2:
                d2[char] += 1
            else:
                d2[char] = 1
        return d1 == d2
