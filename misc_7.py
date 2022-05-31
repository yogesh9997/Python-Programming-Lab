# APPEND TO FILE 

def program10():
    text = input("Enter text to append in the file:")
    with open("merge.txt","a") as f1:
        f1.write(text)
program10()
