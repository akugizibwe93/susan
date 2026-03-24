
import datetime

class PaymentManagement:
    def __init__(self, amount_due, due_date, product_name, holder_name):
        self.amount_due = amount_due
        self.due_date = due_date
        self.product_name = product_name
        self.holder_name = holder_name

    # Make a payment
    def make_payment(self, amount_paid):
        if amount_paid <= 0:
            print("Please enter a valid amount.")
            return

        if self.amount_due <= 0:
            print("You have no outstanding payments.")
            return
        
        if amount_paid > self.amount_due:
            print(f"Amount paid exceeds amount due. Only {self.amount_due} will be applied.")
            amount_paid = self.amount_due

        # Apply payment
        applied = min(amount_paid, self.amount_due)
        self.amount_due -= applied

        print(f"{self.holder_name} paid {applied}. Remaining balance: {self.amount_due}")

    # Send a reminder if due soon
    def send_reminder(self):
        today = datetime.date.today()
        days_left = (self.due_date - today).days

        if self.amount_due > 0 and 0 <= days_left <= 5:
            print(f"Reminder: Your {self.product_name} payment is due on {self.due_date}.")
        else:
            print("No reminder needed today.")

    # Add penalty if past due
    def add_penalty(self):
        today = datetime.date.today()

        if today > self.due_date and self.amount_due > 0:
            penalty = round(self.amount_due * 0.05, 2)  # simple 5% penalty
            self.amount_due += penalty
            print(f"Late penalty of {penalty} added. New balance: {self.amount_due}")
        else:
            print("No penalty applied.")

# Example usage
initial_payment = PaymentManagement(500, datetime.date(2024, 6, 1), "Health Insurance", "Alice")
initial_payment.make_payment(1000)
initial_payment.send_reminder()
initial_payment.add_penalty()