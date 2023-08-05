class math:
	def average(numbers):
		return sum(numbers) / len(numbers)
	def round(number, pos):
		pos = '-' + str(pos - 2)
		firstHalf = str(number)[:int(pos) - 1]
		firstHalf = int(firstHalf)
		if int(str(number)[len(str(firstHalf)):len(str(firstHalf)) + 1]) >= 5:
			firstHalf += 1
		newNumber = str(firstHalf)
		while len(newNumber) + 1 <= len(str(number)):
			newNumber = newNumber + '0'
		return int(newNumber)