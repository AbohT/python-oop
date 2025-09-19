'''
class Cohort3Web2:
    pass
std_1 = Cohort3Web2()
std_2 = Cohort3Web2()
std_3 = Cohort3Web2()


print(std_1)
print(std_2)

std_1.first = 'ThankGod'
std_1.last = 'Audu'
std_1.age = 22
std_1.isMarried = True

std_2.firstname = 'Joe'
std_2.lastname = 'Plangshak'
std_2.age = 32
std_2.isMarried = False


std_3.firstname = 'Mary'
std_3.lastname = 'Anum'
std_3.age = 24
std_3.isMarried = True

print(std_1.isMarried)
print(std_2.isMarried)
print(std_3.isMarried)
'''

# Using Constructors
'''
class Cohort3Web2:
    def __init__(self, firstname, lastname, age, isMarried):
      #The constructor or initialize method of a class
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.isMarried = isMarried
    
std_1 = Cohort3Web2('Joe', 'Plangshak', 32, False)
#his passes std_1 as self (first instance), then the respective values of firstname, lastname, age, etc as args in their respcetive order thereby keeping code DRY and less lines of code
std_2 = Cohort3Web2('Mary', 'Anum', 24, True)

print(std_1.age)
print(std_2.age)
# To create a fullname output  for each student would be manual example
print('{},{}'.format(std_1.firstname, std_1.lastname))
print(f'{std_1.firstname} {std_1.lastname}')
'''
#To simplify this we use a mrthod called fullname within the class.'''
class Cohort3Web2:
    def __init__(self, firstname, lastname, age, isMarried):
	    #The constructor or initialize method of a class'''
      self.firstname = firstname
      self.lastname = lastname
      self.age = age
      self.isMarried = isMarried
    
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)
        #We use self for each instance of the class Cohort3Web2'''
        
std_1 = Cohort3Web2('Joe', 'Plangshak', 32, False)
std_2 = Cohort3Web2('Mary', 'Anum', 24, True)
print(std_1.fullname())
#std_1.fullname()
print(Cohort3Web2.fullname(std_1))
#The two lines above do the same thing however, the first is an instance of the class and takes no argument in parenthesis, but the second is the class followed by the methods(functions). Methods of a class always requires an instance (self) while attributes do not
