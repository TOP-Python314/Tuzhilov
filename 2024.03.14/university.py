from typing import List, Tuple
from dataclasses import dataclass
from datetime import date

class EducationForm:
    INTRAMURAL = "Очный"
    EXTRAMURAL = "Заочный"
    REMOTE = "Удаленный"

class ContractForm:
    BUDGET = "Бюджет"
    COMPANY = "Целевой"
    PERSONAL = "Персональный"
    
class Degree:
    CANDIDATE = "Кандидат"
    DOCTOR = "Доктор"    
    
class ExamType:
    CHECK = "Зачет"
    DIFF_CHECK = "Дифзачет"
    EXAMEN = "Экзамен"
    PROJECT = "Проект"
    
@dataclass
class Contact:
    mobile:str 
    email:str 
    telegram: str 
    web: str 
    adress: str
    
class Person:
    def __init__(self, last_name: str, first_name: str, patr_name: str, birthdate: date, contact: Contact):
        self.last_name:str = last_name
        self.first_name: str = first_name 
        self.patr_name: str = patr_name
        self.birthdate: date = birthdate
        self.contact: Contact = contact
    
    def __repr__(self):
        return f'Person(last_name={self.last_name}, first_name={self.first_name}, patr_name={self.patr_name}, birthdate={self.birthdate}, contact{self.contact})'
        
class Employee(Person):
    def __init__(self, last_name, first_name, patr_name, birthdate, contact: Contact, position: str, income: float, joined: date):
        super().__init__(last_name, first_name, patr_name, birthdate, contact)
        self.position = position
        self.income = income
        self.joined = joined
        
class Student(Person):
    def __init__(self, id: str, form: EducationForm, contract: ContractForm, stipendia: float):
        super.__init__(last_name, first_name, patr_name, birthdate, contact)
        self.id = student_id
        self.form = form
        self.contract = contract
        self.stipendia = 0.0
        self.gradebook = gradebook(self.id)
    
    def set_stipendia(self, new_stipendia: float):
        self.stipendia = new_stipendia
        
    def __repr__(self):
         return f"Student(id={self.id}, last_name={self.last_name}, first_name={self.first_name}, form={self.form}, contract={self.contract})"
         
class Teacher(Employee):
    def __init__(self, last_name, first_name, patr_name, birthdate, contact: Contact, position: str, income: float, joined: date, previous_experience: int):
        super().__init__(last_name, first_name, patr_name, birthdate, contact, position, income, joined, previous_experience)
        self.previous_experience = previous_experience
        self.courses = []
        self.degree = None
        self.professor = False
        
    def total_experience(self) -> int:
        return previous_experience
    
    def make_examination(self):
        pass 
        
    def __repr__(self):
        return f'Teacher(previous_experience={self.previous_experience})'
        
class Administrator(Employee):
    def __init__(self, last_name, first_name, patr_name, birthdate, contact: Contact, position: str, income: float, joined: date, previous_experience: int, subordinates: list):
        super().__init__(contact, position, income)
        self.subordinates = []
    
@dataclass
class GradeRecord():
    name: str
    date: str
    type: ExamType
    semester: int 
    grade: int 
    scale: int 
    examiner: Teacher 
    
class Gradebook:
    def __init__(self, id: str):
        self.id = id
        self.records: List[GradeRecord] = []

    def average(self) -> float:
        if not self.records:
            return 0.0
        total = sum(record.grade for record in self.records)
        return total / len(self.records)

    def add_record(self, record: GradeRecord):
        self.records.append(record)

    def __repr__(self):
        return f"Gradebook(id={self.id}, records=[{', '.join(str(r) for r in self.records)}])"

@dataclass
class GradeRecord:
    name: str
    date: date
    type: ExamType
    semester: int
    grade: int
    scale: int
    examiner: Teacher

    def __repr__(self):
        return f"GradeRecord(name={self.name}, date={self.date}, type={self.type}, semester={self.semester}, grade={self.grade}, scale={self.scale}, examiner={self.examiner.first_name} {self.examiner.last_name})"

class OrganizationLevel:
    def __init__(self, title: str, description: str, head: Administrator, contact: Contact):
        self.title = title
        self.description = description
        self.head = head  
        self.contact = contact
        self.staff: List[Administrator] = []  

    def __repr__(self):
        return f"OrganizationLevel(title={self.title}, description={self.description}, head={self.head.first_name} {self.head.last_name}, staff_count={len(self.staff)})"

class University(OrganizationLevel):
    def __init__(self, title: str, description: str, head: Administrator, contact: Contact):
        super().__init__(title, description, head, contact)
        self.hr = HR()
        self.auditoria: List[Auditorium] = []  

    def add_auditorium(self, auditorium: 'Auditorium'):
        self.auditoria.append(auditorium)

    def __repr__(self):
        return f"University(title={self.title}, auditoria_count={len(self.auditoria)}, hr={self.hr})"

class HR:
    def hire(self, employee: Employee):
        pass

    def fire(self, employee: Employee):
        pass

    def __repr__(self):
        return "HR()"

class Auditorium:
    def __init__(self, number: str, description: str, seats: int, building: str):
        self.number = number
        self.description = description
        self.seats = seats
        self.building = building

    def __repr__(self):
        return f"Auditorium(number={self.number}, description={self.description}, seats={self.seats}, building={self.building})"

class Faculty(OrganizationLevel):
    def __init__(self, title: str, description: str, head: Administrator, contact: Contact):
        super().__init__(title, description, head, contact)
        self.departments: List['Department'] = []  
        
    def add_department(self, department: 'Department'):
        self.departments.append(department)

    def __repr__(self):
        return f"Faculty(title={self.title}, departments_count={len(self.departments)})"

class Department(OrganizationLevel):
    def __init__(self, title: str, description: str, head: Administrator, contact: Contact):
        super().__init__(title, description, head, contact)
        self.teachers: List[Teacher] = []  
        self.groups: List['Group'] = []  

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def add_group(self, group: 'Group'):
        self.groups.append(group)

    def __repr__(self):
        return f"Department(title={self.title}, teachers_count={len(self.teachers)}, groups_count={len(self.groups)})"

class Group:
    def __init__(self, number: str, semester: int, chief: Student, curator: Teacher):
        self.number = number
        self.sem
    