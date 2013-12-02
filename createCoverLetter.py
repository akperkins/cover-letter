from django.template import Template,Context
from django.conf import settings
import pyperclip
import sys

'''
creating a python script that will read in the coverLetter template
add the company name, and save it to a new file and the system's clipboard
Also append the current date to the letters as well
the compnay_name variable in the tempate is passed to the application
'''

#parses args passed to the application
def init():
    if sys.argv[0] == "createCoverLetter.py":
        argsList = sys.argv[1:]
    else:
        argsList = sys.argv
        if len(argsList) != 1:
            print "Invalid number of arguments passed,"+str(len(argsList))+" , application terminating!"
            print "Expected args: \"companyName>\""
            sys.exit()
        else:
            company_name = argsList[0]
            print "company name received:"+company_name

#Creates the cover letter and returns it as a String
def createLetter():
    fp=open("templates/coverLetter.txt","r")
    settings.configure()
    t = Template(fp.read())
    fp.close()
    map = {
        "company":sys.argv[1],
        }

    c = Context(map)
    letter = str(t.render(c))
    return letter

#writes the letter to the createdCLetters directory
def writeLetter(letter):
    file_name = "createdCLetters/"+sys.argv[1]+"CoverLetter.txt"
    outFile = open(file_name,"w+")
    outFile.write(letter)
    outFile.close()
    print "Successfully created cover letter: "+file_name

#uses pyperclip module to set the system clipboard to letter
def copyToClipboard(letter):
    pyperclip.setcb(letter)
    print "The cover letter has been appended to the system clipboard. Enjoy!"

#start of application
def main():
    init()
    letter = createLetter()
    writeLetter(letter)
    copyToClipboard(letter)

main()
