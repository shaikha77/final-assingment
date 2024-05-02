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

