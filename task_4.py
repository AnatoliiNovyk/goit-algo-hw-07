from typing import List, Type

class Comment:
    """
    Клас для представлення ієрархічної структури коментарів.
    Включає покращену обробку помилок та анотації типів.
    """
    def __init__(self, text: str, author: str):
        self.text: str = text
        self.author: str = author
        self.replies: List['Comment'] = []
        self.is_deleted: bool = False

    def add_reply(self, reply: 'Comment'):
        """
        Додає нову відповідь до коментаря.
        Викликає TypeError, якщо відповідь не є екземпляром класу Comment.
        """
        if not isinstance(reply, Comment):
            # Замість друку помилки генеруємо виняток
            raise TypeError("Відповідь має бути екземпляром класу Comment.")
        self.replies.append(reply)

    def remove_reply(self):
        """
        "М'яке видалення" коментаря: змінює текст та встановлює прапорець.
        Структура нащадків зберігається.
        """
        self.text = "Цей коментар було видалено."
        self.author = "" # Приховуємо автора
        self.is_deleted = True

    def display(self, level: int = 0):
        """
        Рекурсивно виводить коментар та всі його відповіді з відступами.
        """
        prefix = "    " * level
        if self.is_deleted:
            print(f"{prefix}{self.text}")
        else:
            print(f"{prefix}{self.author}: {self.text}")
        
        for r in self.replies:
            r.display(level + 1)

# Створення коментарів
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

# Додавання відповідей
root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

# Вкладена відповідь
reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# "Видалення" коментаря Андрія
reply1.remove_reply()

print("--- Структура коментарів після оновлення коду ---")
root_comment.display()

# Тестування обробки помилок
print("\n--- Тестування обробки помилок ---")
try:
    # Спроба додати відповідь неправильного типу
    root_comment.add_reply("Це не коментар, а просто рядок")
except TypeError as e:
    print(f"Успішно перехоплено помилку: {e}")