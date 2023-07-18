def ColoumSum(arr):
    coloumSum=[0 for i in range(len(arr[0]))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            coloumSum[j]+=arr[i][j]
    print(coloumSum)
ColoumSum([[1,2,3,4],[5,6,7,8],[9,2,3,4]])