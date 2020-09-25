# Let's open an external file:
ipsum_file = open('files/ipsum.txt')

# Now let's cycle through the file line by line:
# for line in ipsum_file:
#   print(line)

# Now let's strip out the empty space between the lines:
for my_line in ipsum_file:
  print(my_line.rstrip())


# we've already read through file and are at the end...in order to do this next
# task, we have to reset the cursor to the front of the text to the very first
# space, in this case, [0], using the "seek()" method like so:
ipsum_file.seek(0)

# OK so now let's use the "readlines()" method to read each line in the file,
# and assign each line as a string element in a list called "lines"
lines = ipsum_file.readlines()
print(lines)

# now let's set the cursor to the 45th element...
ipsum_file.seek(45)

# then from the 45th element, let's read 4 (i.e. really '3') elements:
selected_text = ipsum_file.read(4)

print(selected_text)
#=> scin

# if we start opening files and not closing them, we're gonna take a performance
# hit, so, here's how to close a file:
ipsum_file.close()

#####################################################################
# Opening & Closing Files is Not Ideal; Here's a Different Approach #
#####################################################################

# a function to filter out the brackets from the file we're importing below
def sequence_filter(line):
  # if '>' is not in the line, return the line
  return '>' not in line

with open('files/dna_sequence.txt') as dna_file:
  # while indented you can do s.thing with this file...
  # let's print out out the DNA sequences without the titles...
  lines = dna_file.readlines()
  # print(filter(sequence_filter, lines)) # This needs to be typecasted...
  print(list(filter(sequence_filter, lines)))
# ...once you're out of the indentation (code block) you've closed the connection
# to the externam .txt file
