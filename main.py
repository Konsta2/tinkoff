#проверка можно ли разделить на три множества
#______________________#
def possible(n):
    if (n>3):
        sum=(n*(n+1))//2
        if (sum%3==0):
            return True
    return False
#вводим число n
n=int(input())
#______________________#
if (possible(n)) :
    print("Yes")
    
#______________________#
else:
    print("-1")
