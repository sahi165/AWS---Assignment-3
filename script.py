import os
import collections
import socket

# Define the paths to the files
data_path = '/home/data'
output_path = '/home/output/result.txt'

# Specify the filenames to read
filenames = ['IF.txt', 'Limerick-1.txt']

# Initialize a dictionary to keep the word count for each file
word_counts = {}

# Initialize a variable to keep the total word count
total_word_count = 0

# Count words in specified files
for filename in filenames:
    with open(os.path.join(data_path, filename), 'r') as file:
        words = file.read().split()
        word_counts[filename] = len(words)
        total_word_count += len(words)

# Get the IP address of the machine
ip_address = socket.gethostbyname(socket.gethostname())

# Write the results to the output file
with open(output_path, 'w') as file:
    for filename, count in word_counts.items():
        file.write(f"{filename}: {count} words\n")
    file.write(f"Grand total of words: {total_word_count}\n")
    file.write(f"IP Address: {ip_address}\n")

# Print the result.txt content
with open(output_path, 'r') as file:
    print(file.read())

