import Strategy


class CreateNewStrategy(Strategy):
    def create(self, event_row, register):
        entity = self.lookup_callback(event_row, register)

        return entity

