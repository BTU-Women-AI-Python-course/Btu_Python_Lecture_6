class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"First name: {self.first_name}\nLast name: {self.last_name}"

class Doctor(Person):
    def __init__(self, first_name, last_name, hospital):
        super().__init__(first_name, last_name)
        self.hospital = hospital


doctor = Doctor("Nika", "Mdinaradze", "Hospital 1")
print(doctor)

