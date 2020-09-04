
hac_input = input("Enter your HAC balance: ")
sen =''.join(i for i in hac_input if i.isdigit())
sen1 = int(sen)
sr1 = sen[:-3]
sr2 = int(sr1)

#identifier
identifier = abs(sen1)%1000



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


#list	
sr240Mul = int(hac_balance*100000000)
sr241Mul = int(hac_balance*10000000)
sr242Mul = int(hac_balance*1000000)
sr243Mul = int(hac_balance*100000)
sr244Mul = int(hac_balance*10000)
sr245Mul = int(hac_balance*1000)
sr246Mul = int(hac_balance*100)
sr247Mul = int(hac_balance*10)
sr248Mul = int(hac_balance*1)


hb='{:.8f}'.format(hac_balance)



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


