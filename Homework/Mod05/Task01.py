# Я работала с кодом, представленным в файле, также использовала подсказки по улучшению кода и добавляла комментарии для понимания логики выполнения программы.
class Node:
    """Вспомогательный класс для узлов списка"""
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """Основной класс для стека"""
    def __init__(self):
        self.end = None  # ссылка на конец стека (вершина)

    def push(self, val):
        """Добавление элемента val в конец списка"""
        new_node = Node(val)
        new_node.pref = self.end # Новый узел ссылается на старый конец
        self.end = new_node     # Конец теперь указывает на новый узел

    def pop(self):
        """Возвращение последнего элемента из списка с удалением"""
        if self.end is None:
            return None # Стек пуст
        
        val = self.end.data       # Запоминаем данные
        self.end = self.end.pref  # Смещаем конец на предыдущий элемент
        return val

    def print(self):
        """Вывод на печать содержимого стека"""
        current = self.end
        print("Stack (top to bottom):", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.pref
        print("None")

# Пример использования, который предлагается для проверки работы кода.
# Проверка, что код работает без ошибок.
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.print()       # Вывод: Stack (top to bottom): 30 -> 20 -> 10 -> None
print("Popped:", s.pop()) # Вывод: Popped: 30
s.print()       # Вывод: Stack (top to bottom): 20 -> 10 -> None
