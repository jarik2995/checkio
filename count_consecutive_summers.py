# Sum of 1 + 2 + 3 + ... + m-1
def sum_m(m):
	result = 0
	for i in range(1,m):
		result = result + i
	return result

def count_cs(x):
	result = [x]
	for i in range(1,round(x/2)+1):
		# n + n + 1 + ... + n + m-1 = n*m + sum_n(m)
		m = round(x/2)
		for j in range(1,m+1):
			tmp = j*i + sum_m(j)
			if tmp > x:
				break
			if tmp == x:
				result.append(i)
				break
	return result

print(count_cs(11))
print(count_cs(11))
print(count_cs(4096))