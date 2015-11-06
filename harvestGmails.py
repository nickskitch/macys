__author__ = 'Nick'
import imaplib
import quopri
import rfc822,StringIO,re
import gspread
import sys

# attempt to read in credentials from file that will not be checked in to vcs
try:
   from dev_settings import *
except ImportError:
   pass

def HarvestEmails():
    file=open(r"\tmp\emailHarvestTest.txt",'w')

    obj = imaplib.IMAP4_SSL('imap.googlemail.com', 993)
    obj.login(GMAILU, GMAILP)
    #obj.select('Hudson') #<-- the label in which u want to search message

    obj.select()
    typ, data = obj.search(None, '(SUBJECT "Visual Search Feedback")')

    print ('.')
    sys.stdout.write('Harvesting emails...')
    for num in data[0].split():
        typ, data = obj.fetch(num, '(RFC822)')
        #
        #print 'Message %s\n%s\n' % (num, quopri.decodestring(data[0][1]))
        file.write('Message %s\n%s\n' % (num, quopri.decodestring(data[0][1])))
        sys.stdout.write('.')

    obj.close()
    obj.logout()
    file.close()







def AddToSpreadsheet():
    gc = gspread.login(GMAILU, GMAILP)
    sh = gc.open("Visual Search Feedback")
    worksheet = sh.get_worksheet(0)


    file=open(r"\tmp\emailHarvestTest.txt",'r')

    lines = file.read()
    #print lines
    linesSplit=[]
    linesSplit = lines.split('Message ')
    counter=1

    print ('.')
    sys.stdout.write('Adding new survey''s to spreadsheet...')

    for message in linesSplit:
        #print message
        searchID = re.findall(r"(Search ID: [0-9]*)", message)
        categoryMsg=re.findall(r"(Category: [A-Z]*)", message)
        iGot=re.findall(r"(I got: [A-Z]*[a-z]*.*)\w+", message)
        commentMsg=re.findall(r"Comments:.*\n", message,re.MULTILINE)
        fromEmail=re.findall(r"From:.*\n", message,re.MULTILINE)
        dateOfMsg=re.findall(r"Date: .*\n", message,re.MULTILINE)

        #print str(searchID)
        if searchID:
            # try searching the spreadsheet for the searchID.  (.find throws an exception if text not found, so it's wrapped
            # in a try.
            try:
                sys.stdout.write('.')
                cell = worksheet.find(searchID[0].strip())
                #print 'found: '+searchID[0].strip()
            except:
                # It's a new value, format the strings
                print('adding '+searchID[0].strip())
                str1=dateOfMsg[0].strip()
                str2=searchID[0].strip()
                str3=''.join(c for c in iGot[0].strip() if (c.isalnum() or c == ' '))
                str4=categoryMsg[0].strip()
                str5=commentMsg[0].strip()
                str6=fromEmail[0].strip()


                worksheet.append_row([str1, str2, str3, str4, str5,str6])


    exit(0)


HarvestEmails()
AddToSpreadsheet()
