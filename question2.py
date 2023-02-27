def isprime(n):
    if n<2:
        return False
    for i in range(2,n-1):  #check whether n is prime or not by looping from 2 to n-1
        if n % i == 0:
            return False   # if it is divisible by any value, then it is not prime, so return False
    return True          # if it is not divisible by any value, then finally it is prime, so return True

t = int(input())   # input number of test cases  
for _ in range(t):
    n = int(input()) # input number of beads in bracelet
    answer = 0
    per_list = []
    for i in range(2**n):     # total number of possible string = 2 power n
        val = bin(i)[2:]     # treating blacks beads as 0 and white beads as 1, using binary notation
        per_list.append(val)
    for i in range(len(per_list)):
        v1 = n - len(per_list[i])         # number of zeroes to be fit at the start of the string
        per_list[i] = per_list[i]+v1*'0'  # prepending zeros at the beginning of binary strings
    
    for k in range(len(per_list)): 
        flag = True             # initially flag is true, if any of the subsequence does not meet the requirement, then flag becomes false
        for i in range(n):
            if isprime(i+1):          # check if incrementing value is prime or not, since we are checking for prime length subsequences
                for j in range(0,n,i):
                    val1 = per_list[k]
                    if isprime(j-i):
                        if val1.count('0') >= val1.count('1'):  # if number of black >= white, then false
                            flag = False
                            break
            if flag == False:
                break
        if flag == True:   # if number of white >= black then increment answer by 1
            answer+=1
    print(answer)
