m,n = map(int,input().split())   # input m and n seperated by space
# Print a long integer denoting the minimum number of cuts needed to cut the entire paper into 1 x 1 squares.
# are (n-1) in horizontal and (m-1) in vertical
# therefore, a total of (n-1) + (m-1) 
print("Number of cuts required = ", (n-1)+(m-1))   # print the value of (n-1) + (m-1)  
