# Базовые структуры
## Связный список
### Изменение списка:
- добавить элемент по индексу add_at(index, value)
- добавить в конец add (value)
- удалить элемент remove(index)
- перезаписать элемент rewrite(index)
- забрать элемент pop()

### Поиск по списку:
- первое вхождение search_first(value)
- все вхождения search_all(value) возвращает массив индексов
- первое вхождение с поиском в массиве search_first_in_array(index, value)
- все вхождения с поиском в массиве search_all_in_array(index, value)

### Получение данных:
- значение элемента по индексу element(int index)
- получение всего списка в виде массива as_array()


## Связный список с ключами
Наследует методы и свойства обычного связного списка
### Изменение списка:
- добавить элемент add(key, value)
- удалить элемент remove(key) | remove_at(index)
- перезаписать элемент rewrite(key)
### Поиск по списку:
Функции поиска возвращают ключи вместо индексов
- получить индекс get_index(key)


## Стек
Использует для хранения данных связный список
- добавить элемент push(value)
- забрать элемент pop()
- получить последний элемент peek()


## Очередь
Использует для хранения данных связный список
- добавить элемент в очередь enqueue(value)
- добавить элемент в начало очереди enqueue_first(value)
- забрать элемент из очередь dequeue()
- забрать элемент с конца очереди dequeue_last()
- получить последний элемент peek()


## Приоритетная очередь
Использует для хранения данных связный список
- добавить элемент в очередь в конец группы по приоритету enqueue(value, priority)
- добавить элемент в очереди в начало группы по приоритету enqueue_first(value, priority)
- забрать элемент из очередь dequeue()
- забрать элемент с конца очереди dequeue_last()
- получить последний элемент peek()


## Множество
Использует для хранения данных связный список

### Изменение списка
- добавить элемент add(value)
- удалить элемент remove(value)

### Сравнение множеств
- объединение множеств union(other_set, [other_set1])
- сходства intersection(other_set)
- различия difference(other_set)
- является ли множество подмножеством subset(other_set)

### Получение данных
- получить значения множества values()
- содержится ли значение во множестве has()
