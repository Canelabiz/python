class Id_Generator:
    def __init__(self):
        self.id = 0

    def generate(self):
        self.id = self.id + 1
        return self.id


class Employee:
    def __init__(self, Name, id_gen) -> None:
        self.Id = id_gen.generate()
        self.Name = Name
        self.D_id = None
        self.Salary = None

    def printDetails(self):
        print("\n")
        print("Employee Details:")
        print(f"ID: {self.Id}")
        print(f"Name: {self.Name}")
        print(f"Salary: {self.Salary}")
        print("-" * 17)


class Programmer(Employee):
    def __init__(
        self, name, id_gen, lang=None, db=None, projects=None, **add_skills
    ) -> None:
        self.languages = lang
        self.db = db
        self.projects = projects
        self.add_skills = add_skills
        super().__init__(name, id_gen)

    def printSkillDetails(self):
        print(f"ID: {self.Id}")
        print(f"Name: {self.Name}")
        print(f"Salary: {self.Salary}")
        print("Languages: ")
        for l in self.languages:
            print(f"\t{l}")
        print("Databases: ")
        for d in self.db:
            print(f"\t{d}")
        print("Projects: ")
        for p in self.projects:
            print(f"\t{p}")
        print("Add Skills: ")
        for k, v in self.add_skills.items():
            print(f"\t{k}: ")
            for skill in v:
                print(f"\t\t{skill}")


Id_gen = Id_Generator()
p = Programmer(
    "Programmer1",
    Id_gen,
    ["C#", "Python"],
    ["SQLite"],
    ["Finance", "InfoSec", "Bug-Bounty", "Ethical Hacking"],
    os=["Windows", "Dos", "Parrot OS", "Kali", "Raspbian"],
    nosql=["mongo db"],
    data_science=["machine learning", "sci-tek", "NLP"],
)

p.printSkillDetails()


"""
Id_gen = Id_Generator()
emp1 = Employee("Emp1", Id_gen)
emp1.Salary = 20000
emp1.D_id = 2

emp2 = Employee("Emp2", Id_gen)
emp2.Salary = 10000
emp2.D_id = 1

emp1.printDetails()
emp2.printDetails()
"""