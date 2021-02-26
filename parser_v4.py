import os


input_bom_file = 'input_bom_file.bom'
vhdl_files_list = "vhdl_files_list.log"
burin_verif_file = "burin_verif.log"

bom_file = open(input_bom_file, 'r')
vhdl_list = open(vhdl_files_list, 'w')

for line in bom_file:
    if line[0] == 'c' and line.endswith('vhdl\n'):
        vhdl_file_path = line.split('| ')[-1]
        vhdl_list.write(vhdl_file_path)

bom_file.close()
vhdl_list.close()

# string that we want to find inside the vhdl files
burin_str = 'burnin'
vhdl_list = open(vhdl_files_list, 'r')
burnin_verif_wobj = open(burin_verif_file, 'w')

for path in vhdl_list:

    if os.path.exists(path):
        # the variable path contains an endline already so slicing
        current_vhdl_file = open(path[:-1], 'r', encoding='ISO-8859-1')
        vhdl_file_content = current_vhdl_file.read()

        if burin_str in vhdl_file_content:
            # the variable path contains an endline already
            write_str = path + "\n"
            burnin_verif_wobj.write(write_str)

        else:
            current_vhdl_file.close()
            continue

        current_vhdl_file.close()

burnin_verif_wobj.close()
vhdl_list.close()


# Start of the other file parsing for vhdl of other kind
# ------------------------------------------------------


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


