# I'm going to try to solve the problem introduced by dojo, before watching his solution

# Given a list of numbers as the first input (a list), find out the two numbers multiplied to be equal to the input number
# as the second input (a number)

# the problem of q1.py is that: we have iterated all numbers, however, there could be many repeated number, we don't
# have to check all of them.
def find_two_number_times(l, num):
    #set a list for storing tuples that matches
    ret = []
    if not l or len(l) <= 1:
        return ret

    # iterate the whole numbers
    for i in range(len(l)-1):
        # skip if the number (tuple) exists in the outer loop
        if (l[i], int(num/l[i])) in ret or (int(num/l[i]), l[i]) in ret:
            continue

        for j in range(i+1, len(l), 1):
            # skip if the number (tuple) exists in the inner loop
            if (l[i], l[j]) in ret:
                continue

            if l[i] * l[j] == num:
                ret.append((l[i], l[j]))

    return ret


print(find_two_number_times([2,4,1,6,5,40,2,4,5,3,5,7,1,20-1], 20))