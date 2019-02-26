#Write some code, that will flatten an array of arbitrary
#nested arrays of integers into a flat array of integers.
#e.g.:[[1,2,[3]],4]->[1,2,3,4]

import sys
import random


def check_array(array):
    '''Flatten array function'''
    new_array = []

    for item in array:
        if isinstance(item, int):
            new_array.append(item)
        elif isinstance(item, list):
            new_array += check_array(item)
    return sorted(new_array)


def create_array(remove=False):
    '''Randomize array function'''
    array = []
    number = random.randint(5,9)

    for i in range(number):
        if len(array) == 0:
            array.append(i+1)
        if random.randint(1,10) % 2 == 0:
            new_array = [(i+1)**2 for i in range(random.randint(1,9))]
            if random.randint(1,10) % 2 == 0:
                new_array.append(
                    [(i+1)**2 for i in range(random.randint(1,9))]
                )
            array.append(new_array)
        else:
            array.append((i+1)**2)

        if len(array) == number:
            flat_array = check_array(array)
            print ('Received array: ', array)

            '''Remove duplicates if asked to'''
            if remove:
                print('Flattened array: ', sorted(list(set(flat_array))))
            else:
                print('Flattened array: ', flat_array)

if __name__ == '__main__':
    repeated = raw_input(
        "Would like to remove repeated items from array:\n"
        "1 - Yes\n"
        "2 - No\n"
    )
    if int(repeated) == 1:
        create_array(True)
    else:
        create_array()


