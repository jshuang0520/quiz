#shopt -s globstar
#for f in /Users/johnson.huang/Desktop/screenshots/copy_口說課前; do
arr=$(find /Users/johnson.huang/Desktop/screenshots/copy_口說課前 -name "*.png" -or -name '*.jpg' -type f | while read LINE; do echo "$LINE" ; done | rev | cut -d"/" -f1 <<< "$LINE" | rev)
for file in $arr; do
  echo "$file is a screenshot";
done
# to rename mac screenshot pattern
# pattern: Screen Shot 2022-11-20 at 12.56.18 PM.png
for file in */ .*/ ; do
  echo "$file is a directory";

  for i in "Screen Shot"*.png; do
      meta=$(cut -d" " -f3 <<< "$i")
      year=$(echo "${meta}" | awk -F '-' '{printf $1}')
      month=$(echo "${meta}" | awk -F '-' '{printf $2}')
      date=$(echo "${meta}" | awk -F '-' '{printf $3}')
      meta=$(cut -d" " -f5 <<< "$i")
      hour=$(echo "${meta}" | awk -F '.' '{printf $1}')
      minute=$(echo "${meta}" | awk -F '.' '{printf $2}')
      second=$(echo "${meta}" | awk -F '.' '{printf $3}')
      meta=$(cut -d" " -f6 <<< "$i")
      if [[ $meta == "PM.png" ]]; then
        if [[ ${hour} == 12 ]]; then
          hour="$(( ${hour} + 0))"
        else
          hour="$(( ${hour} + 12))"  # 12
        fi
      fi
      # hour=$(echo "${hour}" | awk 'printf $1')
      hour=$(printf '%02d' ${hour})
      minute=$(printf '%02d' ${minute})
      second=$(printf '%02d' ${second})
      new=`echo "${year}-${month}-${date}_${hour}_${minute}_${second}.jpg"`
      echo "new: $new"
      mv "$i" $new
  done
done