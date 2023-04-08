#!/bin/bash

# 1. 引数チェック
if [ $# -ne 2 ]; then
  echo "Usage: $0 [start_time] [end_time]"
  exit 1
fi

# 2. 必要な変数の初期化
start_time=$1
end_time=$2
log_dir="./log"
output_file="$log_dir/syslog.$(date +%Y%m%d%H%M%S).log"

# 3. log_dirの作成
mkdir -p $log_dir

# 4. syslogファイルの検索
while read line; do
  log_time=$(echo "$line" | awk '{print $1" "$2" "$3}')
  if [ "$log_time" \< "$start_time" ] || [ "$log_time" \> "$end_time" ]; then
    continue
  fi

  # syslogに書き込み
  echo "$line" >> $output_file
done < /var/log/messages

