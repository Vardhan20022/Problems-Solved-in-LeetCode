#User function Template for python3
import sys

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        # max=0
        # s=0
        # for i in range(len(arr)-1):
        #     s+=arr[i]
        #     if s>max:
        #         max=s
        #     if s<0:
        #         s=0
        # return max
        max_so_far = -10000
        max_ending_here = 0
 
        for i in range(0, N):
            max_ending_here = max_ending_here + arr[i]
            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
 
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far
        
 
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends