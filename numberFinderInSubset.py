def subset_sum_recursive(numbers,target,partial):
    s = sum(partial)

    #check if the partial sum is equals to target
    if s == target: 
        print "sum(%s)=%s"%(partial,target)
    if s >= target:
        print "Bad Sum(%s)"%(partial)
        return # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        print "sum(%s) iteration %s"%(partial,i)
        subset_sum_recursive(remaining,target,partial + [n]) 

def subset_sum(numbers,target):
    #we need an intermediate function to start the recursion.
    #the recursion start with an empty list as partial solution.
    subset_sum_recursive(numbers,target,list())

if __name__ == "__main__":
    subset_sum([26, 39, 104, 195, 403, 504, 793, 995, 1156, 1673],3165)