class  dictionary_iter:
    def __init__(self, dictionary):
        self.dictionary = dictionary
        self.keys = list(self.dictionary.keys())
        self.values = list(self.dictionary.values())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > len(self.keys) - 1:
            raise StopIteration
        result = (self.keys[self.index], self.values[self.index])
        self.index += 1
        return result

# Solution from teacher

# class dictionary_iter:
#     def __init__(self, dictionary):
#         self.dict_tuple = list(dictionary.items())
#         self.i = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.i < len(self.dict_tuple):
#             i = self.i
#             self.i += 1
#             return self.dict_tuple[i]
#         else:
#             raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# Create a class called dictionary_iter. Upon initialization,
# it should receive a dictionary object. Implement the iterator to return
# each key-value pair of the dictionary as a tuple of two elements (the key and the value).
#
# Output:
# (1, '1
# (2, '2')
