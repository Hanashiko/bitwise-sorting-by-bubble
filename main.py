import random

N = 10
start_file = "initialArray.txt"
end_file = "finalArray.txt"


def generate_array():
  """Створює двовимірний масив розміром N x N."""
  array = [[random.randint(0, 99) for j in range(N)] for i in range(N)]
  return array


def bubble_sort(array):
  """Порозрядне сортування, бульбашкове"""
  comparisons, swaps = 0, 0

  for i in range(len(array) - 1):
    for j in range(len(array) - i - 1):
      if array[j] > array[j + 1]:
        array[j], array[j + 1] = array[j + 1], array[j]
        swaps += 1
      comparisons += 1
    comparisons +=1
  return array, comparisons, swaps

def spiral_array(arr, mat):
  """Заповнює масив по спіралі."""
  top = 0
  bottom = N - 1
  left = 0
  right = N - 1

  index = 0

  while True:
    if left > right:
      break

    for i in range(top, bottom + 1):
      mat[i][left] = arr[index]
      index += 1
    left += 1

    if top > bottom:
      break

    for i in range(left, right + 1):
      mat[bottom][i] = arr[index]
      index += 1
    bottom -= 1

    if left > right:
      break

    for i in range(bottom, top - 1, -1):
      mat[i][right] = arr[index]
      index += 1
    right -= 1

    if top > bottom:
      break

    for i in range(right, left - 1, -1):
      mat[top][i] = arr[index]
      index += 1
    top += 1


def print_array_2d(array):
  """Виводить на консоль 2D масив."""
  for i in range(N):
    for j in range(N):
      print(f"{array[i][j]:>2}", end=" ")
    print()


def print_array_1d(array):
  """Виводить на консоль 1D масив."""
  print(*array)


def print_file(array, filename,comparisons=0,swaps=0):
  """Записує двовимірний масив у txt файл."""

  with open(filename, "w") as f:
    f.write(f"Number of comparisons {comparisons}\nNumber of permutations {swaps}\n")
    for row in array:
      f.write(" ".join(map(str, row)) + "\n")
  f.close()


def main():
  """Основна функція."""

  initial_array = generate_array()
  print("\nДвовимірний масив:")
  print_array_2d(initial_array)

  print_file(initial_array,start_file)

  sorted_array, comparisons, swaps = bubble_sort([item for subarray in initial_array for item in subarray])

  print(f"\nКількість порівнянь: {comparisons}")
  print(f"Кількість перестановок: {swaps}")

  print("\nВідсортований масив:")
  print_array_1d(sorted_array)

  print("\nСпіральний масив:")
  result_array = [[0 for i in range(N)] for j in range(N)]
  spiral_array(sorted_array, result_array)
  print_array_2d(result_array)
  print_file(result_array,end_file,comparisons,swaps)

if __name__ == "__main__":
  main()
