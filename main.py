from random import randint

def bubble_sort(array):
  array_length = len(array)
  for i in range(array_length-1):
    for j in range(array_length-i-1):
        if array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]

def selection_sort(array):
  array_length = len(array)
  for i in range(array_length):
    current_minimal = array[i]
    index_of_minimal = i
    for j in range(i, array_length):
      if array[j] < current_minimal:
        current_minimal = array[j]
        index_of_minimal = j
        array[i], array[j] = array[j], array[i]
  

array = list() 
length = randint(10, 40)
for element in range(length):
  array.append(randint(1,1000))

print(bubble_sort(array))
print(selection_sort(array)) 

 