def rec(num,value):
    if num <= 100:
        if num %2 != 0:
            print(f'{num} * {value} : ',(num * value))
            num+=1
        rec(num,value)

rec(1,2)