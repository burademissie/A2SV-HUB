# Problem: Keyboard Row - https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        firstRow = {'q','w','e','r','t','y','u','i','o','p'}
        secondRow = {'a','s','d','f','g','h','j','k','l'}
        thirdRow = {'z','x','c','v','b','n','m'}
        answer = []
        count = 0
        for word in words:
            lowered = word.lower()
            if lowered[0] in firstRow:

                for i in lowered[1:]:
                    if i not in firstRow:
                        count = 0
                        break
                    else:
                        count += 1
                    print(count)
                if count==len(word)-1:
                    answer.append(word)
                    count=0
            elif lowered[0] in secondRow:

                for i in lowered[1:]:
                    if i not in secondRow:
                        count = 0
                        break
                    else:
                        count += 1
                    
                if count==len(word)-1:
                    answer.append(word)
                    count=0

            else:
                for i in lowered[1:]:
                    if i not in thirdRow:
                        count = 0
                        break
                    else:
                        count += 1
                if count==len(word)-1:
                    answer.append(word)
                    count=0
        return answer
                

