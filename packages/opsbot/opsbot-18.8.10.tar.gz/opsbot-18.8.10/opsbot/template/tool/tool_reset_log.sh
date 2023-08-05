
if [ -z "$2" ]; then
    echo "Missing Param"
    echo "Usage: resetlog <path> <max_size_in_byte>"
fi

path=$1
maximum_bytes=$2
echo "CHECK LOG FILE : $path"
echo "MAXIMUM SIZE ALOW: $maximum_bytes"

file_size=$(stat -c%s "$path")
echo "CURRENT SIZE: $file_size"

echo "------------"

if [ "$file_size" -le "$maximum_bytes" ]; then
    echo "Size < $maximum_bytes"
    echo "ACTION : Do Nothing"
    exit;
fi
echo "ACTION: REMOVE OLD BACKUP $path.bak"
rm "$path.bak"

echo "ACTION: BACKUP TO $path.bak"
cp $path "$path.bak"

echo "ACTION: WRITE EMPTY LOG"
echo "" > $path