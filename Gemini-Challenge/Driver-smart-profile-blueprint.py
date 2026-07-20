# STEP 1: Blueprint taiyar karna (Class Definition)
class Driver:
    # Constructor: Driver ka naam aur rating save karne ke liye
    def __init__(self, name, rating):
        self.name = name       # Driver ka naam
        self.rating = rating   # Driver ki rating

    # STEP 2: Pure Logic Block (Method)
    def check_bonus(self):
        if self.rating >= 4.5:
            print("Eligible for Bonus")
        else:
            print("Standard Payout")

# STEP 3: Outside Execution (Asli driver ka object banana)
driver1 = Driver("Rahul Kumar", 4.7)
driver1.check_bonus()  # Output: Eligible for Bonus