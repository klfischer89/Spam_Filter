import os # import os package
import zipfile # import zipfile package

os.listdir("./data") # list files in data folder

os.path.exists("./data/Spam-Emails.zip") # check if file exists

if not os.path.exists("./data/Spam-Emails"): # extract spam mails if not allready done
    with zipfile.ZipFile("./data/Spam-Emails.zip", "r") as z: # open zipfile as z
        z.extractall("./data/Spam-Emails") 

# path = "./data/Spam-Emails/spam/00001.7848dde101aa985090474a91ec93fcf0" # get path to first email

# with open(path, mode = "r", encoding = "utf-8") as file: # open mail and truncate header
#     email = file.read()
#     content = email.split("\n\n", 1)[1]

def get_email_content(path):

    with open(path, mode = "r", encoding = "iso-8859-1") as file: # open mail and truncate header
        # read mail and split in two halfs
        email = file.read()
        email_parts = email.split("\n\n", 1)
        # check if mail has two parts, otherwise return None
        if len(email_parts) != 2:
            return None
        # get content of mail
        content = email_parts[1]
        return content

def read_emails(folder):
    contents = []
    for f in os.listdir(folder):
    # build path to an email
        complete_path = folder + "/" + f    
        # check if path is folder, if it is skip it
        if os.path.isdir(complete_path):
            continue
        # get content for this mail
        email_content = get_email_content(complete_path)
        # if mail has content, append it to the list
        if email_content != None:
            contents.append(email_content)
    return contents        


spam_path = read_emails("./data/Spam-Emails/spam")
ham_path = read_emails("./data/Spam-Emails/easy_ham")

