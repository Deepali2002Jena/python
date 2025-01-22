import re
email_file=input("enter file path for original email file:")
f=open(email_file,"r")
email_data=f.read()
f.close()
result=re.findall(r"\w+@\w+\.\w+",email_data)
print(result)

result_file=input("enter the filename to redirect output in:")
f=open(result_file,"w")
for line in result:
   f.write(line+"\n")
f.close()
