import psutil
from tabulate import tabulate


# プロセスのメモリ使用率を取得する関数
def get_memory_usage():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_percent']):
        # プロセス情報が取得できない場合はスキップ
        if not proc.info['memory_percent']:
            continue
        processes.append(proc.info)

    # メモリ使用率で降順にソート
    processes.sort(key=lambda x: x['memory_percent'], reverse=True)

    # 表示用のデータを作成
    data = [(p['name'], f"{p['memory_percent']:.2f}%") for p in processes]
    return data


# 表形式でメモリ使用率を表示
memory_usage_data = get_memory_usage()
print(tabulate(memory_usage_data, headers=['Process Name', 'Memory Usage']))
