class Node:

    def __init__(self, name, attr_list):
        self.name = str(name)
        self.attr_list = attr_list

    def __str__(self):
        if self.attr_list:
            return "{0} [{1}];".format(self.name, ", ".join(map(str, self.attr_list)))
        else:
            return "{0};".format(self.name)