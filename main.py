import customtkinter
import cryptography
import base64

'''
$ TODO $
## NOTE: Each of these functionality na ig aadd must have the capability to be reversed
# Add SHA-2 (SHA-224, SHA-256, SHA-384, SHA-512)
# Add SHA-3 (SHA3-224, SHA3-256, SHA3-384, SHA3-512)
# Add MD5
# Add BLAKE2 
# Add AES (Advanced Encryption Standard) in various modes (CBC, GCM, CFB, etc.)
# Add Fernet (a symmetric encryption implementation using a combination of AES and HMAC)
# Add RSA (Rivest-Shamir-Adleman)
# Add DSA (Digital Signature Algorithm)
# Add Elliptic Curve Cryptography (ECC) algorithms (ECDSA, ECDH)
# RSA signatures
# DSA signatures
# Binary to Text
'''
class App(customtkinter.CTk):

    encryptionAlgorithms = {
        "Base64": (base64.b64encode, base64.b64decode)
    }

    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.columnconfigure((0, 1), weight=1)

        ##### Application Title #####
        title_Label = customtkinter.CTkLabel(self, text="ENCRYPTION STUFF", font=("Arial", 20))
        title_Label.grid(row=0, column=0, columnspan=2, pady=20)

        ##### Text Box for Plaintext input #####
        self.plaintext_Entry = customtkinter.CTkTextbox(self, width=400, corner_radius=5)
        self.plaintext_Entry.grid(row=1, column=0, padx=20, columnspan=2, pady=15)

        ##### 
        self.recipie = customtkinter.CTkOptionMenu(self, values=["Hash Functions", "Symmetric Encryption", "Asymmetric Encryption", "Digital Signatures"], command=self.displayRecipie)
        self.recipie.grid(row=2, column=0)
        
        self.encryptionAlgoToUse = customtkinter.CTkOptionMenu(self, values=[
            "Base64", 
            ""
        ])

        self.encryptionAlgoToUse.grid(row=2, column=3)

        ##### Pick either to Encrypt to Decrypt #####
        self.encrypt_or_decrypt = customtkinter.CTkOptionMenu(self, values=["Encrypt", "Decrypt"], command=self.execute)
        self.encrypt_or_decrypt.grid(row=2, column=1)

        ##### Encrypted text output #####
        self.encryptedText_Entry = customtkinter.CTkTextbox(self, width=400, corner_radius=5)
        self.encryptedText_Entry.grid(row=3, column=0, padx=20, columnspan=2, pady=15)

    def execute(self, value):
        plaintext = self.plaintext_Entry.get("0.0", "end")
        encryptedText = base64.b64encode(str.encode(plaintext))
        self.encryptedText_Entry.insert("0.0", encryptedText)

app = App()
app.title("Encryption/Decryption GUI")
app.mainloop()
