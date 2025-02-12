# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        answer = [[0] * len(img[0]) for _ in range(len(img))]
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 0), (0, 1), (1, -1), (1, 0), (1, 1)]


        for i in range(len(img)):
            for j in range(len(img[0])):
                total , count = 0 , 0

                for di , dj in directions:
                    ni , nj = i + di , j + dj
                    if 0<= ni < len(img) and 0 <= nj < len(img[0]):
                        total += img[ni][nj]
                        count += 1
                print(total)
                answer[i][j] = (total//count)
        return answer
        

        