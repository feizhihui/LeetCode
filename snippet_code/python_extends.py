# encoding=utf-8
"""
继承Python内置类List
"""


class NameList(list):
    def __init__(self, name):
        list.__init__(list())  # initialize super class
        self.name = name
        self.d = {chr(i): i for i in range(97, 123)}

    def show_name(self):
        print(self.name)

    @property
    def to_dict(self):
        return self.d


if __name__ == '__main__':
    obj = NameList('My name is Han-meimei')
    print(dir(obj))
    obj.append(10)
    obj.extend([1, 2, 3, 4])
    print(obj[-1])
    print(len(obj))
    obj.show_name()
    NameList.show_name(obj)
    sorted_obj = sorted(obj)
    print(sorted_obj, type(obj))

