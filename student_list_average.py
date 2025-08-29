#Student situation

student = {}

student['name'] = input('Name:\n')
student['average'] = float(input(f'{student['name'].capitalize()} Average:\n'))

if student['average'] >= 7:
	student['situation'] = 'Passed'
else:
	student['situation'] = 'Failed'
	
for key, value in student.items():
	print(f'  - {key}: {value}')