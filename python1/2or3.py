num = int (input("숫자를 입력해주세요. "))

sum = 0

for i in range(1, num+1):
    #print(i)
    #i % 2

    if (i%2!=0):
        sum += i

print(sum)

