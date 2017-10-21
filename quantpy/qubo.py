def geth(N,qubo):
        h = []
        for j in range(N):
                Jsum = 0
                for i in range(j+1,N):
                        Jsum += qubo[j][i] 
                h.append(qubo[j][0]*1.0/2 + Jsum)
	return h

def getj(N,qubo):
        J = [[0]*N for i in range(N)]
        for j in range(N):
                for i in range(j+1,N):
                        r = qubo[j][i]
                        J[j][i] = r*1.0/4
                        J[i][j] = r*1.0/4

        return J