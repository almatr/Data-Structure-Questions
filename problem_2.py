import os

def find_files(suffix, path):

    if len(suffix) == 0 or len(path) == 0:
        return

    arr = os.listdir(path)
    new_list = list()
    for i in arr:
        new_list.append(os.path.join(path, i))
    return check_every_file(suffix, new_list, 0)

def is_directory(path):

    return os.path.isdir(path)

def is_file(path):

    return os.path.isfile(path)

def check_every_file(suffix, arr, index):

    if index == len(arr):
        return list()

    output = check_every_file(suffix, arr, index + 1)

    # if element is a list --> deep_reverse the list
    if is_directory(arr[index]):
        output.extend(find_files(suffix, arr[index]))
    elif is_file(arr[index]) and arr[index].endswith(suffix):
        output.append(arr[index])

    return output

#Test 1
listOfFiles = find_files(".c", "./")
print(listOfFiles)  #should print ['./testdir/subdir1/a.c', './testdir/subdir5/a.c', './testdir/t1.c',
                    # './testdir/subdir3/subsubdir1/b.c']

#Test 2
listOfFiles = find_files(".c", "./testdir/subdir1/")
print(listOfFiles)  #should print ['./testdir/subdir1/a.c']

#Test 3
listOfFiles = find_files(".c", "")
print(listOfFiles) #should print None
