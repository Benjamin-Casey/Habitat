class Habitat_Node:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Habit(Habitat_Node):
    def __init__(self, name, description):
        super().__init__(name, description)


class Daily(Habitat_Node):
    def __init__(self, name, description, repetition_period):
        super().__init__(name, description)
        self.repetition_period = repetition_period

    def get_interval(self):
        #TODO
        pass


class Todo(Habitat_Node):
    def __init__(self, name, description):
        super().__init__(name, description)