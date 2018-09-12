import math

data_file = 'result-2.txt'

raw_data = open(data_file).read()

print('Length of the raw data: ', len(raw_data))

data_array = raw_data.split('\n')

print('Length of the split array: ', len(data_array))

array_splitter_number = math.ceil(len(data_array) / 2)

print('The data should have: ', array_splitter_number, ' on the left and right')


with open('result-3.txt', 'a+') as file_handler:
	for sentence in data_array[:array_splitter_number]:
		file_handler.write(sentence+'\n')
