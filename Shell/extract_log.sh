#!/bin/bash

# 引数を格納
START_TIME=$1
STOP_TIME=$2

# 関数
# 引数チェック関数
function check_args(){
  if [ $# -ne 2 ]; then
    echo "Usage: $0 [start_time] [end_time]"
    echo "Ex: $0 \"12,30,9,0\" \"12,31,9,55\""
    exit 1
  fi
}

# 引数が数字かどうかを判定する関数
function is_number() {
  re='^[0-9]+$'
  if ! [[ $1 =~ $re ]]; then
    echo "Error: Argument '$1' is not a number" >&2
    exit 1
  fi
}

# 引数の桁数を判定する関数（時間）
function digit_check_time() {
  local digit=${#1}
  if [ $digit -gt 2 ]; then
    echo "Error: Argument '$1' has too many digits" >&2
    exit 1
  elif [ $digit -eq 1 ]; then
    echo "0$1"
  else
    echo "$1"
  fi
}

# 引数の桁数を判定する関数（日付）
function digit_check_date() {
  local digit=${#1}
  if [ $digit -gt 2 ]; then
    echo "Error: Argument '$1' has too many digits" >&2
    exit 1
  else
    echo "$1"
  fi
}

# 引数の範囲をチェックする関数
function range_check() {
  if [ $1 -lt 0 ] || [ $1 -gt 59 ]; then
    echo "Error: Argument '$1' is out of range (0-59)" >&2
    exit 1
  fi
}

# フォーマット変換関数
function convert_time_format() {
  local time_str="$1"
  IFS=',' read -ra time_arr <<< "$time_str"
  is_number ${time_arr[0]}
  month=$(LANG=en_US.UTF-8 date -d "${time_arr[0]}/1" +"%b")

  # 日付のフォーマットをチェック
  is_number ${time_arr[1]}
  day_tmp=$(digit_check_date ${time_arr[1]})
  if [ "x${day_tmp}" == "x" ]; then
    exit 3
  fi
  range_check ${day_tmp}
  day=${day_tmp}

  # 時間のフォーマットをチェック（時）
  is_number ${time_arr[2]}
  hour_tmp=$(digit_check_time ${time_arr[2]})
  if [ "x${hour_tmp}" == "x" ]; then
    exit 4
  fi
  range_check ${hour_tmp}
  hour=${hour_tmp}

  # 時間のフォーマットをチェック（分）
  is_number ${time_arr[3]}
  min_tmp=$(digit_check_time ${time_arr[3]})
  if [ "x${min_tmp}" == "x" ]; then
    exit 5
  fi
  range_check ${min_tmp}
  min=${min_tmp}

  echo "$month $day $hour:$min"
}

# 引数チェック
check_args ${START_TIME} ${STOP_TIME}

# 引数のフォーマット変換
start_time_formatted=$(convert_time_format "${START_TIME}")
ret=$?
# echo "ret = ${ret}"
if [ "${ret}" != "0" ]; then

  if [ "${ret}" == "3" ]; then
    echo "Error: invalid args 'day' : exit code ${ret}"
  elif [ ${ret} -eq 4 ]; then
    echo "Error: invalid args 'hour' : exit code ${ret}"
  elif [ ${ret} -eq 5 ]; then
    echo "Error: invalid args 'min' : exit code ${ret}"
  else
    echo "Error: Error occuered"
  fi

  echo "Error: func: start_time_formatted: convert_time_format : exit code ${ret}"
  exit 1
fi

end_time_formatted=$(convert_time_format "${STOP_TIME}")
ret=$?
# echo "ret = ${ret}"
if [ "${ret}" != "0" ]; then

  if [ "${ret}" == "3" ]; then
    echo "Error: invalid args 'day' : exit code ${ret}"
  elif [ ${ret} -eq 4 ]; then
    echo "Error: invalid args 'hour' : exit code ${ret}"
  elif [ ${ret} -eq 5 ]; then
    echo "Error: invalid args 'min' : exit code ${ret}"
  else
    echo "Error: Error occuered"
  fi

  echo "Error: func: end_time_formatted: convert_time_format : exit code ${ret}"
  exit 1
fi

echo "START TIME : ${start_time_formatted}"
echo "END TIME : ${end_time_formatted}"

# 必要な変数の初期化
log_dir="./log"
output_file="$log_dir/syslog.$(date +%Y%m%d%H%M%S).log"

# log_dirの作成
mkdir -p "$log_dir"
touch ${output_file}

# syslogファイルの検索
while read line; do
  log_time=$(echo "$line" | awk '{print $1" "$2" "$3}')
  if [ "$log_time" \< "$start_time_formatted" ] || [ "$log_time" \> "$end_time_formatted" ]; then
    continue
  fi

  # syslogに書き込み
  echo "$line" >> "$output_file"
done < /var/log/messages

