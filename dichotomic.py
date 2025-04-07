def dichotomic(arr, val):  #imput list e un valore da veriricare
    if len(arr) == 1:
        if arr[0] == val:
            return True
        else: return False

    else:
        index = len(arr)//2
        return dichotomic(arr[:index], val) or dichotomic(arr[index:], val)


if __name__ == "__main__":
    arr = [1, 3, 4, 5, 6, 2, 14, 543, 45, 32]
    print(dichotomic(arr, 123))