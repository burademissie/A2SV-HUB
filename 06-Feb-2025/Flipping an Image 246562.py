# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image[i])):
                # print(j)
                if image[i][j] == 0:
                    image[i][j] = 1
                else:
                    image[i][j] = 0
        return image

        