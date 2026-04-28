import sys, Ice
import Demo

with Ice.initialize(sys.argv) as communicator:

    # --- Printer object ---
    base = communicator.stringToProxy("SimplePrinter:tcp -h <SERVER_PRIVATE_IP> -p 11000")
    printer = Demo.PrinterPrx.checkedCast(base)
    if not printer:
        raise RuntimeError("Invalid proxy for Printer")

    printer.printString("Hello from the client!")
    echo = printer.echoString("Echo this string")
    print("Echo reply:", echo)
    n = printer.countChars("hello world")
    print("countChars:", n)

    # --- Calculator object (new server object) ---
    base2 = communicator.stringToProxy("SimpleCalc:tcp -h <SERVER_PRIVATE_IP> -p 11000")
    calc = Demo.CalculatorPrx.checkedCast(base2)
    if not calc:
        raise RuntimeError("Invalid proxy for Calculator")

    print("10 + 3 =", calc.add(10, 3))
    print("10 x 3 =", calc.multiply(10, 3))
    print("10 - 3 =", calc.subtract(10, 3))