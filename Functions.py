import math
"""
Input : Integer
Output : Integer
Description : Sum of two numbers
"""
def add(a,b):
    c = a+b
    return c
"""
Input : List of numbers
Output : Integer
Description : Sum of numbers given in a list / parsed dynamically
"""
def sum_argument(n):
    sum=0
    for i in range(len(n)):
        sum=sum+n[i]
    return sum
"""
Input : Integer/Float
Output : Float
Description : Division of two numbers
"""
def division(n,d):
    result = n/d
    return result

def multiplication(table,limit):
    for n in range(1,limit):
         result = table*n
         print(f"{table}*{n}={result}")

def multiplication_multitable(table_list,limit):
    for i in range(len(table_list)):
        print(f"Multiplication for {table_list[i]}")
        for j in range(1,limit):
            result = table_list[i]*j
            print(f"{table_list[i]}*{j}={result}")

"""
Description : Difference of two numbers
Input : Integer
Output : Integer
"""
def sub_of_two_num(u,s):
    return u-s

"""
Description : Factorial - recursive
Input : Integer
Output : Integer
"""
def fact(n):
    if(n>0):
        if(n==0):
            return 1
        elif(n==1):
            return 1
        else:
            return n * fact(n-1)
    else:
        print(f"Enter only positive numbers")

"""
Description : Prime numbers
Input : Integer
Output : Integer
"""
def prime(x):
    prime = [2]
    for i in range(3,x):
        for j in range(2,i):
            if(i%j==0):
               break
        else:
            prime.append(i)
              #  print(f"Given num {i} is prime")
    return set(prime)
def prime_num(y):
    isPrime = False
    for i in range(2,y):
        if(y%i==0):
            break
    else:
        isPrime = True
    return isPrime
       # print(f"Given number {y} is prime number")


"""
Description : Palindrom number
Input : Integer
Output : Palindrom or Not
"""
def Palindrom_Num(num):
    is_palindrome = False
    original_num = num
    #num = num
    reverse = 0
    while(num>0):
        #remainder and quotient
        remainder = num%10
        quotient = num//10
        #reverse logic
        reverse = (reverse*10)+remainder
        num = quotient
    if(original_num == reverse):
        is_palindrome = True
    else:
        is_palindrome

    return is_palindrome

"""
Description : Palindrome of strings
Input : String
Output : Palindrom or not
"""
def Palindrom_String(string_name):
    IsPalindrom = False
    name = string_name
    len_name = len(name)
    print(f"The name is {name} and its length is {len_name}")
    reverse_list = []
    for i in range(len_name-1,-1,-1):
       reverse_list.append(name[i])
    reversed_name = "".join(reverse_list)
    if(name==reversed_name):
        IsPalindrom = True
    else:
        IsPalindrom
    return IsPalindrom

def sorted_list(num_list):
    a = num_list
    for i in range(len(a)):
        for j in range(len(a) - 1):
            temp = a[j]
            if (a[j] > a[j + 1]):
                a[j] = a[j + 1]
                a[j + 1] = temp
    return a

def sorted_list_of_list(list_of_list):
    a = list_of_list
    for i in a:
        for i in range(len(a)-1):
            temp_name = a[i][0]
            temp_score = a[i][1]
            if(a[i][1]>a[i+1][1]):
                a[i][1] = a[i+1][1]
                a[i][0] = a[i+1][0]
                a[i+1][1] = temp_score
                a[i+1][0] = temp_name
    print(a)
    list_sorted_names=[]
    list_sorted_scores=[]

    # append names to list_sorted_names
    for i in range(len(a)):
        list_sorted_names.append(a[i][0])

    print(f"list_sorted_names : {list_sorted_names}")

    # append scores to list_sorted_scores
    for i in range(len(a)):
        list_sorted_scores.append(a[i][1])

    print(f"list_sorted_scores : {list_sorted_scores}")

    second_least = list(set(list_sorted_scores))
    second_least = second_least[1]

    print("Student with least score are :")
    names = []
    for i in range(len(a)):
        if(a[i][1]==second_least):
            names.append(a[i][0])

    print(f"names : {names}")
    names.sort()
    print(f"sorted names : {names}")

def fibnocci_num_iterations(n1,n2,n):
    l = [n1,n2]
    for i in range(n):
        sum = l[-1] + l[-2]
        l.append(sum)
    return l

def fibnocci_till_num(n):
    l = [0,1]
    while(l[-1] < n):
        sum = l[-1] + l[-2]
        if(sum < n):
            l.append(sum)
        else:
            break
    return l