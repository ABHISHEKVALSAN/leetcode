TIME=$1
EASY_COUNT=0
MEDIUM_COUNT=0
HARD_COUNT=0
TOTAL=0
EASY_STRING="<h3>Easy</h3>"
MEDIUM_STRING="<h3>Medium</h3>"
HARD_STRING="<h3>Hard</h3>"

for folder in $(ls | grep -E "[0-9]{4}");
do
  #echo $folder/README.md;
  file_creation_time=$(git log --follow --format=%ad --date default $folder/README.md| tail -n 1)
  if [[ "$file_creation_time" == *"$TIME"* ]]; then
    first_line=$(head -n 1 "$folder/README.md")
    if [[ "$first_line" == *"$EASY_STRING"* ]]; then
      ((EASY_COUNT++))
    fi
    if [[ "$first_line" == *"$MEDIUM_STRING"* ]]; then
      ((MEDIUM_COUNT++))
    fi
    if [[ "$first_line" == *"$HARD_STRING"* ]]; then
      ((HARD_COUNT++))
    fi
    ((TOTAL++))
  fi
done;
echo "$EASY_COUNT $MEDIUM_COUNT $HARD_COUNT $TOTAL"
