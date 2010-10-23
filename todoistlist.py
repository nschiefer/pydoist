class TodoistList(list):
    def __init__(self, user):
        self.user = user

    def delete(self):
        for member in self:
            member.delete()
            self.remove(member)

