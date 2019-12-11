def balanced_parenthesis(data):
	if len(data) % 2 != 0:
		return False

	opening = {'{','(','['}
	datas = {
		('(',')'),
		('[',']'),
		('{','}')
	}
	stack = []

	for e in data:
		if e in opening:
			stack.append(e)
		else:
			if len(stack) == 0:
				return False

			ch = stack.pop()

			if (ch, e) not in datas:
				return False
	return len(stack) == 0				

print(balanced_parenthesis('[]'))