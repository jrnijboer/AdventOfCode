from collections import Counter

with open("day6.input") as inputfile:
	columns = zip(*[list(message[:-1]) for message in inputfile])

answer = ''
for column in columns:
	answer += Counter(column).most_common()[0][0]
print answer
