class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"<Device: {self.name!r} ({self.connected_by}) >"

    def disconnect(self):
        self.connected = False
        print("Disconnect")

    def connect(self):
        self.connected = True
        print("Connected")


class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity
        self.remaining_pages = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_pages} pages remaining)"

    def print(self, pages):
        if self.connected:
            print(f"Printing {pages} pages.")
            self.remaining_pages -= pages
        else:
            print("Your printer is not connected!")


printer = Device("Printer", "USB")
print(printer)
printer.disconnect()

printer2 = Printer("Printer2", "Ethernet", 1000)
print(printer2)
printer2.disconnect()
printer2.print(50)
printer2.connect()
printer2.print(50)
print(printer2)
printer2.print(1900)
print(printer2)
