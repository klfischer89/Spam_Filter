import os # import os package
import zipfile # import zipfile package

os.listdir("./data") # list files in data folder

os.path.exists("./data/Spam-Emails.zip") # check if file exists

if not os.path.exists("./data/Spam-Emails"): # extract spam mails if not allready done
    with zipfile.ZipFile("./data/Spam-Emails.zip", "r") as z: # open zipfile as z
        z.extractall("./data/Spam-Emails") 