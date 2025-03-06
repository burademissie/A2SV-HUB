# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacks = []
        stackt = []

        for c in s:
            if c != '#':
                stacks.append(c)
            elif stacks:
                stacks.pop()
        
        for c in t:
            if c != '#':
                stackt.append(c)
            elif stackt:
                stackt.pop()
        return (stackt == stacks)