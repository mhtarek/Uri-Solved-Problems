while True:
       try:
              n = int(input())

              ar = [[3 for j in range(n)] for i in range(n)]

              for i in range(n):
                     for j in range(n):
                            ar[i][i] = 1
                            ar[i][n-1-i] = 2

              for i in range(n):
                     for j in range(n):
                            print("%d" % ar[i][j], end='')
                     print()
       except EOFError:
              break
