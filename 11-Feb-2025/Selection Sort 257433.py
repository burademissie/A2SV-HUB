# Problem: Selection Sort - https://practice.geeksforgeeks.org/problems/selection-sort/1

 for i in range(len(arr)-1):
            mini = i
            for j in range(i,len(arr)):
                if arr[mini] > arr[j]:
                    mini = j
            arr[mini] , arr[i] = arr[i] , arr[mini]