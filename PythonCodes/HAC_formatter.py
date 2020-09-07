

hac_input = input("Enter your HAC balance: ")
sen =''.join(i for i in hac_input if i.isdigit())
sen1 = int(sen)
sr1 = sen[:-3]
sr2 = int(sr1)

#identifier
identifier = abs(sen1)%1000



if (identifier == 230):
    sr230Div = sr2/1000000000000000000
    hac_balance = sr230Div
if (identifier == 231):
    sr231Div = sr2/100000000000000000
    hac_balance = sr231Div
if (identifier == 232):
    sr232Div = sr2/10000000000000000
    hac_balance = sr232Div
if (identifier == 233):
    sr233Div = sr2/1000000000000000
    hac_balance = sr233Div
if (identifier == 234):
    sr234Div = sr2/100000000000000
    hac_balance = sr234Div
if (identifier == 235):
    sr235Div = sr2/10000000000000
    hac_balance = sr235Div
if (identifier == 236):
    sr236Div = sr2/1000000000000
    hac_balance = sr236Div
if (identifier == 237):
    sr237Div = sr2/100000000000
    hac_balance = sr237Div
if (identifier == 238):
    sr238Div = sr2/10000000000
    hac_balance = sr238Div
if (identifier == 239):
    sr239Div = sr2/1000000000
    hac_balance = sr239Div
if (identifier == 240):
	sr240Div = sr2/100000000
	hac_balance = sr240Div
if (identifier == 241):
	sr241Div = sr2/10000000
	hac_balance = sr241Div
if (identifier == 242):
	sr242Div = sr2/1000000
	hac_balance = sr242Div
if (identifier == 243):
	sr243Div = sr2/100000
	hac_balance = sr243Div
if (identifier == 244):
	sr244Div = sr2/10000
	hac_balance= sr244Div
if (identifier == 245):
	sr245Div = sr2/1000
	hac_balance = sr245Div
if (identifier == 246):
	sr246Div = sr2/100
	hac_balance = sr246Div
if (identifier == 247):
	sr247Div = sr2/10
	hac_balance = sr247Div
if (identifier == 248):
	sr248Div = sr2/1
    
	hac_balance = sr248Div
if (identifier == 249):
	sr249Div = sr2*.1
	hac_balance = sr249Div
if (identifier == 250):
	sr250Div = sr2/.01
	hac_balance = sr250Div
if (identifier == 251):
	sr251Div = sr2/.001
	hac_balance = sr251Div
if (identifier == 252):
	sr252Div = sr2/.0001
	hac_balance = sr252Div
    
if (identifier == 253):
	sr253Div = sr2/.00001
	hac_balance = sr248Div
if (identifier == 254):
	sr254Div = sr2/.000001
	hac_balance = sr254Div
if (identifier == 255):
	sr255Div = sr2/.0000001
	hac_balance = sr255Div



#list
sr230Mul = int(hac_balance*1000000000000000000)
sr231Mul = int(hac_balance*100000000000000000)
sr232Mul = int(hac_balance*10000000000000000)
sr233Mul = int(hac_balance*1000000000000000)
sr234Mul = int(hac_balance*100000000000000)
sr235Mul = int(hac_balance*10000000000000)
sr236Mul = int(hac_balance*1000000000000)
sr237Mul = int(hac_balance*100000000000)
sr238Mul = int(hac_balance*10000000000)	
sr239Mul = int(hac_balance*1000000000)
sr240Mul = int(hac_balance*100000000)
sr241Mul = int(hac_balance*10000000)
sr242Mul = int(hac_balance*1000000)
sr243Mul = int(hac_balance*100000)
sr244Mul = int(hac_balance*10000)
sr245Mul = int(hac_balance*1000)
sr246Mul = int(hac_balance*100)
sr247Mul = int(hac_balance*10)



hb='{:.8f}'.format(hac_balance) #




print("...")
#print(f"Your {hac_input}is equivalent to:")
print("Your %s HAC is equivalent to: "%hac_input)
print("=================")
str1 = u'\u311c'
print(str1, end = ' ') 
print(hb, end = ' ')
print("HAC")
str1 = u'\u311c'
print(str1, end = ' ') 
print(hb, end = '')
print(":248")
print("=================")







print(str1, end = ' ') 
print(sr247Mul, end = '')
print(":247")
print(str1, end = ' ') 
print(sr246Mul, end = '')
print(":246")
print(str1, end = ' ') 
print(sr245Mul, end = '')
print(":245")
print(str1, end = ' ') 
print(sr244Mul, end = '')
print(":244")
print(str1, end = ' ') 
print(sr243Mul, end = '')
print(":243")
print(str1, end = ' ') 
print(sr242Mul, end = '')
print(":242")
print(str1, end = ' ') 
print(sr241Mul, end = '')
print(":241")
print(str1, end = ' ') 
print(sr240Mul, end = '')
print(":240")




