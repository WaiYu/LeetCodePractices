class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        ans=[]
        q=[]
        for i in range(len(mat)):
            ans.append([])
            for j in range(len(mat[i])):
                ans[i].append(-1)
                if (int(mat[i][j]) == 0):
                    ans[i][j] = 0
                    q.append((i,j))
        neighbors=[(1,0),(-1,0),(0,1),(0,-1)]
        while(len(q)>0):
            i,j = q.pop(0)
            for walkI, walkJ in neighbors:
                neiI = i + walkI
                neiJ = j + walkJ
                if (neiI>=0 and neiI<len(mat) and neiJ>=0 and neiJ<len(mat[0])):
                    if (ans[neiI][neiJ] == -1):
                        ans[neiI][neiJ] = ans[i][j]+1
                        q.append((neiI, neiJ))
                    else:
                        if (ans[neiI][neiJ] > ans[i][j]+1):
                            ans[neiI][neiJ] = ans[i][j]+1
                            q.append((neiI, neiJ))
        return ans
