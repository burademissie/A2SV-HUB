# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:

        def validpalindrome(arr , left , right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        right , left = len(s) - 1 , 0
        
        while right > left:
            if s[right] != s[left]:
                return validpalindrome(s , left + 1 , right) or validpalindrome(s, left , right - 1)
            right -= 1
            left += 1
        return True


        