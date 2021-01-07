class Guest:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class setStatus(Guest):
    def __init__(self, firstname, lastname, city, status):
        super().__init__(firstname, lastname)
        self.city = city
        self.status = status

    def printInfo(self):
        print('{} {}, г.{}, статус "{}"'.format(self.firstname, self.lastname, self.city, self.status))

guest_1 = setStatus("Геннадий", "Федорович", "Ростов-на-Дону", "Руководитель")
guest_1.printInfo()
