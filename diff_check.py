import os
from typing import final

vhdl_file = open("vhdl_replica.txt", "r")
spider_file = open("vhdl.txt", "r")

vhdl_file_linelist = vhdl_file.read().split("\n")
spider_file_linelist = spider_file.read().split("\n")

spider_file.close()
vhdl_file.close()

final_output = open("final_output.txt", "w")

for file in vhdl_file_linelist:
    if file not in spider_file_linelist:
        file_write = file + str("\n\n")
        final_output.write(file_write)

final_output.close()
