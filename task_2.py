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

def find_min(root):
    """
    Функція для знаходження найменшого значення в BST.
    Рухається до крайнього лівого вузла.
    Виправлено: додано обробку порожнього дерева.
    """
    # ПЕРЕВІРКА: Якщо дерево порожнє, неможливо знайти мінімум.
    if not root:
        return None # Повертаємо None як індикатор відсутності значення

    current = root
    while(current.left is not None):
        current = current.left
    return current.val

# Виклик функції та вивід результату
min_value = find_min(root)
print(f"Найменше значення в дереві: {min_value}")

# Очікуваний результат: Найменше значення в дереві: 4