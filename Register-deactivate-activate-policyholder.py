class PolicyHolder:
    # Simple in-memory list to store registered holders
    registry = []

    def __init__(self, surname, firstname, NIN, DateOfBirth, Occupation, Telephone):
        self.surname = surname
        self.firstname = firstname
        self.NIN = NIN
        self.DateOfBirth = DateOfBirth
        self.occupation = Occupation
        self.telephone = Telephone
        self.policy_numbers = []
        # default status
        self.status = "Active"

    @classmethod
    def nin_exists(cls, nin):
        """Check if a policyholder with this NIN is already registered."""
        for holder in cls.registry:
            if holder.NIN == nin:
                return True
        return False

    def register(self):
        """Register policyholder if NIN is unique."""
        if PolicyHolder.nin_exists(self.NIN):
            print(f"Registration FAILED: NIN '{self.NIN}' already exists.")
            return False
        
        PolicyHolder.registry.append(self)
        print(f"{self.firstname} {self.surname} registered successfully.")
        return True

    def suspend(self):
        if self.status == "Suspended":
            print(f"{self.firstname} {self.surname} is already suspended.")
            return False
        self.status = "Suspended"
        print(f"{self.firstname} {self.surname} has been SUSPENDED.")
        return True

    def reactivate(self):
        if self.status == "Active":
            print(f"{self.firstname} {self.surname} is already active.")
            return False
        self.status = "Active"
        print(f"{self.firstname} {self.surname} has been REACTIVATED.")
        return True
    
# Example usage
holder1 = PolicyHolder("Daphine", "Kwikiriza", "123451234", "01/01/1980", "doctor", "332-1234")
holder2 = PolicyHolder("Edna", "Kobusinge", "0000000101", "01/01/1980", "student", "576-1233")
holder1.register() 
holder2.register()  

holder1.suspend()
  
