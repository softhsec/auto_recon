import os  # import a os module

os.system("clear") #clear screen
print("""
    Hello world!
   __   _  _  ____  __   _  _   __  ____  __  __   __ _       
  / _\ / )( \(_  _)/  \ ( \/ ) / _\(_  _)(  )/  \ (  ( \      
 /    \) \/ (  )( (  O )/ \/ \/    \ )(   )((  o )/    /      
 \_/\_/\____/ (__) \__/ \_)(_/\_/\_/(__) (__)\__/ \_)__)      
  
  _|-|_  Created by Anonymous

    1. Subfinder + WaybackURLs + gf sqli + HTTPX -mc 200 
    2. Subfinder + WaybackURLs + gf IDOR + HTTPX -mc 200
    3. 
    4. 
    5. 
    6. 
    h. HELP! For more information on how to use the script
    """)


path_tools = input("path tools on your system: ") # to inform the path of the tools 
url = input("url: ") # to inform the target url 
name_files = input("name: ") # to set the name of files



# Subfinder
def subfinder():
  os.system(f"{path_tools}subfinder -d {url} > ./{name_files}/subfinder-{name_files}.txt")

# WaybackURL 
def waybackurl():
  os.system(f"cat ./{name_files}/subfinder-{name_files}.txt | {path_tools}waybackurls  > ./{name_files}/waybackurls-{name_files}.txt")

# GF sql injection
def gf_sqli():
  os.system(f"cat ./{name_files}/waybackurls-{name_files}.txt | {path_tools}gf sqli > ./{name_files}/sqli-gf-{name_files}.txt")
  os.system(f"wc ./{name_files}/sqli-gf-{name_files}.txt") 

# GF IDOR
def gf_idor():
  os.system(f"cat ./{name_files}/waybackurls-{name_files}.txt | {path_tools}gf idor > ./{name_files}/idor-gf-{name_files}.txt")
  os.system(f"wc ./{name_files}/idor-gf-{name_files}.txt")    
 
# HTTPX only code 200 for sqli
def httpx_200_sqli():
  os.system(f"{path_tools}httpx -list ./{name_files}/sqli-gf-{name_files}.txt -silent -mc 200 > ./{name_files}/httpx-200only-sqli-{name_files}.txt")
  os.system(f"wc ./{name_files}/httpx-200only-sqli-{name_files}.txt")

# HTTPX only code 200 for idor
def httpx_200_idor():
  os.system(f"{path_tools}httpx -list ./{name_files}/idor-gf-{name_files}.txt -silent -mc 200 > ./{name_files}/httpx-200only-idor-{name_files}.txt")
  os.system(f"wc ./{name_files}/httpx-200only-idor-{name_files}.txt")  





def main():
    os.system(f"mkdir {name_files}")
    choose = input("select an option: ") # for user input
    if choose == "1":
        subfinder()
        waybackurl()
        gf_sqli()
        httpx_200_sqli()
    elif choose == "2":
        subfinder()
        waybackurl()
        gf_idor()
        httpx_200_idor()
    elif choose == "h":
      print("""
            HELP!

      """)    
    else:
        print("""

          Invalid option! Try again...

        """)

main()