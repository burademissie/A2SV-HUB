# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = Counter(chars)
        res = 0

        for word in words:

            curWord = defaultdict(int)
            good = True
            
            for w in word:
                curWord[w] += 1
            
            for w in curWord:
                if w not in count or curWord[w] > count[w]:
                    good = False
            
            if good:
                res += len(word)


        return res
            

    

        