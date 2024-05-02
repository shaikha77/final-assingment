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

    # Getters
    def getName(self):
        return self.name

    def getEmployeeID(self):
        return self.employeeID

    def getDepartment(self):
        return self.department

    def getJobTitle(self):
        return self.jobTitle

    def getBasicSalary(self):
        return self.basicSalary

    def getAge(self):
        return self.age

    def getDateOfBirth(self):
        return self.dateOfBirth

    def getPassportDetails(self):
        return self.passportDetails

    # Setters
    def setName(self, name):
        self.name = name

    def setEmployeeID(self, employeeID):
        self.employeeID = employeeID

    def setDepartment(self, department):
        self.department = department

    def setJobTitle(self, jobTitle):
        self.jobTitle = jobTitle

    def setBasicSalary(self, basicSalary):
        self.basicSalary = basicSalary

    def setAge(self, age):
        self.age = age

    def setDateOfBirth(self, dateOfBirth):
        self.dateOfBirth = dateOfBirth

    def setPassportDetails(self, passportDetails):
        self.passportDetails = passportDetails



class Event:
    """Represents an event organized by the company."""
    def __init__(self, eventID, type, theme, date, venueAddress, clientID):
        self.eventID = eventID
        self.type = type
        self.theme = theme
        self.date = date
        self.venueAddress = venueAddress
        self.clientID = clientID

    # Getters
    def getEventID(self):
        return self.eventID

    def getType(self):
        return self.type

    def getTheme(self):
        return self.theme

    def getDate(self):
        return self.date

    def getVenueAddress(self):
        return self.venueAddress

    def getClientID(self):
        return self.clientID

    # Setters
    def setEventID(self, eventID):
        self.eventID = eventID

    def setType(self, type):
        self.type = type

    def setTheme(self, theme):
        self.theme = theme

    def setDate(self, date):
        self.date = date

    def setVenueAddress(self, venueAddress):
        self.venueAddress = venueAddress

    def setClientID(self, clientID):
        self.clientID = clientID

class Client:
    """Represents a client of the company."""
    def __init__(self, clientID, name, address, contactDetails, budget):
        self.clientID = clientID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails
        self.budget = budget

    # Getters
    def getClientID(self):
        return self.clientID

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getContactDetails(self):
        return self.contactDetails

    def getBudget(self):
        return self.budget

    # Setters
    def setClientID(self, clientID):
        self.clientID = clientID

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setContactDetails(self, contactDetails):
        self.contactDetails = contactDetails

    def setBudget(self, budget):
        self.budget = budget


class Guest:
    """Represents a guest attending an event."""
    def __init__(self, guestID, name, address, contactDetails):
        self.guestID = guestID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

    # Getters
    def getGuestID(self):
        return self.guestID

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getContactDetails(self):
        return self.contactDetails

    # Setters
    def setGuestID(self, guestID):
        self.guestID = guestID

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setContactDetails(self, contactDetails):
        self.contactDetails = contactDetails


class Supplier:
    """Represents a supplier for the company."""
    def __init__(self, supplierID, name, address, contactDetails):
        self.supplierID = supplierID
        self.name = name
        self.address = address
        self.contactDetails = contactDetails

    # Getters
    def getSupplierID(self):
        return self.supplierID

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getContactDetails(self):
        return self.contactDetails

    # Setters
    def setSupplierID(self, supplierID):
        self.supplierID = supplierID

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setContactDetails(self, contactDetails):
        self.contactDetails = contactDetails


class Venue:
    """Represents a venue for events."""
    def __init__(self, venueID, name, address, contact, minGuests, maxGuests):
        self.venueID = venueID
        self.name = name
        self.address = address
        self.contact = contact
        self.minGuests = minGuests
        self.maxGuests = maxGuests

    # Getters
    def getVenueID(self):
        return self.venueID

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getContact(self):
        return self.contact

    def getMinGuests(self):
        return self.minGuests

    def getMaxGuests(self):
        return self.maxGuests

    # Setters
    def setVenueID(self, venueID):
        self.venueID = venueID

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setContact(self, contact):
        self.contact = contact

    def setMinGuests(self, minGuests):
        self.minGuests = minGuests

    def setMaxGuests(self, maxGuests):
        self.maxGuests = maxGuests


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

    # Getters
    def getCatererID(self):
        return self.catererID

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getContactDetails(self):
        return self.contactDetails

    def getMenu(self):
        return self.menu

    def getMinGuests(self):
        return self.minGuests

    def getMaxGuests(self):
        return self.maxGuests

    # Setters
    def setCatererID(self, catererID):
        self.catererID = catererID

    def setName(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setContactDetails(self, contactDetails):
        self.contactDetails = contactDetails

    def setMenu(self, menu):
        self.menu = menu

    def setMinGuests(self, minGuests):
        self.minGuests = minGuests

    def setMaxGuests(self, maxGuests):
        self.maxGuests = maxGuests


