import os

input_file = "/home/shrinivas/workspace/shefali_shell/something.txt"
infile = open(input_file, "r")

burnin_str = "BURNIN"

file_contents = infile.read()
file_content_separated = file_contents.split("// ")[1:]
infile.close()

output_file = "/home/shrinivas/workspace/shefali_shell/vhdl.txt"
outfile = open(output_file, "w")

for index in file_content_separated:
    if burnin_str in index:
        split_by_line_lst = index.split("\n")
        split_by_space = split_by_line_lst[0].split(" ")
        vhdl_path = split_by_space[-1] + str("\n\n")
        outfile.write(vhdl_path)


outfile.close()
