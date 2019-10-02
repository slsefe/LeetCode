'''
给定一个字符串，返回其中不包含重复字符的最长子串的长度。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''两次遍历

        :param s:
        :return:
        '''
        res = 0
        for i in range(len(s)):
            char_set = set()
            for j in range(i, len(s)):
                if s[j] in char_set:
                    break
                else:
                    char_set.add(s[j])
            res = max(res, len(char_set))
        return res