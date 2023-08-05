class Edge:

    def __init__(self, source, destination, attr_list):
        self.source = str(source)
        self.destination = str(destination)
        self.attr_list = attr_list

    def __str__(self):
        if self.attr_list:
            return "{0} -> {1} [{2}];".format(self.source, self.destination, " ".join(map(str, self.attr_list)))
        else:
            return "{0} -> {1};".format(self.source, self.destination)

    def get_source(self):
        return self.source

    def get_destination(self):
        return self.destination

    def get_label(self):
        if self.attr_list:
            return str(self.attr_list[0])[8:]
        else:
            return ''