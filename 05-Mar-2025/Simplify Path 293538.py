# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        answer = []
        
        for p in range(len(path)):
            if path[p] == "" or path[p] == '.':
                continue
            elif path[p] == "..":
                if answer:
                    answer.pop()
                
            else:
                answer.append(path[p])
            
        answer = '/'.join(answer)
        return "/" + answer

            

        