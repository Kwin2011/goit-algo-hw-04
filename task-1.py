import timeit
import random

# Функція для сортування злиттям
def merge_sort(array):
    if len(array) > 1:
        mid_index = len(array) // 2
        left_half = array[:mid_index]
        right_half = array[mid_index:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        # Зливаємо відсортовані частини
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        # Додаємо залишки з лівої частини
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        # Додаємо залишки з правої частини
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

# Функція для сортування вставками
def insertion_sort(array):
    for index in range(1, len(array)):
        key = array[index]
        position = index - 1
        # Зсуваємо елементи, які більші за ключ
        while position >= 0 and key < array[position]:
            array[position + 1] = array[position]
            position -= 1
        array[position + 1] = key

# Генеруємо випадковий масив
random_array = [random.randint(1, 10000) for _ in range(1000)]

# Вимірюємо час для сортування злиттям
merge_sort_time = timeit.timeit(lambda: merge_sort(random_array.copy()), number=100)
# Вимірюємо час для сортування вставками
insertion_sort_time = timeit.timeit(lambda: insertion_sort(random_array.copy()), number=100)
# Вимірюємо час для вбудованого Timsort
timsort_time = timeit.timeit(lambda: sorted(random_array.copy()), number=100)

print(f"Час сортування злиттям: {merge_sort_time} секунд")
print(f"Час сортування вставками: {insertion_sort_time} секунд")
print(f"Час Timsort (вбудований): {timsort_time} секунд")

# Висновок
if merge_sort_time < insertion_sort_time:
    print("Сортування злиттям працює швидше, ніж сортування вставками.")
else:
    print("Сортування вставками працює швидше, ніж сортування злиттям.")

if timsort_time < merge_sort_time and timsort_time < insertion_sort_time:
    print("Вбудоване сортування (Timsort) є найшвидшим.")
