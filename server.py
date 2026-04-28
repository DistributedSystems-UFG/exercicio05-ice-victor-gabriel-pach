import sys, Ice
import Demo

class PrinterI(Demo.Printer):
    def printString(self, s, current=None):
        print("printString:", s)

    def echoString(self, s, current=None):
        print("echoString called with:", s)
        return s

    def countChars(self, s, current=None):
        print("countChars called with:", s)
        return len(s)

class CalculatorI(Demo.Calculator):
    def add(self, a, b, current=None):
        return a + b

    def multiply(self, a, b, current=None):
        return a * b

    def subtract(self, a, b, current=None):
        return a - b

communicator = Ice.initialize(sys.argv)
adapter = communicator.createObjectAdapterWithEndpoints("SimpleAdapter", "default -p 11000")

adapter.add(PrinterI(), communicator.stringToIdentity("SimplePrinter"))
adapter.add(CalculatorI(), communicator.stringToIdentity("SimpleCalc"))

adapter.activate()
print("Server running on port 11000...")
communicator.waitForShutdown()