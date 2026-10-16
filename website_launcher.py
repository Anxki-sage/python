import webbrowser
#enter the websites here you want to open 
websites = [
    "https://www.google.com",
   
]

def open_website(websites):
    try:
        for website in websites:
         
           
         webbrowser.open(website)
        print(f"opening:{website}")
    except webbrowser.Error as error:
        print(f"website not opening: {website}")

open_website(websites)





