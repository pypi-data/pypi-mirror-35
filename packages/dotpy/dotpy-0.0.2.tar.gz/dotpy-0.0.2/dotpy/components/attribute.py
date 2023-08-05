class Attribute:

    def __init__(self, first_attr, second_attr):
        self.first_attr = first_attr
        self.second_attr = second_attr

    def __str__(self):
        return "{0} = {1}".format(self.first_attr, self.second_attr)