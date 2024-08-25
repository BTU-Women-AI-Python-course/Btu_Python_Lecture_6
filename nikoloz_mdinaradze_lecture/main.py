class Database:
    store = {}
    last_pk = 1
    def add_person(self, first_name, last_name, age):
        self.store[self.last_pk] = [first_name, last_name, age]
        self.last_pk += 1

    def _check_person(self, pk):
        person = self.store.get(pk)
        if not person:
            print("Not Found")
        return person

    def get_person(self, pk):
        person = self._check_person(pk)
        if not person:
            return
        print("-"*20)
        print(f"First name: {person[0]}\nLast name: {person[1]}\nAge: {person[2]}")
        print("-" * 20)

    def all_persons(self):
        for pk, person in self.store.items():
            print("-" * 20)
            print(f"PK:{pk}\nFirst name: {person[0]}")
            print("-" * 20)

    def delete_person(self, pk):
        person = self._check_person(pk)
        if not person:
            return
        self.store.pop(pk)


database = Database()
database.add_person("Nika", "Mdinaradze", 20)
database.add_person("Mariam", "Testiashvili", 20)
database.add_person("Giorgi", "Vigacashvili", 20)
database.all_persons()
database.get_person(100)
database.delete_person(200)

