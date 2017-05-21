'''
Author: Blair Gemmer
Description:
Compares two files that contain arrays of JSON objects, merging them into one output file.
'''

import json
import os

def write_json(filename=None, data=None):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile)

def read_json(filename=None):
    with open(filename) as infile:    
        data = json.load(infile)
    return data

input_directory = 'input'
output_directory = 'output'
output_filename = 'merged_files.json'

# Field name (if it exists) that contains an array of JSON objects:
old_data_field = 'data'
new_data_field = 'data'
merged_data = {
	new_data_field: []
}
extra_data = []

for filename in os.listdir(input_directory):
	input_filepath = os.path.join(input_directory, filename)

	data = read_json(filename=input_filepath)
	
	if old_data_field != None:
		data = data[old_data_field]
	entries = len(data)

	print('{filename} has {entries} entries.'.format(filename=filename, entries=entries))

	for data_entry in data:
		if data_entry not in merged_data[new_data_field]:
			merged_data[new_data_field].append(data_entry)
		else:
			extra_data.append(data_entry)


# print(json.dumps(merged_data, indent=4))
# print(json.dumps(extra_data, indent=4))
output_filepath = os.path.join(output_directory, output_filename)
write_json(filename=output_filepath, data=merged_data)