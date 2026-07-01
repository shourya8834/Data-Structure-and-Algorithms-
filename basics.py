#Basics of python programming
#part1

from logging import lastResort
from operator import truediv


def pattern7_single_loop(A):
    # Total rows will always be (2 * A) - 1
    total_rows = (2 * A) - 1

    for i in range(1, total_rows + 1):

        distance_from_peak = abs(A - i)


        stars = A - distance_from_peak


        for j in range(stars):
            print("*", end="")
        print()

def pattern11(A):
    start=1
    for i in range(1,A+1):
        if i%2==0:
            start=0
        else:
            start=1
        for j in range(i):
            print(start,end="")
            start=1-start
        print()

def pattern13(a):
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(j,end="")

        for j in range(2*(a-i),0,-1):
            print(" ",end="")

        for j in range(i,0,-1):
            print(j,end="")


        print()

def pattern14(a):
    start=1
    for i in range(1,a+1):
        for j in range(1,i+1):
            print(start,end=" ")
            start+=1


        print()



def pattern15(a):
    x=65
    for i in range(1,a+1):
        x = 65
        for j in range(1,i+1):
            print(chr(x),end="")
            x+=1
        print()

def maths1(a):
    while (a>0):
        last_digit=a%10
        a=a//10
        print(last_digit)


def maths3(a):
    int1=0
    while (a>0):
        a=a//10
        int1+=1

    print(int1)


def reverse_number_palindrome(a):
    new_number=0
    original_number=a
    while (a>0):
        last_digit=a%10
        a=a//10
        new_number=new_number*10+last_digit

    if new_number==original_number:
        print("it is a palindrome")
    else:
        print("not a palindrome")


def armstrong_number(a):
    original_num=a
    new_number=0
    while (a>0):
        last_digit=a%10
        a=a//10
        new_number=new_number+last_digit**3
    if new_number==original_num:
        print("it is a armstrong number")
    else:
        print("its not a armstrong number")




def pattern16(a):
    for i in range(a,0,-1):
        x=65
        for j in range(i,0,-1):
            print(chr(x),end="")
            x+=1
        print()




from math import sqrt

def factors(a):
    for i in range(1, int(sqrt(a)) + 1):
        if a % i == 0:
            print(i, end=" ")

            if i != a // i:   # avoid duplicates for perfect squares
                print(a // i, end=" ")




def prime_number_checker(a):
    is_prime = True

    for i in range(2,a):

        if a%i==0:
            is_prime == False
        else:
            continue

    if is_prime==True:
        print("is prime")
    else:
        print("is not prime")




def butterfly(n):
    for i in range(1, n + 1):
        print("*","*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)

    for i in range(n-1, 0, -1):
        print("*" * i, end="")
        print(" " * (2 * (n - i)), end="")
        print("*" * i)





# recursion
# print Name 5 times
def function11(i,n):
    if i>n:
        return
    print("shourya")
    function11(i+1,n)



# print linearly from 1 to N
def function13(i,n):
    if i>n:
        return
    print(i)
    function13(i+1,n)


# print linearly from B to 1
def function14(i,n):
     if i<1:
         return
     print(i)
     function14(i-1,n)


# print linearly from 1 to N using back tracking

def function15(i,n):
    if i>n:
        return
    function15(i+1,n)
    print(i)



# print the sum of upto N numbers

class solution_recursion:
    def function17(self,N):
        if N==1:
            return 1
        return N+ self.function17(N-1)

    def function18(self,N):
        if N==1:
            return 1
        return N*self.function18(N-1)


class solution_array_recursion:
    def function21(self,arr):
        p1=0
        p2=len(arr)-1
        while p1<p2:
            arr[p1],arr[p2]=arr[p2],arr[p1]
            p1+=1
            p2-=1

        return arr


def function22(string):
    orignal_string = string
    p1 = 0
    p2 = len(string) - 1
    while p1 < p2:
        string[p1], string[p2] = string[p2], string[p1]
        p1 += 1
        p2 -= 1

    if orignal_string == string:
        print("string is palindrome")

    else:
        print("string is not palindrome")



def fibonacci(N):
    # Base case: if N is 0 or 1, return N
    if N <= 1:
        return N

    # Recursive calls: calculate previous two terms
    last = fibonacci(N - 1)   # (N-1)th term
    slast = fibonacci(N - 2)  # (N-2)th term

    return last + slast

# Driver code
 # Output: 3


def function40(number,arr):
    cout=0
    for i in arr:
        if i==number:
            cout+=1

    return cout
print(function40(1,[1,23,3,1,1,11,1]))

def function50(arr):
    hasharr={}
    for i in arr:
        if i in hasharr:
            hasharr[i]+=1

        else:
            hasharr[i]=1

    print(hasharr)



def function60(s):

    hash_arr=[0]*26

    for ch in s:
        hash_arr[ord(ch)-ord('a')]+=1
    for i in range(26):
        if hash_arr[i]>0:
            print(chr(ord('a')+i)," : ",hash_arr[i])





def function61(arr):
    hash_arr={}
    for i in arr:
        if i in hash_arr:
            hash_arr[i]+=1
        else:
            hash_arr[i]=1

    for key,value in hash_arr.items():
        print(key,value)
       





def function62(arr):
    largest=arr[0]

    for i in range(1,len(arr)):
        if arr[i]>largest:
            largest=arr[i]


    print(largest)



function62([1,3,3,4,1,4,5])

def function63(arr):
    hash_arr={}

    for i in arr:
        if i in hash_arr:
            hash_arr[i]+=1
        else:
            hash_arr[i]=1


    max_frequency=0
    answer= None
    for key,value in hash_arr.items():
        if value>max_frequency:
            max_frequncy=value
            answer=key

    print(answer,"the highest frequency element ")

function63([4,1,3,4,1,4,5])

def function60_checkprimes(A):
    is_prime=True
    for i in range(2,A+1)
        if A%2==0:
            is_prime=False

        else:
            is_prime=True

    if is_prime==True:
        return A,"is a prime number"
    else:
        return A,"is not a prime numeber"

print(function60_checkprimes(23))