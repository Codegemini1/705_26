def square_evenodd (a):
	square = a*a
	even_odd = ''
	if a%2 == 0:
		even_odd = 'Even'
	else:
		even_odd = 'Odd'
	return square, even_odd
		