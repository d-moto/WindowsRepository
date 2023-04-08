#!/bin/bash

# 引数チェック
if [ $# -ne 2 ]; then
  echo "Usage: $0 [start_time] [end_time]"
  exit 1
fi

# フォーマット変換関数
function convert_time_format() {
  local time_str="$1"
  IFS=',' read -ra time_arr <<< "$time_str"
  month=$(LANG=en_US.UTF-8 date -d "${time_arr[0]}/1" +"%b")
  day=${time_arr[1]}
  hour=$(printf "%02d" ${time_arr[2]})
  min=$(printf "%02d" ${time_arr[3]})
  echo "$month $day $hour:$min"
}

# 引数のフォーマット変換
start_time_formatted=$(convert_time_format "$1")
end_time_formatted=$(convert_time_format "$2")

# 必要な変数の初期化
log_dir="./log"
output_file="$log_dir/syslog.$(date +%Y%m%d%H%M%S).log"

# log_dirの作成
mkdir -p "$log_dir"

# syslogファイルの検索
while read line; do
  log_time=$(echo "$line" | awk '{print $1" "$2" "$3}')
  if [ "$log_time" \< "$start_time_formatted" ] || [ "$log_time" \> "$end_time_formatted" ]; then
    continue
  fi

  # syslogに書き込み
  echo "$line" >> "$output_file"
done < /var/log/messages

