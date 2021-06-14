# BubbleSort_PyAnimation

## Bubble Sort

A Bubble sort is an easy algorithm among the various sorting algorithms. We learn it as a first sorting algorithm. It is easy to learn and highly intuitive.
It can be easy to implement into the code, which is much beneficial for beginner software developers. But it is the worst algorithm for sorting the elements 
in every except because it checks every time the array is sorted or not.
This program shows visually how buuble sort work lika an animation.

### Programme

      import os
      import time

      lis=[9,8,7,6,5,4,3,2,4,3,2]

      def display(arr):
        n = len(arr)
        for i in range (n-1):
          print(arr[i],end=" : ")
          for j in range (arr[i]):
            print("#",end ="")
          print("\n")


      def buble(arr):
        n = len(arr)
        for i in range(0,n-1):

          for j in range(0,n-1):
            if arr[j]>arr[j+1]:
              t = arr[j]
              arr[j] =arr[j+1]
              arr[j+1] = t   
              os.system('clear')
              display(arr)
              time.sleep(1) 
        print(arr)
      buble(lis)

# Output

      2 : ##

      2 : ##

      3 : ###

      3 : ###

      4 : ####

      4 : ####

      5 : #####

      6 : ######

      7 : #######

      8 : ########

      [2, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9]
