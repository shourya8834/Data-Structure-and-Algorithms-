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







# sorting technique 2 - bubble sort
def function1(arr):
    n=len(arr)
    for i in range(n-1,0,-1):
        for j in range(0,i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    return arr



# sorting technique 3 - insertion sort

def function3(arr):
    n=len(arr)
    for i in range(0,n):
        j=i
        while j>0 and arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1

    return arr





#sorting technique 4 - merge sort(best time complexity)

class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

       
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        
        while left <= mid:
            temp.append(arr[left])
            left += 1

       
        while right <= high:
            temp.append(arr[right])
            right += 1

        
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def mergesort(self, arr, low, high):
        if low >= high:
            return

        mid = (low + high) // 2

        self.mergesort(arr, low, mid)
        self.mergesort(arr, mid + 1, high)
        self.merge(arr, low, mid, high)





# sorting technique 5 - quick sort

class solution2:
    def function1(self,arr,low,high):
        pivot=arr[low]
        i=low
        j=high

        while i<j:

            while arr[i] <= pivot and i<high:
                i+=1

            while arr[j] > pivot and j>low:
                    j-=1

            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
                        

        arr[low],arr[j]=arr[j],arr[low]
        return j
                    
            

            
    def quicksort(self,arr,low,high):
        if low>=high:
            return
        Pindex=self.function1(arr,low,high)
        self.quicksort(arr,low,Pindex-1)
        self.quicksort(arr,Pindex+1,high)


B = solution2()
arr = [1, 6, 5, 9, 3, 4, 9, 1, 3]
B.quicksort(arr, 0, len(arr) - 1)
print(arr)






