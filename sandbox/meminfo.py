import psutil
import GPUtil
import time


def get_memory_usage():
    mem = psutil.virtual_memory()
    return mem.used / 1024**3  # メモリ使用量をGB単位で返す


def get_gpu_memory_usage():
    gpus = GPUtil.getGPUs()
    if len(gpus) == 0:
        return 0
    gpu = gpus[0]  # 最初のGPUの使用量を取得する
    return gpu.memoryUsed / 1024  # VRAM使用量をGB単位で返す


def monitor_python_processes(interval, log_file):
    while True:
        # 全てのプロセスを取得
        processes = psutil.process_iter(['pid', 'name', 'cmdline', 'cpu_percent', 'memory_percent'])

        # Pythonに関連するプロセスのみを抽出して表示
        python_processes = [process for process in processes if process.info['cmdline'] == ['python', 'launch.py']]
        with open(log_file, 'a') as f:
            f.write('Process Monitoring Log\n')
            f.write('----------------------\n')
            for process in python_processes:
                f.write(f"PID: {process.info['pid']}\n")
                f.write(f"Name: {process.info['name']}\n")
                f.write(f"Command Line: {' '.join(process.info['cmdline'])}\n")
                f.write(f"CPU Percent: {process.info['cpu_percent']}%\n")
                f.write(f"Memory Percent: {process.info['memory_percent']}%\n")
                f.write("---------------------------\n")

            # memory_usage = get_memory_usage()
            gpu_memory_usage = get_gpu_memory_usage()
            # print(f"Memory Usage: {memory_usage:.2f} GB")
            f.write(f"GPU Memory Usage: {gpu_memory_usage:.2f} GB\n")
            f.write("print end\n")
            f.write("\n")

            time.sleep(interval)


while True:
    log_file = 'process_monitoring.log'  # ログファイルのパス
    monitor_python_processes(5, log_file)  # 監視する間隔（秒）とログファイルのパス
    time.sleep(0)
