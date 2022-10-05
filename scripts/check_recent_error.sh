#!/bin/bash
# reference: https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
# in bash, "&&" will execute sequentially ; "&" will execute simultaneously
# (("command 1") || (echo "command 1 failed")) && ((ssh mlgpu) || (echo "command 'ssh mlgpu' failed") && (echo "command 4"))

current_position=`pwd`

error_book_file_name="error_book_en.txt"
parentdir="$(dirname "${current_position}")"
#echo "current_position: ${current_position}; parentdir: ${parentdir}"
grep -e '^[a-z]' "${current_position}/${error_book_file_name}" | uniq | head -n 10
