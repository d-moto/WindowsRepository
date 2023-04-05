import os
import openai
import requests

openai.api_key = "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"

def chat_with_gpt(prompt_img):
    # ChatGPTのAPIエンドポイント
    url = 'https://api.openai.com/v1/chat/images/generations'

    response_img = openai.Image.create(
        prompt = prompt_img,
        n=5,
        size="1024x1024"
    )

    # レスポンスから応答テキストを取得
    image_url = []
    n = 0

    for i in range(10):
        try:
            image_url.append(response_img['data'][i]['url'])
            if isinstance(image_url[i], str):
                n = n + 1
                print('"url_' + str(n) + '"')
                print("")
                print(image_url[i])
                print("")

                # ログファイルに入力と応答を書き込む
                log_file = open('image_url.log', 'a')
                log_file.write(f'URL: {image_url[i]}\n')
                log_file.write(f'\n')
                log_file.close()

        except IndexError as ex:
            print("No such No." + str(i + 1) + " picture : {}".format(ex))
        else:
            print("")
        
        
    
    print("")
    print(n, "pictures", "created")

    return image_url

# 対話の開始
while True:
    # ユーザーからの入力を受け取る
    user_input = input('> ')

    # ChatGPTによる応答生成の処理
    response = chat_with_gpt(user_input)

    # ChatGPTからの応答を表示する
    # print(response)
    print("")
