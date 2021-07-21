def binary_search(mlist, item):
    low = 0
    high = len(mlist)-1

    while low < high:
        mid = int((low + high)/2)
        guess = mlist[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1


def main():
    inp_array = [1, 3, 5, 9, 34, 108, 512, 1024]
    print(inp_array)
    print(binary_search(inp_array, 9))


if __name__ == "__main__":
    main()
