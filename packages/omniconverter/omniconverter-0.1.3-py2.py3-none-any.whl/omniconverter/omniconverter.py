class Converter:

    def __init__(self):
        pass

    def array_to_string(self, array):
        temp = []
        for i in array:
            temp.append(str(i))
        return "".join(temp)

    def string_to_array(self, string):
        return list(string)
