# Class Warehouse to Store Widget
class Warehouse:
    def __init__(self, quantity, cost, company):
        self.quantity = quantity
        self.cost = cost
        self.company = company
        self.next = None


# Class Shipment Main Class
class Shipment:
    def __init__(self):
        self.first_widget = None
        self.last_widget = None

    # Method Menu to Display Menu Driven
    def menu(self):
        print()
        print('-------------------- Widget Menu ------------------------')
        print('[1] - Received Shipment')
        print('[2] - Sent Shipment')
        print('[3] - Show Warehouse Widget')
        print('[0] - Exit')
        option = int(input('Enter Choices: '))
        print('---------------------------------------------------------')

        if option == 1:
            print()
            print('---------------------------------------------------------')
            quantity = int(input('Enter Widget Quantity: '))
            cost = int(input('Enter Widget Cost: '))
            company = input('Enter Company Name: ')
            print('Widget Successfully Received!')
            print('---------------------------------------------------------')
            print()
            Shipment.shipment_received(self, quantity, cost, company)
            w.menu()

        elif option == 2:
            print()
            print('---------------------------------------------------------')
            sent_company = input('Enter Company Name to Send: ')
            print('---------------------------------------------------------')
            Shipment.shipment_sent(self, sent_company)
            w.menu()

        elif option == 3:
            Shipment.warehouse_widget(self)
            w.menu()

        elif option == 0:
            exit()

        else:
            print()
            print('-------------------- Widget Menu ------------------------')
            print('Invalid Option!')
            print('---------------------------------------------------------')
            w.menu()

    # Method Shipment Receive to Store Widget in Warehouse
    def shipment_received(self, quantity, cost, company):
        received_shipment = Warehouse(quantity, cost, company)

        if self.first_widget:
            received_shipment.next = self.first_widget
            self.first_widget = received_shipment
        else:
            self.first_widget = self.last_widget = received_shipment

    # Method Shipment Sent to Ship the old Widget in Warehouse
    def shipment_sent(self, sent_company):
        if self.first_widget:
            current = self.first_widget
            pre_current = current

            while current.next:
                pre_current = current
                current = current.next

            pre_current.next = None
            self.last_widget = pre_current

            total_cost = current.quantity * (current.cost / 2 + current.cost)
            print()
            print('--------------------- Widget Shipment -------------------')
            print('Sent Company to: ', sent_company)
            print('Widget Quantity: ', current.quantity,
                  '\nWidget Cost: ', current.cost)
            print('Total Cost Billing: ', total_cost)
            print('Shipment Sent Successfully! ')
            print('---------------------------------------------------------')

            if current == self.first_widget:
                self.first_widget = None
                return

        else:
            print()
            print('---------------------------------------------------------')
            print('Warehouse Widget is Empty!')
            print('---------------------------------------------------------')

    # Peek Widget Data in Warehouse
    def warehouse_widget(self):
        current = self.first_widget
        if current:
            print()
            print('----------------------------------------------------- Widget Warehouse -----------------------------'
                  '-------------------------')
            print('Widget Quantity \t\t Widget Cost\t\t Received From \t\t\t Total Cost \t\t Shipout Billing'
                  '\t Expected Profit')
            while current:
                cost = current.quantity * current.cost
                total_cost = current.quantity * (current.cost / 2 + current.cost)
                total_profit = total_cost - cost
                print(current.quantity, '\t\t\t\t\t', current.cost, ' \t\t\t\t', current.company, '  \t\t\t',
                      '\t', cost, '\t\t\t\t', total_cost, '\t\t\t', total_profit)
                current = current.next
            print('----------------------------------------------------------------------------------------------------'
                  '-------------------------')

        else:
            print()
            print('---------------------------------------------------------')
            print('Warehouse Widget is Empty!')
            print('---------------------------------------------------------')


# Invoke Class and Method and Assign Values to Parameters
w = Shipment()
w.shipment_received(500,  8,   'Frotees')
w.shipment_received(400,  13,  'Piattos')
w.shipment_received(250,  13,  'Nova')
w.shipment_received(300,  7,   'Cheezy')
w.shipment_received(150,  6,   'Patata')
w.shipment_received(600,  14,  'Vcut')
w.shipment_received(350,  8,   'Martys')
w.shipment_received(150,  6,   'Rebisco')
w.shipment_received(900,  10,  'Lala')
w.shipment_received(250,  11,  'Chippy')
w.shipment_received(700,  10,  'Clover')
w.shipment_received(100,  8,   'Hansel')
w.shipment_received(500,  7,   'Fita')
w.shipment_received(1000, 1,   'Happy')
w.shipment_received(650,  7,   'Bingo')
w.shipment_received(100,  15,  'Wafello')
w.shipment_received(350,  7,   'Combi')
w.shipment_received(350,  30,  'Nutella')
w.shipment_received(350,  6,   'Bravo')
w.shipment_received(350,  14,  'Pillows')
w.shipment_received(350,  12,  'Tiger')
w.menu()
