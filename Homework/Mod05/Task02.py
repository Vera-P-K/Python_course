# За основу взят код из файла.
# При выполнении задания порядок функций был изменен, поскольку столкнулась с ошибками при выполнении.
# Также представлен "Пример для выполнения", чтобы проверить.ю работает ли код. Использованы подсказки из интернет-сообщества.
class Node:
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел

class Queue:
    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None    # ссылка на конец очереди

    def push(self, val):
        """Добавление элемента val в конец очереди (FIFO)"""
        new_node = Node(val)
        if self.end is None:  # Если очередь пуста
            self.start = new_node
            self.end = new_node
        else:
            new_node.pref = self.end  # Новый узел ссылается назад на старый конец
            self.end.nref = new_node  # Старый конец ссылается вперед на новый
            self.end = new_node       # Конец теперь указывает на новый узел

    def pop(self):
        """Возвращаем элемент из начала очереди с удалением"""
        if self.start is None:
            return None  # Очередь пуста
        
        val = self.start.data
        self.start = self.start.nref  # Переносим старт на следующий узел
        
        if self.start is None:
            self.end = None  # Если удалили последний элемент
        else:
            self.start.pref = None  # Обнуляем ссылку на старый первый узел
            
        return val

    def insert(self, n, val):
        """Вставить элемент val после элемента с номером n (индексация с 0)"""
        new_node = Node(val)
        current = self.start
        
        # Находим узел с номером n
        for _ in range(n):
            if current:
                current = current.nref
            else:
                break
        
        if current is None: # Если список меньше n, можно добавить в конец или выбросить ошибку
            self.push(val)
            return

        # Вставка после узла current
        next_node = current.nref
        
        new_node.nref = next_node
        new_node.pref = current
        current.nref = new_node
        
        if next_node:
            next_node.pref = new_node
        else:
            self.end = new_node # Если вставили в самый конец

# Пример использования (пишет только значение 10):
q = Queue()
q.push(10)
q.push(20)
q.push(30) # Очередь: 10 <-> 20 <-> 30
print(q.pop()) # 10, Очередь: 20 <-> 30
q.insert(0, 15) # Вставить 15 после 0-го элемента (после 20) -> 20 <-> 15 <-> 30
