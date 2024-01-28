from entities import entity


class Sport(entity.Entity):
    def __init__(self, event_row):
        super().__init__()

        self.name = event_row.sport

    def query_statement(self):
        return "INSERT INTO sports (name) VALUES(?)"

    def parameters(self):
        return tuple([self.name,])