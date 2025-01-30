import pyfiglet

def app():
    text = input("Enter your text here : ")
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)

app()
