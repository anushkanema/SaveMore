class Person:
    def __init__(self, name, bal, goal):
        self.exp = 0
        self.name = name
        self.bal = bal
        self.goal = goal
        self.savings = 0

    def show_balance(self):
        print(f"Name: {self.name} \nBalance: {self.bal}")

    def debit(self, exp):
        self.exp = exp
        if exp > self.bal:
            print("Insufficient Balance")
        else:
            if self.bal > 0:
                        self.bal = self.bal - self.exp
            else:
                print("No amount left!")

    def credit(self, cre):
        self.bal = self.bal + cre

    def set_goal(self, goal):
        self.goal = goal
        print(f"Goal set: {self.goal}")

    def check_goal(self):
        if self.goal == 0:
            print("Set Goal first")
        else:
            print(f"Goal set is: {self.goal}")
            if self.bal > self.goal:
                   print(f"So far so good. You have saved {self.bal-self.goal} more than your goal")
            elif self.bal==self.goal:
                   print("You are at par with your goal!")
            else:
                   print(f"Keep Going! You need {self.goal-self.bal} more to reach your goal!")


A = Person("Anjali", 500, 350)
A.show_balance()
A.debit(1000)
A.credit(400)
A.debit(800)
A.show_balance()
A.check_goal()