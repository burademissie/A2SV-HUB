# Problem: Integer to Roman - https://leetcode.com/problems/integer-to-roman/description/

class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [[1000,"M" ],[900,"CM"],[500,"D"],[400,"CD"],[100 , "C"],[90,"XC"],[50,"L"],[40,"XL"],[10,"X"],[9,"IX"],[5,"V"],[4,"IV"],[1,"I"]]
        
        ret = ""
        for nums , rom in romans:
            if num // nums:
                times = num // nums

                ret += rom * times

                num = num % nums
        return ret




            

        



       