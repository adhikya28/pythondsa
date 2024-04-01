import heapq
def nth_max(arr,n):
    arr=[-d for d in arr]
    heapq.heapify(arr)
    i=0
    while i<n:
        d=heapq.heappop(arr)
        i+=1
    return -d
print(nth_max([5,20,3,6,8,22,1,9,7],3))
