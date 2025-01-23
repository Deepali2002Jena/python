import re

log_file=input("Enter the file name here:")
f=open(log_file,"r")
log_data=f.read()
f.close()

result=re.findall(r"\d+\.\d+\.\d+\.\d+ \[\d{2}/\d{2}/\d{2} \d{2}:\d{2}:\d{2}\]",log_data)
print_ask=input("do you want to redirect the output ? [y/n]")
if print_ask.lower()[0] == "y":
   result_file=input("Enter the filename for redirecting:")
   f=open(result_file,"w")
   for line in result:
       f.write(line+"\n")
   f.close()
else:
   pass
