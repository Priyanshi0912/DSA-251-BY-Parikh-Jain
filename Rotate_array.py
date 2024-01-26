def rotateArray(arr: list, k: int) -> list:
    ans=arr.copy()
    n=len(arr)
    for i in range(n):
        ans[i]=arr[(i+k)%n]
    return ans
    
    pass
