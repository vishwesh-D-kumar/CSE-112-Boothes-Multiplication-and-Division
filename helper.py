def decimal_to_binary(n):
	s=""
	while n>0:
		s=str(n%2)+s
		n=n//2

	while(len(s)<11):
		s="0"+s
	return s	


def convert_twos_complement(n):
	f=0
	if(n<0):
		f=1
		n=-n
	n=decimal_to_binary(n)
	# print(n)
	if f==1:
		n=list(n)
		for i in range(len(n)):
			n[i]=str(1-int(n[i]))
		n="".join(n)
		n=add(n,decimal_to_binary(1))
	return n
def twos_complement(n):
	n=list(n)
	for i in range(len(n)):
		n[i]=str(1-int(n[i]))
	n="".join(n)
	n=add(n,decimal_to_binary(1))
	return n	
	

def add(n1, n2):
	ans=""
	c=0
	for i in range(11):
		a=int(n1[10-i])
		b=int(n2[10-i])
		ans=str(a^(b^c))+ans
		if c+a+b>=2:
			c=1
		else:
			c=0
	return ans							


