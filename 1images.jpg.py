# ques1
import re
email=input('Enter email id:')
a=re.fullmatch('^[a-zA-Z][_a-zA-z0-9.]*(@)(gmail.com|yahoo.com)',email)
if a:
    print('email is valid')
else:
    print('email is not valid')
  


# ques2
import re
x=input('Enter Indian Phone number:')

match=re.fullmatch('(\+91-)[6-9][0-9]{9}',x)
if a:
    print('phone number is valid')
else:
    print('phone number is not valid')
  
