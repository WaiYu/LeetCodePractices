class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        startI = 0
        longest = 0
        if (s == None):
            return 0
        checked = {}
        for i in range(0,len(s)):
            if s[i] in checked:
                startI = max(startI, checked[s[i]]+1)
            checked[s[i]] = i
            longest = max(longest, i-startI+1)
        return longest
