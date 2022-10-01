"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Bonus:
    def __init__(self, isFlatCommission, commissionNum, pricepercommission=0):
        self.isFlatCommission = isFlatCommission
        self.commissionNum = commissionNum
        self.pricepercommission = pricepercommission

    def get_commission(self):
        if self.isFlatCommission:
            return self.pricepercommission
        else:
            return self.pricepercommission * self.commissionNum


class Employee:
    def __init__(self, name, isFlatCommission, commissionNum, pricepercommission=0):
        self.name = name
        self.bonus = Bonus(isFlatCommission, commissionNum, pricepercommission)

    def get_pay(self):
        pass

    def __str__(self):
        return self.name

    def get_string(self, input):
        returnstring = input
        if self.bonus.isFlatCommission and self.bonus.commissionNum != 0:
            returnstring += f" and receives a bonus commission of {self.bonus.get_commission()}."
        elif self.bonus.commissionNum > 0:
            returnstring += f" and receives a commission for {self.bonus.commissionNum} contract(s) at {self.bonus.pricepercommission}/contract."
        else:
            returnstring += "."
        returnstring += f"  Their total pay is {self.get_pay()}."
        return returnstring


class SalaryEmployee(Employee):
    def __init__(self, name, salary, isFlatCommission, commissionNum, pricepercommission=0):
        super().__init__(name, isFlatCommission, commissionNum, pricepercommission)
        self.salary = salary

    def get_pay(self):
        return self.salary + self.bonus.get_commission()

    def __str__(self):
        return super().get_string(f"{self.name} works on a monthly salary of {self.salary}")


class ContractEmployee(Employee):

    def __init__(self, name, contractperhour, contracthours, isFlatCommission, commissionNum, pricepercommission=0):
        super().__init__(name, isFlatCommission, commissionNum, pricepercommission)
        self.contractperhour = contractperhour
        self.contracthours = contracthours

    def get_pay(self):
        return (self.contracthours * self.contractperhour) + self.bonus.get_commission()

    def __str__(self):
        return super().get_string(
            f"{self.name} works on a contract of {self.contracthours} hours at {self.contractperhour}/hour")


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = SalaryEmployee('Billie', 4000, True, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = ContractEmployee('Charlie', 25, 100, True, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = SalaryEmployee('Renee', 3000, False, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = ContractEmployee('Jan', 25, 150, False, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = SalaryEmployee('Robbie', 2000, True, 1, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = ContractEmployee('Ariel', 30, 120, True, 1, 600)
