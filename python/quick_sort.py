def swap(array, i, j):
  t = array[i]
  array[i] = array[j]
  array[j] = t

def find_partition_index(array, low, high):
  i = low
  j = high
  pivot = array[low]
  while(i<j):
    while((i in range(low, high+1)) and array[i] <= pivot): # = needed to move i from the pivot
      i+=1
    while((j in range(low, high+1)) and array[j] > pivot):
      j-=1
    if(i<j): # Do this only if i<j, if i==j, we do diffn thing
      swap(array, i, j)

  swap(array, low, j)
  return j

def q_sort(array, low, high):
  if high <= low:
    return
  partition_index = find_partition_index(array, low, high)
  q_sort(array, low, partition_index-1)
  q_sort(array, partition_index+1, high)

def main():
  array = [5, 4, 3, 2, 1]
  q_sort(array, 0 , len(array)-1)
  print array

if __name__ == "__main__":
  main()
