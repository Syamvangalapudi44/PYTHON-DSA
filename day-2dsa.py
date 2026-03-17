#count even no.s from 1 to n
"""
def count_even(n):
    count=0
    for i in range(1,n+1):
        if i%2==0:
            count +=1
    return count
def main():
    n=int(input("enter your number:"))
    print("even count:", count_even(n))
main()

"""

#count digits in a number

#input=12345
#output=5

def count_digits(num):
    count=0
    while num>0:
        num = num //10
        count+=1
    return count

num=int(input("enter your number:"))
print("digits count:",count_digits(num))
