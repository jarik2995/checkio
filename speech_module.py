def ones(x):
	result = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
	return result[int(x)]

def excepts(x):
	result = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	return result[int(x)]

def tens(x):
	result = ['', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
	return result[int(x)-1]

def hundreds(x):
	return ones(x) + ' hundred'

def TwoDigit(x):
	if x >= 0 and x <=9:
		result = ones(x)
	elif x >= 10 and x <= 19:
		result = excepts(str(x)[1])
	elif x >= 20 and x <= 99:
		result = tens(str(x)[0]) + ' ' + ones(str(x)[1])
	return result.rstrip()

def main(x):
	if x >= 1 and x <= 99:
		result = TwoDigit(x)
	else:
		result = ones(str(x)[0]) + ' hundred ' + TwoDigit(int(str(x)[1:]))
	return result.rstrip()



print(main(900))