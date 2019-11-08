def decimal_to_binary(n,l):
	s=""
	while n>0:
		s=str(n%2)+s
		n=n//2

	while(len(s)<l):
		s="0"+s
	return s	


def convert_twos_complement(n,l):
	f=0
	if(n<0):
		f=1
		n=-n
	n=decimal_to_binary(n,l)
	# print(n)
	if f==1:
		n=list(n)
		for i in range(len(n)):
			n[i]=str(1-int(n[i]))
		n="".join(n)
		n=add(n,decimal_to_binary(1,l))
	return n

def twos_complement(n,l):
	n=list(n)
	for i in range(len(n)):
		n[i]=str(1-int(n[i]))
	n="".join(n)
	n=add(n,decimal_to_binary(1,l))
	return n	
	

def add(n1, n2):
	ans=""
	c=0
	l=len(n1)
	for i in range(l):
		a=int(n1[l-i-1])
		b=int(n2[l-i-1])
		ans=str(a^(b^c))+ans
		if c+a+b>=2:
			c=1
		else:
			c=0
	return ans

def twos_complement_to_decimal(n):
	f=0
	if n[0]=="1":
		f=1
		n=twos_complement(n,len(n))
	value=0
	r=1
	l=len(n)
	for i in range(l-1):
		value+=(r*int(n[l-i-1]))
		r=r*2
	if f==1:
		value=-value
	return value		


