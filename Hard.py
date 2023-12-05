class Solution:
    def shortestPalindrome(self, s: str) -> str:  
        end = 0
        if(s == s[::-1]):
            return s
        for i in range(len(s)+1):
            if(s[:i]==s[:i][::-1]):
                end=i-1
        return (s[end+1:][::-1])+s
