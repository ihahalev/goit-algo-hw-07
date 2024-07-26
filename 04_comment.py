from __future__ import annotations

class Comment:
    def __init__(self, text:str, author:str):
        if not author.strip():
            print("Author name is empty")
            return
        if not text.strip():
            print("Comment text is empty")
            return
        self.text = text
        self.author = author
        self.replies:list[Comment] = []
        self.is_deleted = False

    def __str__(self, level=0):
        ret = f"{"\t"*level}{self.author}: {self.text}\n"
        if self.is_deleted:
            ret = f"{"\t"*level}Цей коментар було видалено.\n"
        if len(self.replies):
            for reply in self.replies:
                ret += reply.__str__(level+1)
        return ret

    def add_reply(self, reply:Comment):
        self.replies.append(reply)

    def remove_reply(self):
        self.is_deleted = True

    def display(self):
        print(self)

root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()