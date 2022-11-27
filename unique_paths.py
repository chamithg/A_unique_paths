class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        # the length to the path is always m + n
        
        # please reffer the screen shot
        
        # we should think about this from bottom right. each cell in bottom row and left column can create 1 path to end
        # we should create a grid and iterate backwords on ti
        
        
        grid = [[0]*n for _ in range(m)]
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                if c == n-1 or r == m-1:
                    grid[r][c] = 1
                else:
                    grid[r][c] = grid[r+1][c] + grid[r][c+1]
        
        
        ## now each value says the number of posible paths from that cell to taget destination.
        return grid[0][0]
            





obj = Solution()

m = 3
n = 7

print(obj.uniquePaths(m,n))