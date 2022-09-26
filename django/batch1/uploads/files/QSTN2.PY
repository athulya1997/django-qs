import re
a=input('Enter Phone : ')


# pattern='^([0-9]{3})+([\s|-])+([0-9]{3})+([\s|-])+([0-9]{4})$'

pattern='^([0-9]{3})+([\)|\s|-])+([0-9]{3})+([\s|-])+([0-9]{4})$'
res=re.search(pattern,a)
if res:
    print("Valid")
else:
    print("not valid")