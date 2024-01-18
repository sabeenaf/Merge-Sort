
def merge_sort(arr):
  index=len(arr)//2
  if index==0:
    return
  left_arr=arr[:index]
  right_arr=arr[index:]
  merge_sort(left_arr)
  merge_sort(right_arr)
  merge(left_arr,right_arr,arr)

def merge(left_arr, right_arr, arr):
  sorted=0
  left_index=0
  right_index=0
  while left_index<len(left_arr) and right_index<len(right_arr):
    #print('left',left_arr,'right',right_arr)
    if left_arr[left_index]<right_arr[right_index]:
      arr[sorted]=left_arr[left_index]
      left_index+=1
    else:
      arr[sorted]=right_arr[right_index]
      right_index+=1
    sorted+=1
  while left_index<len(left_arr):
    arr[sorted]=left_arr[left_index]
    left_index+=1
    sorted+=1
  while right_index<len(right_arr):
    arr[sorted]=right_arr[right_index]
    right_index+=1
    sorted+=1
  #print('sorted',arr)




arr=[7,83,6,4,1,2,10]
merge_sort(arr)
print('Sorted Array: ',arr)