import os

CRED = '\033[91m'
CGREEN = '\u001b[32m'
CEND = '\033[0m'
CYELLOW = '\u001b[33m'

def banner():
    print(CGREEN+''' ____    _____    ____   ____   __   __  ____    _____    ___    ____  
 |  _ \  | ____|  / ___| |  _ \  \ \ / / |  _ \  |_   _|  / _ \  |  _ \ 
 | | | | |  _|   | |     | |_) |  \ V /  | |_) |   | |   | | | | | |_) |
 | |_| | | |___  | |___  |  _ <    | |   |  __/    | |   | |_| | |  _ < 
 |____/  |_____|  \____| |_| \_\   |_|   |_|       |_|    \___/  |_| \_\ 
                                                                        
   Created by N!gh+m@r3             version 1.0.0                      '''+CEND)



def fileexitsornot(path):
    return os.path.exists(path)

def main():
    os.system('cls')
    banner()

    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890-=!@#$%^&()_+{}[];,."
    print('')
    shift = input(CGREEN+"[*] Enter the key of your ransome : "+CEND)
    print('')
    global ext_aft_infect
    ext_aft_infect =  input(CGREEN+"[*] Enter Infected extension of ransomware : "+CEND)
    print('')

    print(CRED+"Key : "+ shift + "\n"
          "Infection Extension : "+ ext_aft_infect + "\n"+CEND)


    print( CYELLOW+"[+] Your Ransomware  is going to be Decrypted" +CEND )
    cwd = os.getcwd()
    global dectobefile
    global dec_file_output
    dec_file_output = ''
    for i in os.listdir(cwd):
        if i.endswith(ext_aft_infect):
            print(i)
            with open(i, "rb+") as df:
                dectobefullfile = df.name
                dectobefile = os.path.splitext(dectobefullfile)[0]
                for x in range(len(dectobefile)):
                    dec_file_char = dectobefile[x]
                    dec_file_char_location = alpha.find(dec_file_char)
                    #dec_file_char_newlocation = (dec)
                    dec_file_output += alpha[dec_file_char_location - (int(shift))% 82]
                    #print(dec_file_output)
                    if x >= len(dectobefile)-1:
                        df.close()
                        rename( dec_file_output )
                        print( CGREEN+'[+] '+i + ' is encrypted to ' + dec_file_output+CEND )
                        dec_file_output = ''
                        print( dec_file_output )


def rename(dec_file_output):
    os.rename(dectobefile + ext_aft_infect, dec_file_output)



if __name__ == '__main__':
    main()