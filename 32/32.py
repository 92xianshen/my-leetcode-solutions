# -*- coding: utf-8 -*-

class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        stack.append(-1)
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif len(stack) > 1: 
                stack.pop()
                res = max(res, i-stack[-1])
            else:
                stack.pop()
                stack.append(i)
                
        return res
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.longestValidParentheses(s='(())'))