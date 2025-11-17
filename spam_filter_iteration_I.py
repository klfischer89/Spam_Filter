import os # import os package
import zipfile # import zipfile package

os.listdir("./data") # list files in data folder

os.path.exists("./data/Spam-Emails.zip") # check if file exists

if not os.path.exists("./data/Spam-Emails"): # extract spam mails if not allready done
    with zipfile.ZipFile("./data/Spam-Emails.zip", "r") as z: # open zipfile as z
        z.extractall("./data/Spam-Emails") 

path = "./data/Spam-Emails/spam/00001.7848dde101aa985090474a91ec93fcf0" # get path to first email

with open(path, mode = "r", encoding = "utf-8") as file: # open mail and truncate header
    email = file.read()
    content = email.split("\n\n", 1)[1]


    
    