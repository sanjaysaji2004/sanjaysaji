# Python3 program for implementation of efficient
# approach to find length of last word


def findLength(str):
	count = 0
	flag = False
	for i in range(len(str) - 1, -1, -1):
		if ((str[i] >= 'a' and str[i] <= 'z') or (str[i] >= 'A' and str[i] <= 'Z')):
			flag = True
			count += 1
		elif (flag == True):
			return count
	return count


# Driver code
str = "Geeks for Geeks"
print("The length of last word is",
	findLength(str))



