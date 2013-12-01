from django.template import Template,Context
from django.conf import settings
import pyperclip
import sys

argsList = None

if sys.argv[0] == "createCoverLetter.py":
    argsList = sys.argv[1:]
else:
    argsList = sys.argv

company_name=""

if len(argsList) != 1:
    print "Invalid number of arguments passed,"+str(len(argsList))+" , application terminating!"
    print "Expected args: \"companyName>\""
    sys.exit()
else:
    company_name = argsList[0]
    print "company name received:"+company_name

#creating a python script that will read in the coverLetter template
#add the company name, and save it to a new file and the system's clipboard
#Also append the current date to the letters as well

#now add company name parameter to python args
fp=open("templates/coverLetter.txt","r")
settings.configure()
t = Template(fp.read())
fp.close()

map = {
    "company":company_name,
}

c = Context(map)
letter = str(t.render(c))

file_name = "createdCLetters/"+company_name+"CoverLetter.txt"
outFile = open(file_name,"w+")
outFile.write(letter)
outFile.close()
print "Successfully created cover letter: "+file_name

#uses pyperclip module to set the system clipboard to letter
pyperclip.setcb(letter)

print "The cover letter has been appended to the system clipboard. Enjoy!"
