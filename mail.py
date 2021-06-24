#!/usr/bin/env python
# coding: utf-8

# In[1]:


import smtplib as smt


# In[2]:


ob = smt.SMTP("smtp.gmail.com",587)   #make a server for gmail

ob.starttls()

ob.login("kashi14590@gmail.com","rtu181459") #login details

subject = "Sending By himanshu"  #subject of email

body="Hello, This is Himanshu" #email body

message = "Subject:{}\n\n{}".format(subject,body) #this is all message 

ob.sendmail("kashi14590@gmail.com","himanshu1999may@gmail.com",message) # senderEmail,RecevierEmail,message

print("send successfully")
ob.quit() #use to quit the all process


# In[ ]:




