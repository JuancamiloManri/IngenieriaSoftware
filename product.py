class Product: 
    def __init__(self, name, lastname, age):
        self.name = name
        self.lasname = lastname
        self.age = age

    def toDBCollection(self):
        return{
            'name': self.name,
            'lastname': self.lasname,
            'age': self.age
        }  