from django.template import Template,Context
from django.conf import settings
import pyperclip
import sys
import os
'''
creating a python script that will read in the coverLetter template
add the company name, and save it to a new file and the system's clipboard
Also append the current date to the letters as well
the compnay_name variable in the tempate is passed to the application
'''
CREATEDDIR = "createdCLetters/"
TEMPLATEDIR = "templates/"
COVERLETTER = "coverLetter.txt"

#creates a directory if one doesn't exist
def createDir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)
        print "Directory "+dir+" was created."
    else:
	print "Directory "+dir+" already existed"

#parses args passed to the application, checks template dir exist (otherwise application terminated),
#creates the createdDir
#TODO refactor out all the system verification code into its' own method
def init():
    print "Expected args: \"companyName>\""
    if sys.argv[0] == "createCoverLetter.py":
        argsList = sys.argv[1:]
    else:
        argsList = sys.argv
        if len(argsList) != 1:
	    print "Invalid number of arguments passed,"+str(len(argsList))+" , application terminating!"        
            sys.exit()
        company_name = argsList[0]
        print "company name received:"+company_name
    if not  os.path.exists(TEMPLATEDIR) :
	print "There was not a template folder found in the indicated directory...application temrinating!"
	sys.exit()
    if not os.path.isfile(TEMPLATEDIR+COVERLETTER):
	print "Issue with reading the cover letter..application terminating!"
        sys.exit()
    print "The cover letter at "+TEMPLATEDIR+COVERLETTER+" was successfully found"
    createDir(CREATEDDIR)

#Creates the cover letter and returns it as a String
def createLetter():
    fp=open(TEMPLATEDIR+COVERLETTER,"r")
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
    file_name = CREATEDDIR+sys.argv[1]+COVERLETTER
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
