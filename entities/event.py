from entities import entity


class Event(entity.Entity):
    def __init__(self, event_row):
        super().__init__()

        self.name = event_row.event

    def query_statement(self):
        return "INSERT INTO events (name) VALUES(?)"

    def parameters(self):
        return tuple([self.name,])