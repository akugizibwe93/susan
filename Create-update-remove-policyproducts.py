
policholderdata = __import__('Register-deactivate-activate-policyholder')
ph = policholderdata.PolicyHolder.registry[0]  # Get the first registered policy holder


class InsuranceProduct:
    # In‑memory product storage
    registry = []
    _policy_counter = 1000    # starting point for generating unique policy numbers

    def __init__(self, policy_name, Policy_duration, PolicyHolder):
        # Save policyholder info
        self.surname = PolicyHolder.surname
        self.firstname = PolicyHolder.firstname
        self.NIN = PolicyHolder.NIN
        self.DateOfBirth = PolicyHolder.DateOfBirth
        self.occupation = PolicyHolder.occupation
        self.telephone = PolicyHolder.telephone
        self.holder = PolicyHolder

        # Product info
        self.policy_name = policy_name
        self.Policy_duration = Policy_duration

        # Auto‑generated unique policy number
        InsuranceProduct._policy_counter += 1
        self.Policy_number = f"POL-{InsuranceProduct._policy_counter}"

        # Product status
        self.status = "Active"

    # ---------- Create ----------
    def create(self):
        InsuranceProduct.registry.append(self)
        
        if not hasattr(self.holder, "policy_numbers"):
            self.holder.policy_numbers = []
        if self.Policy_number not in self.holder.policy_numbers:
            self.holder.policy_numbers.append(self.Policy_number)

        print(
            f"Product '{self.policy_name}' created with Policy Number: {self.Policy_number} "
            f"for {self.firstname} {self.surname}"
        )

        return self

    # ---------- Update ----------
    def update(self, policy_name=None, Policy_duration=None, telephone=None, occupation=None):
        if policy_name is not None:
            self.policy_name = policy_name
        if Policy_duration is not None:
            self.Policy_duration = Policy_duration
        if telephone is not None:
            self.telephone = telephone
        if occupation is not None:
            self.occupation = occupation


        print(f"Product '{self.Policy_number}' updated.")
        return self

    # ---------- Suspend / Reactivate ----------
    def suspend_product(self):
        if self.status == "Suspended":
            print(f"Product '{self.Policy_number}' is already suspended.")
            return False
        self.status = "Suspended"
        print(f"Product '{self.Policy_number}' has been SUSPENDED.")
        return True

    def reactivate_product(self):
        if self.status == "Active":
            print(f"Product '{self.Policy_number}' is already active.")
            return False
        self.status = "Active"
        print(f"Product '{self.Policy_number}' has been REACTIVATED.")
        return True

    # ---------- Remove ----------
    def remove(self):
        try:
            InsuranceProduct.registry.remove(self)
            print(f"Product '{self.Policy_number}' REMOVED.")
            return True
        except ValueError:
            print("Product not found.")
            return False

    # ---------- Lookup helpers ----------
    @classmethod
    def list_all(cls):
        return cls.registry

    @classmethod
    def find_by_policy_number(cls, policy_no):
        for p in cls.registry:
            if p.Policy_number == policy_no:
                return p
        return None
    
# Example usage
# Create

prod1 = InsuranceProduct("life insurance", "36 months", ph)
prod1.create()

print(prod1.Policy_number) 

