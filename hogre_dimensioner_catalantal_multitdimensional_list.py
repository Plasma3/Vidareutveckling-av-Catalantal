

class N_Dim_list():
    value = []      # the mega-gega-giga list
    dimensions = [] # the dimension of said list

    # returns the value for a index
    def getValue(self, index):
        # get the element at index (if there's a list at index, the output is a list of len(dimesnions) - len(index) -dimension)
        output = self._getListReference(index)
        # return the integer
        if type(output) is int: return output
        # otherwise, return a copy and not a refrence of the list (because grrrr python)
        return output.copy()

    # sets a value at index
    def setValue(self, index, value):
        # get a refrence to the list including the element (because lists returns refrences)
        segment =  self._getListReference(index[:-1])
        # update the refrenced list with the new element
        segment[index[-1]] = value


    # returns a refrence to a list at index
    def _getListReference(self, index:list):
        # if a argument is empty, return a refrence of the entire list-matrix
        if len(index) == 0: return self.value
        # start iterate through the list-matrix until specified list is found (and a refrence is returned)
        return self._iterateListReference(
            index, 0, self.value
        )
    
    # iterates through the list-matrix until specified list (or int-element) is found (and a refrence (if list) is found)
    def _iterateListReference(self, index:list, depth:int, segment):
        # if an element is found, return that element
        if type(segment) is int: return segment
        # if arrived at the specified list, return a refrence to it
        if depth == len(index):  return segment
        # continue to the next level
        return self._iterateListReference(index, depth + 1, segment[index[depth]])

    def _iterateCreate(self, depth:int, index:list):
        if depth == len(self.dimensions): 
            return -1
        segment = self._getListReference(index[:depth - 1])
        segment[index[-1]] = [None for _ in range(self.dimensions[depth])]
        for i in range(self.dimensions[depth]):
            segment[index[-1]][i] = self._iterateCreate(depth + 1, index + [i])
        return segment[index[-1]]

    def create(self, dimensions:list):
        self.dimensions = dimensions
        self.value = [None for _ in range(self.dimensions[0])]
        for i in range(self.dimensions[0]):
            self.value[i] = self._iterateCreate(1, [i])


# === OLD TESTCODE PLEASE IGNORE ===
# x = N_Dim_list()
# x.create([2, 3, 2])

# x.value = [
#     [[1, 1, 5], [1, 2, 5], [1, 3, 5]],
#     [[2, 1, 5], [2, 2, 5], [2, 3, 5]],
#     [[3, 1, 5], [3, 2, 5], [3, 3, 5]]
# ]

# b = x.getListReference([0, 1])
# b[2] = 17

# print(x.setValue([1, 2, 0], 15))

# print("======")
# print(x.value)