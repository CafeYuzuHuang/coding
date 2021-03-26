# Read from the file file.txt and output the tenth line to stdout.

# 2021.03.26 
# 1st approach: use "AWK"
# r.f. https://www.runoob.com/linux/linux-comm-awk.html

# awk "NR == 10 {print}" file.txt # 4 ms (76%), 3.9 MB (17%)

# 2nd approach: if not familiar with awk script ...
# How about using stream editor (sed)?
# r.f. https://www.gnu.org/software/sed/manual/html_node/sed-commands-list.html

# suppress auto-print by -n and assign the print range by x,yp or xp
# where x and y are row numbers
sed -n 10p file.txt # 4 ms (76%) and 3.6 MB (82%)


