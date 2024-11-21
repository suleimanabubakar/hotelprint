import win32print
import win32api
currentprinter = win32print.GetDefaultPrinter()



def printPdf(file,type):
    pdftest = file

    # if type == 'main':
    #     printer = config.default1
    # else:
    #     printer = config.default2
    
    win32api.ShellExecute(0, "print", pdftest, None,  ".",  0)