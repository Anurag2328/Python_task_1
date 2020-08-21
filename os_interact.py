import os

def menu():
  print("\n Hola Amigo, Welcome to the task menu \n\n");
  print(" Please Select an option below \n\n");
  print(" 0 : Exit \n\n");
  print(" 1 : Open File Manager \n\n");
  print(" 2 : Create a text file \n\n");
  print(" 3 : Open an existing file \n\n");
  print(" 4 : Remove an existing file \n\n");
  print(" 5 : Create a new directory \n\n");
  print(" 6 : Remove an existing directory \n\n");
  print(" 7 : Get current directory path \n\n");
  print(" 8 : Install an Application \n\n");
  print(" 9 : Uninstall an Application \n\n");
  print("10 - Shutdown an Application \n\n");  
  print("11 - Open new Terminal \n\n");
  print("12 : Goto Settings \n\n");
  print("13 : Open Google chrome \n\n");
  print("14 - Create a python file \n\n");
  print("15 - Get the list of python installed libraries \n\n");  
  print("16 - Install a python module \n\n");
  print("17 - Shutdown O.S \n\n");
  print("18 - Open calculator \n\n");
  print("19 - Open calander \n\n");
  print("20 - Open Firefox \n\n");
  
  choice()

def choice():
  choice = int(input("Enter your choice \n\n"));
  for choice in range(20):

    if choice == 0:
      os.system("exit()");

    elif choice == 1:
      os.system("xdg-open .");
    
    elif choice == 2:
      name = input("Enter the text file name don't enter extension(provide the complete path if the path is not {os.getcwd()}) \n\n");
      print("press crtl+d after done writing");
      os.system("cat > {name}.txt");

    elif choice == 3:
      name = input("Enter the file name (provide the complete path if the file is not in {os.getcwd()}) \n\n");
      os.system(xdg-open {name});
    
    elif choice == 4:
      name = input("Enter the file name (provide the complete path if the path is not {os.getcwd()}) \n\n");
      os.system("rm {name}");

    elif choice == 5:
      name = input("Enter the Directory name");
      address = input("provide the complete path , type 'this' if the path is {os.getcwd()}) \n\n");
      if address.lower() == 'this':
        os.system("mkdir {{name}}");
      else:
        os.system("cd {address} && mkdir {name}");

    elif choice == 6:
      name = input("Enter the Directory name");
      address = input("provide the complete path , type 'this' if the path is {os.getcwd()}) \n\n");
      if address.lower() == 'this':
        os.system("rmdir {{name}}");
      else:
        os.system("cd {address} && rmdir {name}");

    elif choice == 7:
      os.system("pwd");

    elif choice == 8:
      name = input("Application name \n\n");
      os.system("sudo dnf install {name}");

    elif choice == 9:
      name = input("Application name \n\n");
      os.system("sudo dnf remove -y {name}");

    elif choice == 10:
      name = input("Application name:  \n\n");
      os.system("pkill {name}");
    
    elif choice == 11:
      os.system("gnome-terminal");
 
    elif choice == 12:
      os.system('''gnome-terminal -x sh -c "gnome-control-center|less"''');

    elif choice == 13:
      os.system('''gnome-terminal -x sh -c "google-chrome|less"''');

    elif choice == 14:
      name = input("File Name without Extention \n \n");
      os.system("touch {name}.py");

    elif choice == 15:
      os.system("pip3 list");

    elif choice == 16:
      name = input("Enter the module name \n");
      os.system("pip install {name}");

    elif choice == 17:
      os.system("shutdown");

    elif choice == 18:
      os.system("calc");

    elif choice == 19:
      os.system("cal");
	
    elif choice == 20:
      os.system("firefox");

if __name__ == "__main__":
  menu()
  re = input("Do you want to execute another task press 'y' for yes or 'n' for no");
  while re.lower() == 'y':
    menu()
  print("Adios Amigo!");
