
import datetime

class PaymentManagement:
    def __init__(self, amount_due, due_date, product_name, holder_name):
        self.amount_due = amount_due
        self.due_date = due_date
        self.product_name = product_name
        self.holder_name = holder_name

    def make_payment(self, amount_paid):
        if amount_paid <= 0:
            print("Please enter a valid amount.")
            return

        if self.amount_due <= 0:
            print("You have no outstanding payments.")
            return

        applied = min(amount_paid, self.amount_due)
        self.amount_due -= applied

        print(f"{self.holder_name} paid {applied}. Remaining balance: {self.amount_due}")

    def send_reminder(self):
        today = datetime.date.today()
        days_left = (self.due_date - today).days

        if self.amount_due > 0 and 0 <= days_left <= 5:
            print(f"Reminder: Your {self.product_name} payment is due on {self.due_date}.")
        else:
            print("No reminder needed today.")

    def add_penalty(self):
        today = datetime.date.today()

        if today > self.due_date and self.amount_due > 0:
            penalty = round(self.amount_due * 0.05, 2)
            self.amount_due += penalty
            print(f"Late penalty of {penalty} added. New balance: {self.amount_due}")
        else:
            print("No penalty applied.")


# ✅ Create at least two policyholders who already paid

holder1 = PaymentManagement(
    amount_due=100000,
    due_date=datetime.date(2026, 3, 25),
    product_name="Motor Comprehensive",
    holder_name="John Smith"
)

holder2 = PaymentManagement(
    amount_due=150000,
    due_date=datetime.date(2026, 3, 25),
    product_name="Health Insurance",
    holder_name="Susan Akugizibwe"
)

# ✅ They make payments
holder1.make_payment(60000)
holder2.make_payment(150000)   # Susan clears full amount

# ✅ Display their account details
print("\n------ ACCOUNT DETAILS ------")
print(f"Holder: {holder1.holder_name}\nProduct: {holder1.product_name}\nAmount Due: {holder1.amount_due}\nDue Date: {holder1.due_date}")

print("\n------------------------------")
print(f"Holder: {holder2.holder_name}\nProduct: {holder2.product_name}\nAmount Due: {holder2.amount_due}\nDue Date: {holder2.due_date}")


