def add(num):
    if num>=3:
        return num
    else:
        num=num+1
        add(num)

print add(1)
