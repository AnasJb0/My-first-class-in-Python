class Employer():
    def __init__(self, number, name, sales, bonushrs, basesalary=0):
        self.number = number
        self.name = name
        self.sales = sales
        self.bonushrs = bonushrs
        self.basesalary = basesalary
    def info(self):
        print("The employee number is {}. Name is {}. Base salary is {}. Sales are {}.".format(self.number, self.name, self.basesalary, self.sales))
emp1 = Employer(1, "Anas", 30000, 35)
emp2 = Employer(2, "Mohammed", 2000, 50,6000)
emp1.info()
emp2.info()