#!/bin/bash

# 引数を格納
START_TIME=$1
END_TIME=$2

## 関数
# 引数の数チェック関数
function check_args(){
  if [ $# -ne 2 ]; then
    echo "Usage: $0 [start_time] [end_time]"
    echo "Ex: $0 \"12,30,9,0\" \"12,31,9,55\""
    exit 10
  fi
}

# 引数を分割
function split_arg(){
  time_str_s="${START_TIME}"
  time_str_e="${END_TIME}"
  IFS=',' read -ra time_arr_s <<< "${time_str_s}"
  IFS=',' read -ra time_arr_e <<< "${time_str_e}"
}

# 引数が数字かどうかを判定する関数
function is_number() {
  re='^[0-9]+$'
  if ! [[ $1 =~ $re ]]; then
    echo "Error: Argument '$1' is not a number" >&2
    exit 20
  fi
}

# 数字で指定されたmonthを文字に変換
function convert_mon() {
  month_s=$(LANG=C date -d "${time_arr_s[0]}/1" +"%b")
  ret=$?
  if [ ${ret} -ne 0 ]; then
    echo "Error: Argument ${time_arr_s[0]} is invalid month with code ${ret}"
    exit 31
  fi
  month_e=$(LANG=C date -d "${time_arr_e[0]}/1" +"%b")
  ret=$?
  if [ ${ret} -ne 0 ]; then
    echo "Error: Argument ${time_arr_e[0]} is invalid month with code ${ret}"
    exit 32
  fi
  echo ${month_s}
  echo ${month_e}
}

# 引数の桁数を判定する関数（DAY）
function digit_check_date() {
  digit=${#1}
  date_num=$1
  if [ ${digit} -eq 1 ]; then
    echo ${date_num}
  elif [ ${digit} -eq 2 ]; then
    date_num1=${date_num:0:1}
    date_num2=${date_num:1:1}
    if [ ${date_num1} -eq 0 ]; then
      echo ${date_num2}
    else
      echo ${date_num}
    fi
  else
    echo "Error: Argument '$1' has too many digits" >&2
    exit 80
  fi
}

# 数字で指定されたdayを変換する関数（DAY）
function convert_day() {
  day_s=$(digit_check_date ${time_arr_s[1]})
  ret=$?
  if [ ${ret} -eq 80 ]; then
    echo "exit 80"
    exit 80
  fi

  day_e=$(digit_check_date ${time_arr_e[1]})
  ret=$?
  if [ ${ret} -eq 80 ]; then
    echo "exit 80"
    exit 80
  fi

  echo ${day_s}
  echo ${day_e}
}

## 引数の桁数を判定する関数（HOUR・MIN）
function digit_check_time() {
  local digit=${#1}
  if [ $digit -gt 2 ]; then
    echo "Error: Argument '$1' has too many digits" >&2
    exit 70
  elif [ $digit -eq 1 ]; then
    echo "0$1"
  else
    echo "$1"
  fi
}

# 引数の範囲をチェックする関数（HOUR）
function range_check_h() {
  if [ $1 -lt 0 ] || [ $1 -gt 24 ]; then
    echo "Error: Argument '$1' is out of range (0-24)" >&2
    exit 51
  fi
}

# 引数の範囲をチェックする関数（MINUTES）
function range_check_m() {
  if [ $1 -lt 0 ] || [ $1 -gt 59 ]; then
    echo "Error: Argument '$1' is out of range (0-59)" >&2
    exit 52
  fi
}

# フォーマット変換関数
# function convert_time_format() {
#   # 日付のフォーマットをチェック（月）
#   local time_str="$1"
#   IFS=',' read -ra time_arr <<< "$time_str"
#   is_number ${time_arr[0]}
#   month=$(LANG=en_US.UTF-8 date -d "${time_arr[0]}/1" +"%b")
#   ret="$?"
#   if [ ${ret} -ne 0 ]; then
#     echo "Error: date command failed with exit code ${ret}." >&2
#     exit 10
#   fi

#   # 日付のフォーマットをチェック（日）
#   is_number ${time_arr[1]}
#   #day_tmp=$(digit_check_date ${time_arr[1]})
#   digit_check_date ${time_arr[1]}
#   if [ "x${day_tmp}" == "x" ]; then
#     exit 20
#   fi
#   range_check ${day_tmp}
#   day=${day_tmp}

#   # 時間のフォーマットをチェック（時）
#   is_number ${time_arr[2]}
#   hour_tmp=$(digit_check_time ${time_arr[2]})
#   if [ "x${hour_tmp}" == "x" ]; then
#     exit 30
#   fi
#   range_check ${hour_tmp}
#   hour=${hour_tmp}

#   # 時間のフォーマットをチェック（分）
#   is_number ${time_arr[3]}
#   min_tmp=$(digit_check_time ${time_arr[3]})
#   if [ "x${min_tmp}" == "x" ]; then
#     exit 40
#   fi
#   range_check ${min_tmp}
#   min=${min_tmp}

#   echo "$month $day $hour:$min"
# }

## MAIN
# 引数の数チェック
check_args ${START_TIME} ${END_TIME}

# 引数を分割
split_arg

# 引数が数値かどうかを判定
for i in {0..3}; do
  is_number ${time_arr_s[i]}
  is_number ${time_arr_e[i]}
done

# それぞれの値が適切かを判定
# monthに当たる数値の判定
convert_mon

# dayに当たる数値の判定
convert_day

# hour / minutes に当たる数値の判定
range_check_h ${time_arr_s[2]}
range_check_h ${time_arr_e[2]}
range_check_m ${time_arr_s[3]}
range_check_m ${time_arr_e[3]}
hour_s=$(digit_check_time ${time_arr_s[2]})
hour_e=$(digit_check_time ${time_arr_e[2]})
min_s=$(digit_check_time ${time_arr_s[3]})
min_e=$(digit_check_time ${time_arr_e[3]})

start_time_formatted="${month_s} ${day_s} ${hour_s}:${min_s}"
end_time_formatted="${month_e} ${day_e} ${hour_e}:${min_e}"
#echo "${start_time_formatted}"
#echo "${end_time_formatted}"




# 引数のフォーマット変換
# start_time_formatted=$(convert_time_format "${START_TIME}")
# ret=$?
# # echo "ret = ${ret}"
# if [ "${ret}" != "0" ]; then

#   # if [ "${ret}" == "3" ]; then
#   #   echo "Error: invalid args 'day' : exit code ${ret}"
#   # elif [ ${ret} -eq 4 ]; then
#   #   echo "Error: invalid args 'hour' : exit code ${ret}"
#   # elif [ ${ret} -eq 5 ]; then
#   #   echo "Error: invalid args 'min' : exit code ${ret}"
#   # else
#   #   echo "Error: Error occuered"
#   # fi

#   echo "Error: func: start_time_formatted: convert_time_format : exit code ${ret}"
#   exit 1
# fi

# end_time_formatted=$(convert_time_format "${STOP_TIME}")
# ret=$?
# # echo "ret = ${ret}"
# if [ "${ret}" != "0" ]; then

#   # if [ "${ret}" == "3" ]; then
#   #   echo "Error: invalid args 'day' : exit code ${ret}"
#   # elif [ ${ret} -eq 4 ]; then
#   #   echo "Error: invalid args 'hour' : exit code ${ret}"
#   # elif [ ${ret} -eq 5 ]; then
#   #   echo "Error: invalid args 'min' : exit code ${ret}"
#   # else
#   #   echo "Error: Error occuered"
#   # fi

#   echo "Error: func: end_time_formatted: convert_time_format : exit code ${ret}"
#   exit 1
# fi

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

