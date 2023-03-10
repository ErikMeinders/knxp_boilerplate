import sys
import os

if len(sys.argv) < 3:
    print("Usage: python replace.py <file1> <file2> <file3>")
    sys.exit()

file1 = sys.argv[1]
file2 = sys.argv[2]
file3 = sys.argv[3]

# Read the content of file1
with open(file1, 'r') as f1:
    content1 = f1.read()

# Read the content of file2
with open(file2, 'r') as f2:
    content2 = f2.read()

# Replace everything between '<marker>' and '</marker>' with the content of file2
start_marker = '<ApplicationPrograms>'
end_marker = '</ApplicationPrograms>'
start_index = content1.find(start_marker)
end_index = content1.find(end_marker)
if start_index != -1 and end_index != -1:
    content1 = content1[:start_index] + start_marker + '\n' + content2 + '\n' + end_marker + content1[end_index+len(end_marker):]

# Write the modified content to file3
output_file = file3
with open(file3, 'w') as f:
    f.write(content1)
    
print(f"The modified content has been written to {output_file}")