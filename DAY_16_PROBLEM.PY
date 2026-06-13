class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        def find_max_element(mat , n ,m , col) :
            index = -1
            max_value = -1
            for i in range(n):
                if mat[i][col] > max_value :
                    max_value = mat[i][col]
                    index = i
            return index
        n , m = len(mat) , len(mat[0])
        low , high = 0 , m - 1 
        while low <= high :
            mid = (low + high) // 2

            max_row_index = find_max_element(mat, n , m , mid)
            left = mat[max_row_index][mid - 1] if mid - 1 >= 0 else -1
            rigth = mat[max_row_index][mid + 1] if mid + 1 < m else -1

            if mat[max_row_index][mid] > left and mat[max_row_index][mid] > rigth :
                return mat[max_row_index,mid]
            elif mat[max_row_index][mid] < left :
                high = mid - 1
            else :
                low = mid + 1
    

        return [-1,-1]

        