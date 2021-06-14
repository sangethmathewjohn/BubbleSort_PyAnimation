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
