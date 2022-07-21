import email
from moviepy.editor import *
from django.http import HttpResponse
from django.shortcuts import render
from home.models import contact 
from django.views.decorators.csrf import ensure_csrf_cookie

from django.core.files.storage import FileSystemStorage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

#from somewhere import handle_uploaded_file

#

    
def home(request):
    #return HttpResponse("This is my home page ")
    context = {'name':'Chirag','course':'Django'}
    return render(request,'home.html',context)

def about(request):
    #return HttpResponse("This is my about page ")
    return render(request,'about.html')

def form(request):
    if request.method == 'POST':
        email = request.POST['email']
        newfile = request.FILES['formFile']
        name = newfile.name
        fs = FileSystemStorage()
        fs.save(newfile.name,newfile)
        string_converter(name)
        email_wala_function(name,email)
        os.remove("C:/Users/chirag/vscode/django/portfolio/files/"+name)    
            
    return render(request,'form.html')

def contacts(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
       # print(name,email,phone,desc)
        ins = contact(name=name,email=email,phone=phone,desc=desc)
        ins.save()
        print("The data has been written to the db")
     #return HttpResponse("This is my contacts page ")
    return render(request,'contacts.html')    

   
def string_converter(name):
    text_file = open("C:/Users/chirag/vscode/django/portfolio/files/"+name,"r")
    data = text_file.read()#read whole file to a string
    final = data.upper()
    text_file.close()
    text_file = open("C:/Users/chirag/vscode/django/portfolio/files/"+name,"w")
    text_file.write(final)
    text_file.close()

def email_wala_function(given_name,given_email):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)#yeh is establishing connetion wiht gmail
    smtp.ehlo()
    smtp.starttls()
    #chalo login kara humnei
    #imp point if u want to send from a specifc id then in that id there must be allow acces to less secure apps wali permission on
    smtp.login('test.email.me61@gmail.com', 'test@password')

        # yahan pei we are building our email
        # filhal kei liy yeh essa hai abhi we i wil shape it accourdig to our need in program  
    def message(subject="Python Notification", text="Thank you", attachment=None):
        msg = MIMEMultipart()
        msg['Subject'] = subject

        msg.attach(MIMEText(text)) 
        if attachment is not None:
          
            # Check whether we have the
            # lists of attachments or not!
            if type(attachment) is not list:
            
              # if it isn't a list, make it one
                attachment = [attachment]  
  
            for one_attachment in attachment:
  
                with open(one_attachment, 'rb') as f:
                
                # Read in the attachment
                # using MIMEApplication
                    file = MIMEApplication(f.read(),name=os.path.basename(one_attachment))
                    file['Content-Disposition'] = f'attachment;\
                    filename="{os.path.basename(one_attachment)}"'
               
                msg.attach(file)
            return msg
    # Call the message function
    msg = message("Text file", "Hi there!",r"C:/Users/chirag/vscode/django/portfolio/files/"+given_name)
    #yahan pei we add the path to the fie we wana send 
    # .format y a+ lkarki we will add the string name 

    # to = ["singhsamarjeet09@gmail.com"]
    #multiple bando ko bhi bhej skatei hai cus we made a list
    # Provide some data to the sendmail function!
    smtp.sendmail(from_addr="test.email.me61@gmail.com",to_addrs=given_email, msg=msg.as_string())
  
     # Finally, don't forget to close the connection
    smtp.quit()
              

    
 