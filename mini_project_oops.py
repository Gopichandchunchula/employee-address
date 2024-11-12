class Employee:

    def __init__(self,name,IDcard,domine,company):
        self.name = name
        self.IDcard = IDcard
        self.domine = domine
        self.company = company

    def info(self):
        print('employee name:',self.name)
        print('employee IDcard:',self.IDcard)
        print('employee domaine:',self.domine)
        print('employee company:',self.company)

list_of_Employee=[]
while True:
    name = input('Enter a employee name:')
    IDcard = int(input('Enter a employee card:'))
    domine = input('Enter a employee domine:')
    company = input('Enter a employee company:')
    e = Employee(name,IDcard,domine,company)
    list_of_Employee.append(e)
    print('Employee added successfully')
    option = input('Do you want to add Employees[YES|NO]:')
    if option.lower() == 'no':
        break
print('All employess information..')
for Employee in list_of_Employee:
    Employee.info()
    print()

#output:
'''
Enter a employee name:raju
Enter a employee card:123
Enter a employee domine:python
Enter a employee company:Accenture
Employee added successfully
Do you want to add Employees[YES|NO]:yes
Enter a employee name:Gopi
Enter a employee card:345
Enter a employee domine:BAckend
Enter a employee company:LTI
Employee added successfully
Do you want to add Employees[YES|NO]:yes
Enter a employee name:Hareesh
Enter a employee card:456 
Enter a employee domine:java
Enter a employee company:Techmahindra
Employee added successfully
Do you want to add Employees[YES|NO]:yes
Enter a employee name:vamsi
Enter a employee card:345
Enter a employee domine:frontend
Enter a employee company:TATA
Employee added successfully
Do you want to add Employees[YES|NO]:no
All employess information..
employee name: raju
employee IDcard: 123
employee domaine: python
employee company: Accenture

employee name: Gopi
employee IDcard: 345
employee domaine: BAckend
employee company: LTI

employee name: Hareesh
employee IDcard: 456
employee domaine: java
employee company: Techmahindra

employee name: vamsi
employee IDcard: 345
employee domaine: frontend
employee company: TATA 
'''