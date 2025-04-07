def quicksort(arr):
    if len(arr) <= 1:
        return arr

    else:
        #1) scegliere i pivot
        pivot = arr[0]
        #2) dividere sequenza in sottosequenze
        arr_smaller = []
        arr_bigger  =[]
        arr_pivot = [] #ci possono essere più pivot uguali

        for i in arr:
            if i < pivot:
                arr_smaller.append(i)
            elif i > pivot:
                arr_bigger.append(i)
            else:
                arr_pivot.append(i)
        return (quicksort(arr_smaller) + arr_pivot + quicksort(arr_bigger))



if __name__ == "__main__":
    arr = [3, 5, 9, 2, 11, 4, 24, 52, 14]
    print(quicksort(arr))