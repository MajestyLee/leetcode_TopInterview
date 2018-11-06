# Enter your code here. Read input from STDIN. Print output to STDOUT
temp = input().split()
n = int(temp[0])
m = int(temp[1])
arr = input().split()
arr = [int(a) for a in arr]
lookup = [[i for i in range(n)] for i in range(n)]
for i in range(0,n):
    for j in range(i+1,n):
        if (arr[lookup[i][j - 1]] < arr[j]):
            lookup[i][j] = lookup[i][j - 1]
        else:
            lookup[i][j] = j
for i in range(m):
    temp = input().split()
    start = int(temp[0])
    end = int(temp[1])
    print(arr[lookup[start][end]])
