def linearSearch(item, list, print=True):
    found = False
    position = 0
    
    while position < len(list) and not found:
        if list[position] == item:
            found  = True
        position += 1
    return found

def binarySearch(item, list):
    if len(list) == 1:
        return item == list[0]
    
    middle = len(list) // 2
    
    if list[middle] > item:
        return binarySearch(item, list[:middle])
    
    if list[middle] < item:
        return binarySearch(item, list[middle:])
    
    return True

def bubbleSort(list):
    for index in range(len(list)):
        for item in range((len(list) - 1) - index):
            if list[item] > list[item + 1]:
                # Swap their positions
                list[item], list[item + 1] = list[item + 1], list[item]

    return list

def mergeSort(list, display=True):
    if len(list) > 1:
        middle = len(list) // 2
        left = list[:middle]; right = list[middle:]
        if display:
            print('\tSplit to', left, right)
        mergeSort(left); mergeSort(right)

        a = b = 0
        for item in range(len(list)):
            L = left[a] if a < len(left) else None
            R = right[b] if b < len(right) else None
            
            if ((L and R) and (L < R)) or R is None:
                list[item] = L; a += 1

            elif ((L and R) and (L >= R)) or L is None:
                list[item] = R; b += 1
        if display:
            print('\t\tMerging', left, right)

    return list

if __name__ == '__main__':
    while True:
        # Run Linear Search
        cards = ['King Spades', 'Queen Spades', 'Ace Spades', 'King Hearts', 'Queen Hearts']
        item = input('What card do you want to find? ')
        found = linearSearch(item, cards)
        if found:
            print('Your linear search has found the card requested.')
        else:
            print('Your card is not in the list.')

        # Run Binary Search
        list = [1, 2, 3, 4, 5, 6] # Note: list is sorted
        num = int(input('What number do you want to find? '))
        print(binarySearch(num, list))

        # Run Bubble Sort
        list = [6, 4, 3, 5, 2, 1]
        print('Bubble Sort\nList:', list)
        sortedList = bubbleSort(list)
        print('Sorted List:', sortedList)

        # Run Merge Sort
        list = [6, 4, 3, 5, 2, 1]
        print('Merge Sort\nList:', list)
        list = mergeSort(list, display=True)
        print('Sorted List:', list)
