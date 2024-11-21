import win32print
import win32api
currentprinter = win32print.GetDefaultPrinter()

print(currentprinter)


win32api.ShellExecute(0, "print", "C:\hotelpdf\main4.pdf", None,  ".",  0)