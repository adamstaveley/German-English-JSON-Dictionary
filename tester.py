import sys
import json

with open('./german_english.json') as filename:
	dictionary = json.load(filename)

correct = []
incorrect = []

for word, translation in dictionary.items():
	print(word)
	user_input = input()
	if translation in user_input or user_input in translation:
		print('Correct! ("{}")'.format(translation))
		correct.append(word)
	elif user_input == '\q':
		sys.exit()
	elif user_input == '\s':
		print('Correct: {}\nIncorrect: {}'.format(len(correct), len(incorrect)))
	elif user_input == '\c':
		print('Correct: {}\nIncorrect: {}'.format(correct, incorrect))
	elif user_input == '\h':
		# show help text
	else:
		print('Incorrect! ("{}")'.format(translation))
		incorrect.append(word)
