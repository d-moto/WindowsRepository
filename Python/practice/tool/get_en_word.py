import time
import sched
import datetime as dt
from PyDictionary import PyDictionary
from wordnik import swagger, WordApi

# Wordnik API情報
apiUrl = 'http://api.wordnik.com/v4'
apiKey = 'YOUR_WORDNIK_API_KEY'  # ここにWordnikのAPIキーを入力してください。
client = swagger.ApiClient(apiKey, apiUrl)
wordApi = WordApi.WordApi(client)

# PyDictionaryのインスタンスを作成
dictionary=PyDictionary()

# schedのインスタンスを作成
s = sched.scheduler(time.time, time.sleep)

def get_and_log_word_info():
    # Wordnikからランダムに単語を取得
    word = wordApi.getRandomWord()

    # 単語の意味、同義語、反意語を取得
    meaning = dictionary.meaning(word.word)
    synonym = dictionary.synonym(word.word)
    antonym = dictionary.antonym(word.word)
    
    # 現在の日付と時間を取得
    now = dt.datetime.now()
    
    # ログファイルに書き出し
    with open("word_info_log.txt", "a") as f:
        f.write(f"\n{now}\n")
        f.write(f"Word: {word.word}\n")
        f.write(f"Meaning: {meaning}\n")
        f.write(f"Synonym: {synonym}\n")
        f.write(f"Antonym: {antonym}\n")

def schedule_next_run(sc): 
    # 次の日の9時を取得
    tomorrow = dt.datetime.now() + dt.timedelta(days=1)
    next_run = dt.datetime(tomorrow.year, tomorrow.month, tomorrow.day, 9, 0, 0)
    
    # 次の実行までの秒数を計算
    time_to_next_run = (next_run - dt.datetime.now()).total_seconds()

    # 関数をスケジュール
    s.enter(time_to_next_run, 1, get_and_log_word_info, argument=())
    s.run()

# 最初の実行
get_and_log_word_info()

# 次の実行をスケジュール
schedule_next_run(s)
