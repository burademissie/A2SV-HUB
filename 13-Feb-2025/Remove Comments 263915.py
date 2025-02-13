# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        code = []
        commented = []

        dontadd = False
        for i in range(len(source)):
            j = 0

            if not dontadd:
                code = [] 


            while j < len(source[i]):
                if not dontadd and j+1 < len(source[i]) and source[i][j:j+2] == "//":
                    break
                elif not dontadd and j+1 < len(source[i]) and source[i][j:j+2] == "/*":
                    dontadd = True
                    j+=1
                elif dontadd and j+1 < len(source[i]) and source[i][j:j+2] == "*/":
                    dontadd = False
                    j+=1
                else:
                    if not dontadd:
                        code.append(source[i][j])
                j+=1
            
            if not dontadd and code:
                answer.append("".join(code))
        return answer 

        