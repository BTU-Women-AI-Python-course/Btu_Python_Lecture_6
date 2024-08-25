class Invoice:
    def __init__(self, cost, from_person, to_person, credit_card):
        self._cost = cost
        self.from_person = from_person
        self.to_person = to_person
        self.__credit_card = credit_card

    def set_cost(self, cost):
        if cost < 0:
            print("Invalid cost")
        else:
            self._cost = cost

    def get_credit_card(self):
        getter_card = self.__credit_card // 10000
        return f"{getter_card}****"

    def __str__(self):
        return f"{self._cost}, {self.from_person}, {self.to_person}"


invoice = Invoice(5, "Person A", "Person B", 11111111)
invoice.set_cost(-9)
print(invoice.get_credit_card())
