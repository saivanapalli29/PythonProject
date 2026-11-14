class Laptop:
    def charge(self):
        print("This is a laptop")

class Mobile:
    def charge(self):
        print("This is a mobile")

class Tablet:
    def charge(self):
        print("This is a tablet")

def show_device(device):
    device.charge()

laptop = Laptop()
mobile = Mobile()
tablet = Tablet()

show_device(laptop)
show_device(mobile)
show_device(tablet)