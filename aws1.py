#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os


# In[9]:


os.system("aws ec2 run-instances --image-id ami-011c99152163a87ae --count 1 --instance-type t2.micro --key-name first-keypair  --security-group-ids sg-a004e4dc --subnet-id subnet-b607f2dd")


# In[10]:


os.system("aws ec2 create-volume --availability-zone  ap-south-1a --size 5")


# In[ ]:





# In[ ]:





# In[ ]:




