##Task 
##Read an integer N. For all non-negative integers i < N, print i^2 . See the sample for details.
##
##Input Format
##
##The first and only line contains the integer, N.
##

if __name__ == '__main__':
    n = int(raw_input())
    for i in range(n):
        print(i**2)
