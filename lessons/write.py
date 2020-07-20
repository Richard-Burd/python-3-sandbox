# when we open up a file, it is a read-only unless the "open()" method takes in
# the second variable "w" that enables you to write to the file.
with open('files/write.txt', 'w') as write_file:
  # use the "write()" method to write s.thing to the file
  write_file.write("I will be written only once in the file and wipe out all previous content.")
  # this will open up the file, look at what is inside, and override whatever
  # is inside it...that means this string will appear only once in that file...
  # ...and EVERYTHING ELSE in that file will be deleted.


# now we're gonna ammend the file, you can repeat this and you will get repeat strings appearing:
with open('files/write.txt', 'a') as write_file:
  # use the "write()" method to write s.thing to the file
  write_file.write("\nI am being amended to the string above.")


# let's make a list of quotes to work with:
lahja_quotes = [
"\n1.) Marhaba ya a7"
"\n2.) 3ni alek"
"\n3.) Saba7 al 7er"
]

with open('files/write.txt', 'a') as write_file:
  # the "writelines()" method expect some kind of list and it will cycle through
  # that list and write them to the document
  write_file.writelines(lahja_quotes)
