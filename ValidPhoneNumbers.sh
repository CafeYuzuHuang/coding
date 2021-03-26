# Read from the file file.txt and output all valid phone numbers to stdout.

# 2021.03.26
# To find: (123) 456-7890 or 123-456-7890
# Use grep to search strings in file.txt, option -E for extended RegExp
# Note -e means standard RegExp

grep -E '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt
# grep -e '^(\([0-9]{3}\) |[0-9]{3}-)[0-9]{3}-[0-9]{4}$' file.txt # not work!

# runtime 4 ms (59%), memory 3.2 MB (54%)

