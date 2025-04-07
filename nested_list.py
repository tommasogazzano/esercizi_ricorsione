def count_leaf_notes(input_list):
    if len(input_list) == 0:
        return 0
    else:
        counter = 0
        for e in input_list:
            if type(e) is list:
                counter += count_leaf_notes(e)
            else:
                counter += 1
        return counter



if __name__ == '__main__':
    print(count_leaf_notes([1, 2, [3, 4, 5], 6]))