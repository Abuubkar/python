class Bo:
    count = 0

    def __init__(self):
        #print("constructor called")
        self.watt = 0
        self.unit = 0
        self._bill = 0

        Bo.count += 1
        self._id = Bo.count

    def calculate_bill(self):
        #print("calculating bill")
        self._bill = (self.watt * 24 * 30) / 1000 * self.unit

    def display(self):
        print("ID: " + str(self.id))
        print("Watt: " + str(self.watt))
        print("Unit: " + str(self.unit))
        print("Bill: " + str(self.bill))

    @property
    def watt(self):
        #print("watt getter called")
        return self._watt

    # def watt(self, watt): DOES NOT WORK
    @watt.setter
    def watt(self, watt):
        #print("watt setter called")
        if watt >= 0:
            self._watt = watt

    @property
    def unit(self):
        #print("unit getter called")
        return self._unit

    @unit.setter
    def unit(self, unit):
        #print("unit getter called")
        if unit >= 0:
            self._unit = unit

    @property
    def bill(self):
        #print("bill getter called")
        return self._bill

    @property
    def id(self):
        #print("id getter called")
        return self._id
