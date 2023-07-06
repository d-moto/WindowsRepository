import os
import openai
import requests

#openai.api_key = "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"
#openai.api_key = "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"
openai.api_key = "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"


def chat_with_gpt(prompt):
    # ChatGPTのAPIエンドポイント
    #url = 'https://api.openai.com/v1/engines/davinci-codex/completions'
    url = 'https://api.openai.com/v1/chat/completions'

    # APIにリクエストを送信
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        # model = "gpt-4",
        messages = [
            {"role": "system", "content": "The user appears to be particularly interested in physical mathematics. In particular, they have a considerable k interest in physics. He is considering writing and solving physics problems in python."},
            {"role": "assistant", "content": "you are python teacher"},
            {"role": "user", "content": prompt},
        ]
        # temperature = 1.5,
        # top_p = 1.0,
        #frequency_penalty = 2.0,
        #presence_penalty = 2.0
    )

    # レスポンスから応答テキストを取得
    response_text = response["choices"][0]["message"]["content"]

    # ログファイルに入力と応答を書き込む
    log_file = open('chatgpt_chat.log', 'a')
    log_file.write(f'入力: \n{prompt}\n\n')
    # log_file.write(f'出力: {response_text}\n')
    log_file.write('出力: ' + '\n' + response_text.encode('utf-8').decode('utf-8') + '\n\n')
    log_file.close()

    return response_text

# 対話の開始
while True:
    # ユーザーからの入力を受け取る
    user_input = input('> ')

    # ChatGPTによる応答生成の処理
    response = chat_with_gpt(user_input)

    # ChatGPTからの応答を表示する
    print(response)
