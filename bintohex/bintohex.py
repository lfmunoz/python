input = open("binary.txt", "r") # open file for reading
output = open("hex.txt", "w") # open file for writing
for line in input:
  output.write("0x%012x\n" % int(line, 2))

input.close()
output.close()



