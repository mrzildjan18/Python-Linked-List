# Class Template to Store Data
class StoreData:
    def __init__(self, id, name, address, salary):
        self.id = id
        self.name = name
        self.address = address
        self.salary = salary
        self.next = None
        self.prev = None


# Class Employee Main Class
class Employee:
    def __init__(self):
        self.info_head = None
        self.info_tail = None

    # Method Menu to Display Menu Driven
    def menu(self):
        print()
        print('------------------- Employee Menu -----------------------')
        print('[1] - Add Employee')
        print('[2] - Search Employee (Based on name)')
        print('[3] - Display All Employee')
        print('[4] - Get The Total Number of Employees')
        print('[5] - Get the Total Average of Salary')
        print('[6] - Delete an Employee based on the ID')
        print('[7] - Display the latest')
        print('[0] - Exit')
        option = int(input('Enter Choices: '))
        print('---------------------------------------------------------')

        if option == 1:
            print()
            print('---------------------------------------------------------')
            id = int(input('Enter ID Number: '))
            name = input('Enter Name: ')
            address = input('Enter Address: ')
            salary = int(input('Enter Salary Amount: '))
            print('---------------------------------------------------------')
            print()
            Employee.add_employee(self, id, name, address, salary)
            e.menu()

        elif option == 2:
            print()
            print('---------------------------------------------------------')
            search_name = input('Enter Name to Search: ')
            print('---------------------------------------------------------')
            print()
            Employee.search_employee(self, search_name)
            e.menu()

        elif option == 3:
            Employee.display_all(self)
            e.menu()

        elif option == 4:
            Employee.get_total_employees(self)
            e.menu()

        elif option == 5:
            Employee.get_average_salary(self)
            e.menu()

        elif option == 6:
            print()
            print('---------------------------------------------------------')
            search_id = int(input('Enter Employee ID Number: '))
            print('---------------------------------------------------------')
            print()
            Employee.delete_employee(self, search_id)
            e.menu()

        elif option == 7:
            Employee.display_latest(self)
            e.menu()

        elif option == 0:
            exit()

        else:
            print()
            print('------------------- Employee Menu -----------------------')
            print('Invalid Option!')
            print('---------------------------------------------------------')
            e.menu()

    # Method to Add Employees in the Data
    def add_employee(self, id, name, address, salary):
        add_employee = StoreData(id, name, address, salary)

        if self.info_head:
            add_employee.next = self.info_head
            self.info_head.prev = add_employee
            self.info_head = add_employee
        else:
            self.info_head = self.info_tail = add_employee

    # Method to Search Employee Name in the Data
    def search_employee(self, search_name):
        found = False
        if self.info_head:
            current = self.info_head

            while current:
                if current.name == search_name:
                    print('----------------- Employees Latest Data -----------------')
                    print('ID \t\t Name \t\t\t\t Address \t\t Salary')
                    print(current.id, '\t', current.name, '\t', current.address, '\t\t', current.salary)
                    print('---------------------------------------------------------')
                    found = True

                current = current.next

            if not found:
                print('-------------------- Employees Data ---------------------')
                print('Employee Name Not Found!')
                print('---------------------------------------------------------')

        else:
            print('---------------------------------------------------------')
            print('No Data Found!')
            print('---------------------------------------------------------')

    # Method to Show all the Employee in the Data
    def display_all(self):
        if self.info_head:
            current = self.info_head

            print()
            print('-------------------- Employees Data ---------------------')
            print('ID \t\t Name \t\t\t\t Address \t\t Salary')
            while current.next:
                current = current.next
            while current:
                print(current.id, '\t', current.name, '    \t', current.address, '\t\t', current.salary)
                current = current.prev
            print('---------------------------------------------------------')

        else:
            print('---------------------------------------------------------')
            print('No Data Found!')
            print('---------------------------------------------------------')

    # Method to get the Total Number of Employees
    def get_total_employees(self):
        if self.info_head:
            current = self.info_head

            total_employees = 0
            print()
            print('-------------------- Total Employees --------------------')
            print('ID \t\t Name \t\t\t\t Address \t\t Salary')
            while current.next:
                current = current.next
            while current:
                print(current.id, '\t', current.name, '\t', current.address, '\t\t', current.salary)
                total_employees = total_employees + 1
                current = current.prev

            print('Total Employees: ', total_employees)
            print('---------------------------------------------------------')

        else:
            print('---------------------------------------------------------')
            print('No Data Found!')
            print('---------------------------------------------------------')

    # Method to get the Average Salary in all Employees Data
    def get_average_salary(self):
        if self.info_head:
            current = self.info_head

            average_salary = 0
            total_employees = 0
            while current:
                average_salary = average_salary + current.salary
                total_employees = total_employees + 1
                current = current.next

            total_average = average_salary / total_employees

            print()
            print('-------------- Average Salary of Employees --------------')
            print('Total Average: %.2f' % total_average)
            print('---------------------------------------------------------')

        else:
            print('---------------------------------------------------------')
            print('No Data Found!')
            print('---------------------------------------------------------')

    # Method to Remove or Delete the Employees in Data
    def delete_employee(self, search_id):
        found = False
        if self.info_head:
            current = self.info_head

            if current.id == search_id:
                self.info_head = self.info_head.next
                self.info_head.prev = None
                found = True
                print('-------------------- Employees Data ---------------------')
                print('ID: ', current.id, '\nName: ', current.name)
                print('Employee Successfully Deleted!')
                print('---------------------------------------------------------')

            elif self.info_tail.id == search_id:
                print('-------------------- Employees Data ---------------------')
                print('ID: ', self.info_tail.id, '\nName: ', self.info_tail.name)
                self.info_tail = self.info_tail.prev
                self.info_tail.next = None
                found = True
                print('Employee Successfully Deleted!')
                print('---------------------------------------------------------')

            else:
                while current.next:
                    if current.id == search_id:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        found = True
                        print('-------------------- Employees Data ---------------------')
                        print('ID: ', current.id, '\nName: ', current.name)
                        print('Employee Successfully Deleted!')
                        print('---------------------------------------------------------')

                    current = current.next

            if not found:
                print('-------------------- Employees Data ---------------------')
                print('Employee ID Not Found!')
                print('---------------------------------------------------------')

        else:
            print('---------------------------------------------------------')
            print('No Data Found!')
            print('---------------------------------------------------------')

    # Method to Display only the Latest Employee in the Data
    def display_latest(self):
        if self.info_head:
            current = self.info_head
            print()
            print('----------------- Employees Latest Data -----------------')
            print('ID \t\t Name \t\t\t\t Address \t\t Salary')
            while current:
                if current.next:
                    print(current.id, '\t', current.name, '\t', current.address, '\t\t', current.salary)
                    break

                current = current.next
            print('---------------------------------------------------------')

        else:
            print('---------------------------------------------------------')
            print('No Data Found!')
            print('---------------------------------------------------------')


# Invoke Class and Method and Assign Values to Parameters
e = Employee()
e.add_employee(1000, 'Zil Luvindino',  'V-Rama',    93234)
e.add_employee(1001, 'John Decinan',   'Mambaling', 32943)
e.add_employee(1002, 'Jam Mitucua',    'Lapu-Lapu', 43823)
e.add_employee(1003, 'Maricris Cena',  'Bantayan',  10383)
e.add_employee(1004, 'KJ Catubig',     'Lapu-Lapu', 54323)
e.add_employee(1005, 'Khyle Rafols',   'Talisay',   23443)
e.add_employee(1006, 'Rey Alfante',    'Lapu-Lapu', 53423)
e.add_employee(1007, 'Mary Navares',   'Carcar',    23543)
e.add_employee(1008, 'Jim Laroco',     'Lapu-Lapu', 54325)
e.add_employee(1009, 'Jolex Guba',     'Lapu-Lapu', 96543)
e.add_employee(1010, 'Edie Basay',     'Lapu-Lapu', 12434)
e.add_employee(1011, 'Oneal Torres',   'Mandaue',   54325)
e.add_employee(1012, 'Wenjoy Ybas',    'Talisay',   76533)
e.add_employee(1013, 'John Berdin',    'Lapu-Lapu', 65466)
e.add_employee(1014, 'James Boroy',    'Lapu-Lapu', 54353)
e.add_employee(1015, 'Clyde Gabisan',  'Talisay',   75675)
e.add_employee(1016, 'Paul Chris',     'Lacion',    53465)
e.add_employee(1017, 'Gianni Dylan',   'Liloan',    34543)
e.add_employee(1018, 'Ven Manatad',    'Mandaue',   76654)
e.add_employee(1019, 'Jay Natividad',  'Kamputhaw', 21325)
e.add_employee(1020, 'Denise Erida',   'Carreta',   83432)
e.menu()
