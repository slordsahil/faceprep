#%%
def equalPartition( N, arr):
    arr.sort()
    arr1=[]
    arr1.append(arr.pop())
    def check_equal(arr1,arr):
        if sum(arr1)==sum(arr):
            return 1
        elif sum(arr1)>sum(arr):
            return 0
        elif sum(arr1)<sum(arr):
            i=0
            while i<len(arr)  and (sum(arr1)+arr[i])!=sum(arr)-arr[i] :
                i+=1
            if i<len(arr):
                arr1.append(arr.pop(i))
            else:
                arr1.append(arr.pop(0))
                
            return check_equal(arr1,arr)
    return check_equal(arr1,arr)
ualPartition = equalPartition(8,[4,9,8,10,1,7,5,2])
print(ualPartition)
# %%
