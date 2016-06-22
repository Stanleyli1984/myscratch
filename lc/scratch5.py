def divide(a, b):
	real = a / b
	remain = a % b
	decimal = []
	remainders = {}
	i = 0
	while remain != 0:
		if remain not in remainders:
			remainders[remain] = i
		else:
			decimal.insert(remainders[remain],'(')
			break
		remain *= 10
		digit, remain = divmod(remain, b)
		decimal.append(str(digit))
		i += 1
	if remain != 0:
		decimal.append(')')
	return str(real) + '.' + ''.join(decimal)

divide(15, 13)