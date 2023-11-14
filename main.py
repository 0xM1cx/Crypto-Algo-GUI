import customtkinter
import base64

class App(customtkinter.CTk):

    encryptionAlgorithms = {
        "Base64": (base64.b64encode, base64.b64decode)
    }

    def __init__(self):
        super().__init__()
        self.geometry("500x600")

        ##### Application Title #####
        title_Label = customtkinter.CTkLabel(self, text="ENCRYPTION STUFF", font=("Arial", 20))
        title_Label.pack()

        # plainTextInput_Label = customtkinter.CTkLabel(self, text="Plaintext", fg_color="transparent", font=("Arial", 15))
         # plainTextInput_Label.pack()

        ##### Text Box for Plaintext input #####
        self.plaintext_Entry = customtkinter.CTkTextbox(self, width=400, corner_radius=5)
        self.plaintext_Entry.pack(expand=1)

        ##### Buttons #####
        self.encrypt_Button = customtkinter.CTkButton(self, text="Encrypt", command=self.encrypt)
        self.encrypt_Button.pack(expand=1)
        self.ecryptionAlgoToUse = customtkinter.CTkOptionMenu(self, values=[
            "Base64", 
            ""
        ])


        ##### Encrypted text output #####
        self.encryptedText_Entry = customtkinter.CTkTextbox(self, width=400, corner_radius=5)
        self.encryptedText_Entry.pack(expand=1)

    def encrypt(self):
        plaintext = self.plaintext_Entry.get("0.0", "end")
        encryptedText = base64.b64encode(str.encode(plaintext))
        self.encryptedText_Entry.insert("0.0", encryptedText)
        
app = App()
app.mainloop()