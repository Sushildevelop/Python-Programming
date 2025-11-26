#Exception handling
# file=open("sample.txt","w")
# try:
#     file.write("Writing some data to the file.")
#     #intentionally raising an exception
#     result=10/0
# except ZeroDivisionError as zde:
#     print(f"Error: Cannot divide by zero. Details: {zde}")
# finally:
#     file.close()
#     print("File closed successfully.")
    
with open("sample.txt","w") as file:
    file.write("Writing some data to the file using with statement.")
    
    

