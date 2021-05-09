class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        startI = 0
        lastI = 0
        longest = 0
        if (s == None):
            return 0
        while ((lastI+1)<=len(s)):
            lastI = startI
            charSet = []
            for c in s[startI:]:
                if c not in charSet:
                    charSet.append(c)
                    lastI += 1
                else:
                    repeatI = charSet.index(c)
                    if (len(charSet)>longest):
                        longest = len(charSet)
                    startI += repeatI+1
                    break
            if (len(charSet)>longest):
                longest = len(charSet)
        return longest
