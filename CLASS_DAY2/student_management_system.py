from student import Student

class StudentManagementSystem:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
        print("학생 정보가 추가되었습니다.")
        
    
    def search_student(self,student_id):
        for student in self.students:
            if student.student_id == student_id:
                print(student.get_info())
                return
        print("해당 학생을 찾을 수 없습니다.")
    
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print("학생 정보가 삭제되었습니다.")
                return
        print("해당 학생을 찾을 수 없습니다.")
    
    def update_student(self, student_id, name, age):
        for student in self.students:
            if student.student_id == student_id:
                student.name = name
                student.age = age
                print("학생 정보가 수정되었습니다.")
                return
        print("해당 학생을 찾을 수 없습니다.")
        
    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        print("해당 학생를 찾을 수 없습니다.")