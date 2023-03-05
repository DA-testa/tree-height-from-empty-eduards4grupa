# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    # Write this function
    children =[[] for _ in range(n)]
    for i in range(n):
        if parents[i]!=-1:
            children[parents[i]].append(i)
    def height(node)
    if not children[node]:
        return 1
    max_height=0
    else:
        max_height=max(height(child) for child in children[node])
    return 1+max_height
    #return max_height
        
    # Your code here
    #return max_height


def main():
    # implement input form keyboard and from files
    input_veids=input("write K to write from keyboard or F to do it from file    ")
    
    if input_veids=='K':
        n=int(input())
        parents=list(map(int, input().split()))
        print(compute_height(n, parents))
        break
    elif input_veids=='F':
        file_name=input("wirte name of file ")
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))
