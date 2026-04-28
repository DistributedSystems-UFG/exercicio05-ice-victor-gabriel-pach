module Demo
{
    interface Printer
    {
        void printString(string s);
        string echoString(string s);
        int countChars(string s);
    }

    interface Calculator
    {
        int add(int a, int b);
        int multiply(int a, int b);
        int subtract(int a, int b);
    }
}