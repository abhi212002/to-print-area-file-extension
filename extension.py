filename=input("Input the Filename : ")
a=filename.split(".")
if a[-1]=='py':
   print("The extension of the file is :" +"'python'")
else
   print("The extension of the file is :",repr(a[-1]))
