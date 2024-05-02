from datetime import date

class Employee:
    """Represents an employee."""

    def __init__(self, name, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails):
        self.name = name
        self.employeeID = employeeID
        self.department = department
        self.jobTitle = jobTitle
        self.basicSalary = basicSalary
        self.age = age
        self.dateOfBirth = dateOfBirth
        self.passportDetails = passportDetails

# Test Employee class
employee = Employee("John Doe", "12345", "HR", "Manager", 50000.0, 35, date(1989, 5, 15), "AB123456")
print("Employee name:", employee.name)
print("Employee ID:", employee.employeeID)
print("Employee department:", employee.department)
print("Employee job title:", employee.jobTitle)
print("Employee basic salary:", employee.basicSalary)
print("Employee age:", employee.age)
print("Employee date of birth:", employee.dateOfBirth)
print("Employee passport details:", employee.passportDetails)
print()


class Event:
    """Represents an event organized by the company."""

    def __init__(self, eventID, type, theme, date, venueAddress, clientID):
        self.eventID = eventID
        self.type = type
        self.theme = theme
        self.date = date
        self.venueAddress = venueAddress
        self.clientID = clientID

# Test Event class
event = Event("E001", "Wedding", "Garden", date(2024, 6, 15), "123 Main Street", "C001")
print("Event ID:", event.eventID)
print("Event type:", event.type)
print("Event theme:", event.theme)
print("Event date:", event.date)
print("Event venue address:", event.venueAddress)
print("Event client ID:", event.clientID)
print()


class Client:
    """Represents a client of the company."""

    def __init__(self, clientID, name, address, contactDetails, budget):
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

# Test Client class
client = Client("C001", "John Smith", "456 Elm Street", "123-456-7890", 10000.0)
print("Client ID:", client.clientID)
print("Client name:", client.name)
print("Client address:", client.address)
print("Client contact details:", client.contactDetails)
print("Client budget:", client.budget)
print()


class Guest:
    """Represents a guest attending an event."""

    def __init__(self, guestID, name, address, contactDetails):
        self.guestID = guestID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

# Test Guest class
guest = Guest("G001", "Jane Doe", "789 Oak Street", "987-654-3210")
print("Guest ID:", guest.guestID)
print("Guest name:", guest.name)
print("Guest address:", guest.address)
print("Guest contact details:", guest.contactDetails)
print()


class Supplier:
    """Represents a supplier for the company."""

    def __init__(self, supplierID, name, address, contactDetails):
        self.supplierID = supplierID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

# Test Supplier class
supplier = Supplier("S001", "ABC Catering", "123 Maple Avenue", "456-789-0123")
print("Supplier ID:", supplier.supplierID)
print("Supplier name:", supplier.name)
print("Supplier address:", supplier.address)
print("Supplier contact details:", supplier.contactDetails)
print()


class Venue:
    """Represents a venue for events."""

    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        self.venueID = venueID
        self.name = name
        self.address = address
        self.contact = contact
        self.minGuests = minGuests
        self.maxGuests = maxGuests

# Test Venue class
venue = Venue("V001", "Grand Hall", "1000 Cherry Lane", "555-123-4567", 50, 200)
print("Venue ID:", venue.venueID)
print("Venue name:", venue.name)
print("Venue address:", venue.address)
print("Venue contact:", venue.contact)
print("Venue minimum guests:", venue.minGuests)
print("Venue maximum guests:", venue.maxGuests)
print()


class Caterer:
    """Represents a caterer for events."""

    def __init__(self, catererID, name, address, contactDetails, menu, minGuests, maxGuests):
        self.catererID = catererID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.menu = menu
        self.minGuests = minGuests
        self.maxGuests = maxGuests

# Test Caterer class
caterer = Caterer("C001", "XYZ Catering", "789 Pine Street", "123-456-7890", "Buffet", 20, 150)
print("Caterer ID:", caterer.catererID)
print("Caterer name:", caterer.name)
print("Caterer address:", caterer.address)
print("Caterer contact details:", caterer.contactDetails)
print("Caterer menu:", caterer.menu)
print("Caterer minimum guests:", caterer.minGuests)
print("Caterer maximum guests:", caterer.maxGuests)

