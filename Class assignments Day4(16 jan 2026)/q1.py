class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def display_details(self):
        print("Name:",self.name)
        print("Rollno:",self.rollno)

s1=student("Anunay",101)
s1.display_details()
s2=student("Anshal",102)
s2.display_details()