# sorting technique 1- selection sort

def function(arr):
    n=len(arr)
    for i in range(0,n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
        arr[min],arr[i]=arr[i],arr[min]


    return arr

print(function([1,6,5,9,3,4,9,1,3]))

# time complexity--
# bigo of n)----      o(nxn)----



# sorting technique 2 - bubble sort
def function1(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr

print(function1([1,6,5,9,3,4,9,1,3]))

# sorting technique 3 - insertion sort

def function3(arr):
    n=len(arr)
    for i in range(0,n):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1

    return arr

print(function3([1,6,5,9,3,4,9,1,3]))