import customtkinter
from customtkinter import *
import tkinter as tk
import backend_client
from functools import partial

class UserInterface(CTk):
    def __init__(self, client):
        super().__init__()
        self.title("Client")

        #GETING SCREEN DIMENSIONS TO MAKE IT DYNAMIC
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        #calculating the center of the screen
        position_y = int(screen_height/2 - (500/2))

        self.geometry(f"700x770+{60}+{position_y-160}")
        self.resizable(False,False)
        client.connect()
        self.create_main_screen(client)


    def create_main_screen(self, client):
    # CLEARING WIDGETS OF PREVIOUS WINDOW    

        # ADDING HEADING TO THE MAIN PAGE
        self.head = customtkinter.CTkLabel(self, text="Client Side", bg_color="transparent", font=("Verdana", 24, "bold"))
        self.head.grid(row=0, column=0, pady=30, padx=250)

        
        self.textbox = customtkinter.CTkEntry(self, placeholder_text="Type Message", font=("Verdana", 16), width=550,height=40)
        #calculating the center of the screen
        position_x = int(20)
        position_y = int(680)
        self.textbox.place(x=position_x, y=position_y)
        self.encryptmenu = customtkinter.CTkOptionMenu(self, values=["AES", "DES3", "Caesar"])
        self.encryptmenu.place(x=20, y=position_y+50)
        self.encryptmenu.set("Encryption Algorithm")
        self.send_button = customtkinter.CTkButton(self, text="Send", width=80, height=40, command=partial(self.send_message, client))
        self.send_button.place(x=580, y=position_y)
    def send_message(self, client):
        """Send a message to the server."""
        message = self.textbox.get()
        encryption_algorithm = self.encryptmenu.get()
        if message:
            # Create a backend client instance
            client.send_request(message, encryption_algorithm)
            self.textbox.delete(0, 'end')

def main():
    client = backend_client.BackendClient()
    app = UserInterface(client)
    app.mainloop()
    client.close()

if __name__ == "__main__":
    main()
