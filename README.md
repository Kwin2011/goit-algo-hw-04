# Результати сортування

## Час виконання алгоритмів

- **Сортування злиттям** (Merge Sort): 0.2966 секунд
- **Сортування вставками** (Insertion Sort): 3.0162 секунд
- **Вбудоване сортування (Timsort)**: 0.0103 секунд

## Висновки

1. **Сортування злиттям** працює значно швидше, ніж **сортування вставками**. 
   - Час виконання для сортування злиттям становить приблизно **0.2966 секунд**, тоді як для сортування вставками — **3.0162 секунд**. 
   - Це відображає те, що сортування злиттям є ефективнішим для великих масивів, оскільки його середня складність — \(O(n \log n)\), в той час як у вставок — \(O(n^2)\).

2. **Вбудоване сортування (Timsort)** є найшвидшим з усіх трьох методів, з часом виконання приблизно **0.0103 секунд**. 
   - Timsort є адаптивним алгоритмом, який поєднує особливості сортування вставками і злиттям, тому він оптимізований для практичного використання і часто працює швидше на реальних даних.
