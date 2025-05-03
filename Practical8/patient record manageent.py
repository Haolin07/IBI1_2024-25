class Patients:
    def __init__(self, name, age, latest_admission_date, medical_history):
        self.name = name
        self.age = age
        self.latest_admission_date = latest_admission_date
        self.medical_history = medical_history
    
    def print_details(self):
        print(f"Patient: {self.name}, Age: {self.age}, Latest Admission: {self.latest_admission_date}, Medical History: {self.medical_history}")

# Example usage
if __name__ == "__main__":
    # Create a patient instance
    patient1 = Patients(
        "Stephen Curry", 
        37, 
        "2025-3-20", 
        "fracture of the coccyx"
    )
    patient2 = Patients(
        "Kevin Durant", 
        37, 
        "2019-6-10", 
        "rupture of the achilles tendon"
    )
    patient3 = Patients(
        "Klay Thompson", 
        35, 
        "2019-6-14", 
        "Cruciate ligament rupture"
    )
    
    
    # Print patient details
    print("Patient Record:")
    patient1.print_details()
    patient2.print_details()
    patient3.print_details()