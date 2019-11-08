from helper import *

def boothes(dividend,divisor):
	if divisor==0:
		print("Divisor cannot be zero")
		return
	aplusq=convert_twos_complement(dividend,22)
	m=convert_twos_complement(divisor,11)
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
		print("Step:",0,"A:",a,"Q:",q,"M:",m)


	if dividend*divisor<0:
		q=twos_complement(q,11)
	a=twos_complement_to_decimal(a)
	q=twos_complement_to_decimal(q)	
	print("Quotient:",q,"Remainder:",a)



print("Enter Dividend : ")
dividend=int(input())
print("Enter Divisor : ")
divisor=int(input())
boothes(dividend,divisor)