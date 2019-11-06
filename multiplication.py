#10 bit input 
from helper import *
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
		a=add(a[:11],twos_complement(plicand))+a[11:]
	if decider=="01":
		a=add(a[:11],plicand)+a[11:]
	return rightShift(a)

def rightShift(a):
	# s=convert_twos_complement(0)
	# s=add(a[0],a[0:len(a)-1])
	s=a[0]+a[0:len(a)-1]
	return s


def boothes(a,b):
	plicand=convert_twos_complement(a)

	# plicand="0"*(11-len(plicand))+plicand

	plier=convert_twos_complement(b)
	count=11
	newplier=11*"0"+plier+"0"
	for i in range(count):
		print(newplier)
		# print(len(newplier))
		newplier=operate(newplier,plicand)

	return newplier
print("Enter multiplicand : ")
a=int(input())
print("Enter multipier : ")
b=int(input())
print(boothes(a,b))






