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

def sum_all_values(root):
    """
    Функція для знаходження суми всіх значень у дереві.
    Використовує рекурсивний обхід.
    """
    if root is None:
        return 0
    # Рекурсивно додаємо значення поточного вузла, лівого та правого піддерев
    return root.val + sum_all_values(root.left) + sum_all_values(root.right)

# Виклик функції та вивід результату
total_sum = sum_all_values(root)
print(f"Сума всіх значень у дереві: {total_sum}")

# Очікуваний результат: Сума всіх значень у дереві: 145 (20+8+22+4+12+10+14+25+30)