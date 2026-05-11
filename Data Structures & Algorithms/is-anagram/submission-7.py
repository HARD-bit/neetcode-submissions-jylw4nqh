class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Counts,Countt = {}, {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            Counts[s[i]] = 1 + Counts.get(s[i],0)
        for i in range(len(t)):
            Countt[t[i]] = 1 + Countt.get(t[i],0)
        for char in Counts:
            if Counts[char] != Countt.get(char, 0):
                return False
        return True