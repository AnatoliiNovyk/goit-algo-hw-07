# Клас, що представляє окремий вузол у Двійковому Дереві Пошуку (BST)
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Функція для вставки нового вузла з заданим ключем у BST
def insert(root, key):
    # Якщо дерево порожнє, повертаємо новий вузол
    if root is None:
        return Node(key)
    else:
        # Інакше, рекурсивно спускаємося по дереву
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

# Створення тестового дерева для завдань 1, 2, 3
root = None
keys = [20, 8, 22, 4, 12, 10, 14, 25, 30]
for key in keys:
    root = insert(root, key)

def find_max(root):
    """
    Функція для знаходження найбільшого значення в BST.
    Рухається до крайнього правого вузла.
    """
    current = root
    # Цикл для переходу до крайнього правого нащадка
    while(current.right is not None):
        current = current.right
    return current.val

# Виклик функції та вивід результату
max_value = find_max(root)
print(f"Найбільше значення в дереві: {max_value}")

# Очікуваний результат: Найбільше значення в дереві: 30