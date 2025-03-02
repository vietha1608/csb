class Staff:
    def __init__(self,name, age, position, startedYear):
        self.name = name
        self.__age = age
        self.__positon = position
        self.__startedYear = startedYear

staff1 = Staff('a','18','CEO','2025')
print(staff1.name)
