# -*- coding: utf-8 -*-

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
        
        dist[0][0] = 0
        for i in range(1, len(word1)+1):
            dist[i][0] = i
        for j in range(1, len(word2)+1):
            dist[0][j] = j
            
        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                dist[i][j] = min(dist[i-1][j]+1, dist[i][j-1]+1)
                if word1[i-1] == word2[j-1]:
                    cost = 0
                else:
                    cost = 1
                dist[i][j] = min(dist[i][j], dist[i-1][j-1]+cost)
                
        return dist[-1][-1]
    
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.minDistance('abc', 'def'))
                