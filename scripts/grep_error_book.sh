#!/bin/bash
# reference: https://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
# in bash, "&&" will execute sequentially ; "&" will execute simultaneously
# (("command 1") || (echo "command 1 failed")) && ((ssh mlgpu) || (echo "command 'ssh mlgpu' failed") && (echo "command 4"))

function echo_start_end () {
  while [[ "$#" -gt 0 ]]
  do
    #echo "**kwargs - {${1}: ${2}}"  # argparse and print
    case $1 in
        -s|--situation) situation="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
  done
  exe_time=`date +"%Y-%m-%d %H:%M:%S"`
  echo "==============================================================================================================="
  echo "user who runs this scrip: ${SUDO_USER:-${USER}}" # How do I find which user executes the script when is used sudo?
  echo "script: $(basename "$0"); execution_${situation}_time (UTC+8): ${exe_time}"
  echo "==============================================================================================================="
}

echo_start_end --situation "start"

## export paths to execute scripts
#export PYSPARK_DRIVER_PYTHON=/usr/bin/python3
#export SPARK_HOME=/opt/spark
#export HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop
#export LD_LIBRARY_PATH=/opt/hadoop/lib/native:$LD_LIBRARY_PATH
#source /etc/profile
#export PYSPARK_PYTHON=python3  # key part to make spark-submit work in this correct path
## ensure killing the failed process to get enough resources
#yarn application -list | awk '$2 == "grep_error_book" { print $1 }' | xargs yarn application -kill


#echo "HOME: ${HOME}"
#export PROJ_BASE_PATH="${HOME}/py_ds/tutor_python_project/bookmarks/GRE_prepare/GRE_vocab/MasonGRE_2000/quiz"
#echo "cd to this directory 'PROJ_BASE_PATH': ${PROJ_BASE_PATH}"
#cd "${PROJ_BASE_PATH}"  # key part to let my customized module be found in path when importing


# parse variables
while [[ "$#" -gt 0 ]]
  do
    echo "**kwargs - {${1}: ${2}}"  # argparse and print
    case $1 in
        -n|--n_practices) n_practices="$2"; shift ;;
        -d|--date_of_error_book) date_of_error_book="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
  done


main_start_time="$(date +%s)"; main_start_ts="$(date +"%Y-%m-%d %H:%M:%S")"

# mains
grep -e '^[a-z]' 'error_book_en.txt' | uniq | head -n ${n_practices} >> ${date_of_error_book}_errors_en_raw.csv

# finally
main_end_time="$(date +%s)"; main_end_ts="$(date +"%Y-%m-%d %H:%M:%S")"
main_elapsed_sec="$(( $main_end_time - $main_start_time ))"
main_elapsed_min="$(echo "scale=2; $main_elapsed_sec / 60" | bc )"
echo "Total elapsed time: ${main_elapsed_sec} (secs) (about ${main_elapsed_min} (mins)) - start: $main_start_ts, end: $main_end_ts (in local timezone, UTC+8)"

echo "Tasks are done successfully, system exit!"
echo_start_end --situation "end"






## sample commands
#bash scripts/grep_error_book.sh --n_practices 1 --date_of_error_book 20221005