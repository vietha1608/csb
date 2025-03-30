
def bubble_sort(arr) ->list:
    arr_size = len(arr)
    for i in range(arr_size):
        for j in range(0, arr_size-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
def merge_sorted_array(nums1, nums2):
    result = nums1 + nums2
    print (bubble_sort(arr = result))
merge_sorted_array(nums1= [1, 2, 3], nums2= [2, 5, 6])