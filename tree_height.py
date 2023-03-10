# python3

import sys
import threading
#import numpy


def compute_height(n, parents):
    # Write this function
    children =[[] for _ in range(n)]
    for i in range(n):
        if parents[i]!=-1:
            root = i
        else:
            children[parents[i]].append(i)
            
            
    def height(node):
        if not children[node]:
            return 1
        max_h=0
        for child in children[node]:
            h=height(child)
            max_h=max(max_h, h)
        return max_h+1
        #else:
            #max_height=max(height(child) for child in children[node])
            #return 1+max(height(child) for child in children[node])
    #root=parents.index(-1)
    return height(root)
        
    # Your code here
    #return max_height


def main():
    # implement input form keyboard and from files
    input_veids=input()
    
    if 'I' in input_veids:
        n=int(input())
        parents=list(map(int, input().split()))
        print(compute_height(n, parents))
        
    elif 'F' in input_veids:
        file_name=input()
        #if 'a' in file_name:
         #   print("file name cant contain a letter")
        #    exit()
        #else:
        with open ('./test/' + file_name, 'r') as file:
            n=int(file.readline())
            parents=list(map(int, file.readline().split()))
            print(compute_height(n, parents))
    #else:
     #   print("You have to write K or F!")
      #  exit()
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))
