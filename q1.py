# I'm going to try to solve the problem introduced by dojo, before watching his solution

# Given a list of numbers as the first input (a list), find out the two numbers multiplied to be equal to the input number
# as the second input (a number)
def find_two_number_times(l, num):
    #set a list for storing tuples that matches
    ret = []
    if not l or len(l) <= 1:
        return ret

    # iterate the whole numbers
    for i in range(len(l)-1):
        for j in range(i+1, len(l), 1):
            if l[i] * l[j] == num:
                ret.append((l[i], l[j]))

    return ret


print(find_two_number_times([2,4,1,6,5,40,-1], 20))