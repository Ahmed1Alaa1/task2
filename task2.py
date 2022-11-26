class Medical_Robot:
    
#----------------------------------------------
    @staticmethod
    def defin():
        print ('I will Speak About My Universty In This Task')
    def _init_(self,subject,doctors,student_num,sallary,sucsses):
        self.subjects=subject
        self.doctors=doctors
        self.student_num=student_num
        self.sallary=sallary
        self.sucseed=sucsses
        #self.a=a
    def know_the_subject(self):
        return f'{self.subjects}'

    def know_the_doctor(self):
        return f'{self.doctors}'    

    def calce_The_Student_num(self):
        return f'{self.student_num}'
    def salary(self):
        return f'{self.sallary}'    
    def sucsessful(self,a,sucsses):
        self.a=a
       #self.sucseed=sucsses
        if a>=sucsses:
            print ('A+')

        elif a<80 and a<=50:
            print ('B')
        else:
            print ('C')
#-----------------------------------------
class Robotics(Medical Robot):
    def _init_(self,subject,doctors,student_num,sallary,sucsses):
        Medical_Robot._init_(self,subject,doctors,student_num,sallary,sucsses)
  
class Bio(Medical Robot):
    def _init_(self, subject, doctors, student_num,sallary,sucsses):
        super()._init_(subject, doctors, student_num,sallary,sucsses)
   
#----------------------------------------------
machine=Medical Robot('Data Structures','DR:nora',88,550,98)
print (machine.know_the_subject())
print(machine.know_the_doctor())
print(machine.calce_The_Student_num())
print(machine.salary())
print(machine.sucsessful(100,90))
#----------------------------------------------
rob=Robotics('data base','DR:ahmed',18,660,80)
print(rob.know_the_subject())
print(rob.know_the_doctor())
print(rob.calce_The_Student_num())
print(rob.salary())
print(rob.sucsessful(70,70))
#----------------------------------------------
bio=Bio('bioinformatcs','DR:zainab',26,800,23)
print(bio.know_the_subject())
print(bio.know_the_doctor())
print(bio.calce_The_Student_num())
print (bio.salary())
print (bio.sucsessful(70,90))