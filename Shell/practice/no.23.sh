#!/bin/bash

# 数値の配列
array=(19 2 55 98.4 5 36 7 98 5.9 444)

# 配列の個数
array_length=${#array[@]}

# 配列を昇順にソート
sorted_array=($(echo ${array[@]} | tr ' ' '\n' | sort -n | tr '\n' ' '))

# 中央値計算
if [ $((array_length % 2)) -eq 0 ]; then
    # 要素数が偶数の場合は、中央に位置する2つの要素の平均値を求める
    index1=$((array_length / 2 - 1))
    index2=$((array_length / 2))
    median=$(echo "scale=1;(${sorted_array[$index1]} + ${sorted_array[$index2]}) / 2" | bc)
else
    # 要素数が奇数の場合は、中央に位置する要素を求める
    index=$((array_length / 2))
    median=${sorted_array[$index]}
fi

# 結果
echo "中央値は $median です。"
    