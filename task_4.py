class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        """Додає нову відповідь до коментаря."""
        # Перевірка, що відповідь є екземпляром класу Comment
        if isinstance(reply, Comment):
            self.replies.append(reply)
        else:
            print("Помилка: відповідь має бути об'єктом класу Comment.")

    def remove_reply(self):
        """
        "Видаляє" коментар, змінюючи його текст та встановлюючи прапорець.
        Фактично, коментар залишається в структурі, щоб зберегти відповіді на нього.
        """
        self.text = "Цей коментар було видалено."
        self.is_deleted = True
        self.author = "" # Опціонально, можна приховати автора

    def display(self, level=0):
        """Рекурсивно виводить коментар та всі його відповіді."""
        prefix = "    " * level
        if self.is_deleted:
            print(f"{prefix}{self.text}")
        else:
            print(f"{prefix}{self.author}: {self.text}")
        
        for reply in self.replies:
            reply.display(level + 1)

# Створення коментарів
root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

# Додавання відповідей до головного коментаря
root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

# Створення відповіді на відповідь
reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

# Створення ще одного рівня вкладеності
reply2_1 = Comment("Теж не зрозуміла захоплення.", "Олена")
reply2.add_reply(reply2_1)

print("--- Початкова структура коментарів ---")
root_comment.display()

# "Видалення" коментаря Андрія
reply1.remove_reply()

print("\n--- Структура після видалення коментаря ---")
root_comment.display()