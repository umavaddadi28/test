import Functions
import argparse
if __name__ == '__main__':
    """
    Description:
    This script contains addition , multiplication , division of different numbers
    Author : Uma
    Lead : Santosh
    """
    # addition of two numbers
    a = 3
    b = 4
    sum_two_numbers = Functions.add(a,b)
    print(f"The sum of two numbers {a},{b} is {sum_two_numbers}")

    # addition of list of numbers parsed dynamically
    parser=argparse.ArgumentParser()
    parser.add_argument("num",nargs="+",type=int)
    args = vars(parser.parse_args())
    print(f"The arguments are {args}")
    num_list = args["num"]
    result = Functions.sum_argument(num_list)
    print(f"The sum of given numbers of length {len(num_list)} is {result} ")

    # addition of list of numbers
    list_of_num = [5,58,9]
    sum_list = Functions.sum_argument(list_of_num)
    print(f"The sum of given numbers of length {len(list_of_num)} is {sum_list}")

    # division of two numbers
    n=3
    d=0
    try:
        div_num = Functions.division(n,d)
    except Exception as e:
        print(f"The exception is {e}")

    # multiplication of two numbers
    table = 2
    limit = 11
    result_multip = Functions.multiplication(table,limit)

    # multi table multiplication
    table_list = [1,2]
    limit = 5
    result_multi = Functions.multiplication_multitable(table_list,limit)

    # subtraction of two numbers
    u = 5
    s = 3
    result_sub = Functions.sub_of_two_num(u,s)
    print(f"The difference of two numbers is : {result_sub}")

    #factorial of a number

    num = 6
    fact = Functions.fact(num)
    print(f"The factorial of {num} is {fact}")

    #Prime number

    x = 10
    prime_num = Functions.prime(x)
    print(f"List of prime numbers in range {x} are {prime_num}")
    #prime_num = Functions.prime(x)
    #print(f"The list of prime numbers till {x} are {prime_num}")

    #IntegerPalindrome
    num = 13
    palindrome = Functions.Palindrom_Num(num)
    print(f"{num} is Palindrome : {palindrome}")

    #given number prime or not

    y = 11
    prime_number = Functions.prime_num(y)
    print(f"The given number {y} is prime:{prime_number}")

    #StringPalindrom
    name = "aba"
    IsPalindrom = Functions.Palindrom_String(name)
    print(f"The given name {name} is Palindrom is {IsPalindrom}")

    #Single list
    num = [136,4,56,3,900,321,1]
    sort_list_of_num = Functions.sorted_list(num)

    print(f"sort_list_of_num : {sort_list_of_num}")

    #Listoflists
    a1 = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41.0], ['Harsh', 39.0]]
    a2 = [['Harsh',20],['Beria',20],['Varun',19],['Kakunami',19],['Vikas',21]]
    sort_list_of_list = Functions.sorted_list_of_list(a1)

    str_san = "santosh"
    rev_str_san = str_san[::-1]
    if(str_san == rev_str_san):
        print("IsPalindrome")
    else:
        print("Not")

    print(Functions.fibnocci_num_iterations(10,11,10))

    print(Functions.fibnocci_till_num(10))









