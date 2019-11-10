from helper import *

def boothes(dividend,divisor):
	if divisor==0:
		print("Divisor cannot be zero")
		return

	aplusq=convert_twos_complement(dividend,8)
	print(aplusq)
	m=convert_twos_complement(divisor,4)
	a=aplusq[:4]
	q=aplusq[4:]
	count=4
	print("Step:",0,"A:",a,"Q:",q,"M:",m)
	print("Step:",0,"A:",twos_complement_to_decimal(a),"Q:",twos_complement_to_decimal(q),"M:",twos_complement_to_decimal(m))

	for i in range(count):
		print("Step",i+1)
		aplusq=a+q
		aplusq=aplusq[1:]+"0"
		a=aplusq[:4]
		q=aplusq[4:]
		print("After Shift ",i+1,"A:",a,"Q:",q,"M:",m)

		previous=a
		if m[0]==aplusq[0]:
			a=add(aplusq[:4],twos_complement(m,4))
		else:
			a=add(aplusq[:4],m)	
		print("After adding",i+1,"A:",a,"Q:",q,"M:",m)

		if a[0]==previous[0] or a==("0"*4) or (a==("0"*4) and q=="0"*4):
			q=q[:-1]+"1"
		else:
			print("restored")
			a=previous
			q=q[:-1]+"0"
		print("Finally",i+1,"A:",a,"Q:",q,"M:",m)
		print("Finally",i+1,"A:",twos_complement_to_decimal(a),"Q:",twos_complement_to_decimal(q),"M:",twos_complement_to_decimal(m))


	if dividend*divisor<0:
		q=twos_complement(q,4)
	a=twos_complement_to_decimal(a)
	q=twos_complement_to_decimal(q)	
	print("Quotient:",q,"Remainder:",a)



print("Enter Dividend : ")
dividend=int(input())
print("Enter Divisor : ")
divisor=int(input())
boothes(dividend,divisor)