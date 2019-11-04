def simple_recursion(i):
    if i==0:
        return 0
    print(i)
    return simple_recursion(i-1)

simple_recursion(90)