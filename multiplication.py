#10 bit input 
def check_overflow(a,b,c):
	if sign(a)*sign(b)==-1:
		return False
	else:
		if sign(a)!=sign(c):
			return True
		else:
			return False

def sign(a):
	return int(a[0])
def operate(a,plicand):
	decider=a[-2]+a[-1]
	if decider=="10":
		add(a[:11],complement(plicand))
	if decider=="01":
		add(a[:11],plicand)
	return rightShift(a)

def rightShift(a):
	s=a[-1]
	s+=a[0:len(a)-1]
	return s


def boothes(a,b):
	plicand=bin(a)[2:]
	plicand="0"*(11-len(plicand))+plicand

	plier=bin(b)[2:]
	plier="0"*(11-len(plier))+plier
	count=11
	newplier=11*"0"+plier+0
	for i in range(count):
		newplier=operate(newplier)
	return newplier
print("Enter multiplicand : ")
a=int(input())
print("Enter multipier : ")
b=int(input())






