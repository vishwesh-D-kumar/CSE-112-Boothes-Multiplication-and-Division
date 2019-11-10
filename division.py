from helper import *

def boothes(dividend,divisor):
	if divisor==0:
		print("Divisor cannot be zero")
		return
	aplusq=convert_twos_complement(dividend,22)
	m=convert_twos_complement(divisor,11)
	flag1=0
	flag2=0
	if aplusq[0]=="1":
		aplusq=twos_complement(aplusq,22)
		flag1=1
	if m[0]=="1":
		m=twos_complement(m,11)
		flag2=1				
	a=aplusq[:11]
	q=aplusq[11:]
	count=11
	print("Step:",0,"A:",a,"Q:",q,"M:",m)
	for i in range(count):
		aplusq=a+q
		aplusq=aplusq[1:]+"0"
		a=aplusq[:11]
		q=aplusq[11:]
		previous=a
		if m[0]==aplusq[0]:
			a=add(aplusq[:11],twos_complement(m,11))
		else:
			a=add(aplusq[:11],m)	
		if a[0]==previous[0] or (a==("0"*11) and q=="0"*11):
			q=q[:-1]+"1"
		else:
			a=previous
		print("Step:",i+1,"A:",a,"Q:",q,"M:",m)

	if flag1==1 and flag2==0:
		q=twos_complement(q,11)
		a=twos_complement(a,11)
	if flag1==0 and flag2==1:
		q=twos_complement(q,11)
	if flag1==1 and flag2==1:
		a=twos_complement(a,11)
	print("Quotient:",q,"Remainder:",a)
	a=twos_complement_to_decimal(a)
	q=twos_complement_to_decimal(q)	
	print("Quotient:",q,"Remainder:",a)

c=[456,-10,-20,-1000,1000]
d=[0,-3,3,-1,1000]

for i in range(5):
	print("Sample Test",i+1,":",c[i],"divided by",d[i])
	boothes(c[i],d[i])
	print("----x----x-----x-----x----")	

print("Enter Dividend : ")
dividend=int(input())
print("Enter Divisor : ")
divisor=int(input())
boothes(dividend,divisor)
