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
