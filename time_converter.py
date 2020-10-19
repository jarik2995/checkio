def time_converter(time):
	time,mode = time.split()
	h,m = map(int, time.split(':'))
	h %= 12
	if mode == 'p.m.':
		h += 12
	h = str(h).zfill(2)
	m = str(m).zfill(2)
	return f'{h}:{m}'

print(time_converter('12:54 p.m.'))

#school02web01