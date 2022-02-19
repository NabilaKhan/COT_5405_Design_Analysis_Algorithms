import re
import sys

def sort_and_count(A, left, right): 
  
    if left == right:
        return 0
    else:
        mid = (left + right)//2
        ra = sort_and_count(A, left, mid)
        rb = sort_and_count(A, mid + 1, right) 
        rc = merge_and_count(A, left, mid, right)
        return ra + rb + rc
  

def merge_and_count(A, left, mid, right): 

    L = A[left:mid+1]
    R = A[mid+1:right+1]
    i = 0     
    j = 0
    m = len(L)
    n = len(R)
    
    index = left     
    total_inversions = 0

   
    while i < m and j < n:
        if L[i] > R[j]:
            total_inversions += m - i
            A[index] = R[j]
            j += 1
            index += 1
        else:
            A[index] = L[i]
            i += 1
            index += 1

    while i < m or j < n:
        if(i < m):
           A[index] = L[i]
           index += 1
           i += 1
           
        elif(j < n):
            A[index] = R[j]
            index += 1
            j += 1
    return total_inversions 


if __name__ == "__main__":
    

    if(len(sys.argv) == 1):
        print("Help:")
        print("Please select option 1 for input from STDIN. Example: $python3 Test2.py 1 [10 9 8 7 6 5 4 3 2 1]")
        print("Please select option 2 for input from file. Example: $python3 Test2.py 2 test1000000.txt")
        sys.exit()
    else:
        option = sys.argv[1]
        a = ''
        if(option == '1'):
            line=sys.argv[2:]
            a = str(line)
            
        elif(option == '2'):
            filename = sys.argv[2]
            f = open(filename, "r")
            while True:
                line=f.readline()
                if(line == ''):
                    break
                a = a+line
            f.close()
        elif(option == '-h'):
            print("Help:")
            print("Please select option 1 for input from STDIN. Example: $python3 Test2.py 1 [10 9 8 7 6 5 4 3 2 1]")
            print("Please select option 2 for input from file. Example: $python3 Test2.py 2 test1000000.txt")
            sys.exit()
        else:
            print("Help:")
            print("Please select option 1 for input from STDIN. Example: $python3 Test2.py 1 [10 9 8 7 6 5 4 3 2 1]")
            print("Please select option 2 for input from file. Example: $python3 Test2.py 2 test1000000.txt")
            sys.exit()
            
        A = re.findall(r'\d+', a) 
        A = list(map(int, A))
        n = len(A)

        total = sort_and_count(A, 0, n-1) 
        print("Number of total inversions is: ", total)


  
