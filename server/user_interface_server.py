from customtkinter import *
import tkinter as tk
import customtkinter
import backend_server
import threading

class UserInterface(CTk):
    def __init__(self, server):
        super().__init__()
        self.title("Server")

        #GETING SCREEN DIMENSIONS TO MAKE IT DYNAMIC
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        #calculating the center of the screen
        position_x = int(screen_width/2 -(700/2))
        position_y = int(screen_height/2 - (500/2))
        server.set_ui(self)

        self.geometry(f"700x770+{position_x+600}+{position_y-160}")
        self.resizable(False,False)
        server.start()
        response = threading.Thread(target=server.accept_connections, daemon=True).start()
        # Create the main screen
        self.create_main_screen(server)
    def create_main_screen(self,server):
        self.head = customtkinter.CTkLabel(self, text="Server Side", bg_color="transparent", font=("Verdana", 24, "bold"))
        self.head.grid(row=0, column=0, pady=30, padx=250)
        # Add a textbox for the server to display messages
        self.textbox = customtkinter.CTkTextbox(self, width=550, height=500)
        self.textbox.grid(row=1, column=0, padx=20, pady=20)
    def display_message(self, message):
        """Display a message in the textbox."""
        self.textbox.insert(tk.END, message + "\n")
        self.textbox.see(tk.END)
    

    
         
def main():
    # Create an instance of the UserInterface class
    server = backend_server.BackendServer()
    app = UserInterface(server)
    app.mainloop()
if __name__ == "__main__":
    main()
