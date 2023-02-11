# Python3 
from sys import maxsize
def sameCharAdj(string): 
	n = len(string) 
	st = set()
	st.add(string[0]) 
	for i in range(1, n):
		if string[i] == string[i - 1]:
			continue
		if string[i] in st:
			return False

		st.add(string[i])
	return True
def Swaps(string, l, r, cnt, minm):
	if l == r:
		if sameCharAdj(string):
			return cnt
		else:
			return maxsize

	for i in range(l + 1, r + 1, 1):  
		string[i], string[l] = string[l], string[i]          
		cnt += 1									  
		x = Swaps(string, l + 1, r, cnt, minm)
		string[i], string[l] = string[l], string[i]
		cnt -= 1
		y = Swaps(string, l + 1, r, cnt, minm)
		minm = min(minm, min(x, y))

	return minm
T=int(input())
for _ in range(T):
	string = input()  
	string = list(string) 

	n = len(string) 
	cnt = 0
	minm = maxsize
	print(Swaps(string, 0, n - 1, cnt, minm))

# 4 
# 000 0
# 2010112 2
# 1011210 1
# 2120201 2