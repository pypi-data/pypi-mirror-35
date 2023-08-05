class AttributeStatement:

    def __init__(self, keyword, attr_list):
        self.keyword = keyword
        self.attr_list = attr_list

    def __str__(self):
        if self.keyword:
            return "{0} [{1}];".format(self.keyword, ", ".join(map(str, self.attr_list)))
        else:
            return "{0};".format(" ".join(map(str, self.attr_list)))