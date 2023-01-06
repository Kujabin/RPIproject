a= int(input())
b= int(input())

print('a+b', a+b)
print('a-b', a-b)
print('a*b', a*b)
print('a/b', a/b)

def AB_minus(a,b):
    a= int(input())
    b= int(input())
    c=a-b
    print('a-b=',a-b)
    print('a-b=',c)

    return c

def AB_multyply(c,d):
    print('a*b=',c*d )


def AB_div(c,d):
    value= c/d
    print(type(value))
    calue = str(value)+"cm"
    print(type(value))

    return value

#파이썬은 여러개의 값이 반환 가능하다.

#반환값이 있을 경우
c=AB_div(a,b)
print (c)


#a=1
#b=1
#AB_multiply(a,b)