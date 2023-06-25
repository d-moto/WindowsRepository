import json
import requests
import io
import base64
from PIL import Image, PngImagePlugin
import time

url = "http://127.0.0.1:7860"

prompt = "(RAW photo, masterpiece, 8k, best quality),\
          huge breasts, breasts cleavage,\
          looking at viewer, 18 years old,\
          extremely cute girl, (faint smile:1.1),\
          short bob, brown hair, (hands behind head:1.2), model,\
          extremely detailed baby face, extremely detailed, skin, extremely detailed legs,\
          armpits, Santa Claus costume,\
          outside,"

negative_prompt = "illustration,\
                   3d,\
                   sepia,\
                   painting,\
                   cartoons,\
                   sketch,\
                   (worst quality:2),\
                   ((monochrome)),\
                   ((grayscale:1.2)),\
                   (backlight:1.2),\
                   analog,\
                   analog photo,\
                   (bad hands, bad fingers, bad arms, bad legs, bad knees, bad navel:1.5),\
                   Shank Hair,\
                   (nipples:1.2), (muscle:1.1),\
                   (extra fingers, extra arms, extra legs, extra digit, fewer digits:1.5),\
                   text, signature, missing limb, missing fingers,"

loop = 1
seed = 100
start_time = time.time() # スクリプトの開始時間

# スクリプトの実行回数の記録
try:
    with open("C:/Users/mokos/Stable_Diffusion/sd.webui/webui/outputs/api_output/script_counter.txt", "r") as file:
        counter = int(file.read().strip()) + 1
except FileNotFoundError:
    counter = 0

# スクリプトの実行回数を追記する
with open("C:/Users/mokos/Stable_Diffusion/sd.webui/webui/outputs/api_output/script_counter.txt", "w") as file:
    file.write(str(counter))

for c in range(loop):

    payload = {
        "sd_model_checkpoint": "BRAV5finalfp16.safetensors",
        "enable_hr": False,
        "denoising_strength": 0.4,
        "hr_scale": 2,
        "hr_upscaler": "LDSR",
        "prompt": prompt,
        "steps": 40,
        "seed": seed,
        "width": 540,
        "height": 960,
        "negative_prompt": negative_prompt,
        "sampler_index": "DPM++ SDE Karras"
    }

    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)

    r = response.json()

    for i in r['images']:
        image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))

        png_payload = {
            "image": "data:image/png;base64," + i
        }
        response2 = requests.post(url=f'{url}/sdapi/v1/png-info', json=png_payload)

        pnginfo = PngImagePlugin.PngInfo()
        pnginfo.add_text("parameters", response2.json().get("info"))
        image.save(f'C:/Users/mokos/Stable_Diffusion/sd.webui/webui/outputs/api_output/{counter}-{c + 1}.png', pnginfo=pnginfo)

        # seed値に1を加えてループを終了
        seed = c + 1 

end_time = time.time() # 終了時間の記録
execution_time = end_time - start_time # 実行時間計算
print(f"start_time : {start_time} s")
print(f"end_time : {end_time} s")
print(f"Execution_time : {execution_time} s")
# import webuiapi

# api = webuiapi.WebUIApi(host='127.0.0.1', port=7860, sampler='DPM++ SDE Karras', steps=40)

# result1 = api.txt2img(prompt="cute squirrel",
#                       negative_prompt="ugly, out of frame",
#                       seed=-1,
#                       styles=["anime"],
#                       cfg_scale=7,
#                       sampler_index='DDIM',
#                       steps=30,
#                       enable_hr=True,
#                       hr_scale=2,
#                       hr_upscaler=webuiapi.HiResUpscaler.LDSR,
#                       hr_second_pass_steps=20,
#                       denoising_strength=0.4
#                       )
# result2 = api.txt2img(prompt="cute squirrel",
#                       negative_prompt="ugly, out of frame",
#                       seed=-1,
#                       styles=["anime"],
#                       cfg_scale=7,
#                       sampler_index='DDIM',
#                       steps=30,
#                       enable_hr=True,
#                       hr_scale=2,
#                       hr_upscaler=webuiapi.HiResUpscaler.LDSR,
#                       hr_second_pass_steps=20,
#                       denoising_strength=0.4
#                       )

# print(result1.images)
# result1.image
# print(result1.info)
# print(result1.parameters)
# result1.image.save('output1.png')
# result2.image.save('output2.png')

## payload
# {
#   "enable_hr": false,
#   "denoising_strength": 0,
#   "firstphase_width": 0,
#   "firstphase_height": 0,
#   "hr_scale": 2,
#   "hr_upscaler": "string",
#   "hr_second_pass_steps": 0,
#   "hr_resize_x": 0,
#   "hr_resize_y": 0,
#   "hr_sampler_name": "string",
#   "hr_prompt": "",
#   "hr_negative_prompt": "",
#   "prompt": "",
#   "styles": [
#     "string"
#   ],
#   "seed": -1,
#   "subseed": -1,
#   "subseed_strength": 0,
#   "seed_resize_from_h": -1,
#   "seed_resize_from_w": -1,
#   "sampler_name": "string",
#   "batch_size": 1,
#   "n_iter": 1,
#   "steps": 50,
#   "cfg_scale": 7,
#   "width": 512,
#   "height": 512,
#   "restore_faces": false,
#   "tiling": false,
#   "do_not_save_samples": false,
#   "do_not_save_grid": false,
#   "negative_prompt": "string",
#   "eta": 0,
#   "s_min_uncond": 0,
#   "s_churn": 0,
#   "s_tmax": 0,
#   "s_tmin": 0,
#   "s_noise": 1,
#   "override_settings": {},
#   "override_settings_restore_afterwards": true,
#   "script_args": [],
#   "sampler_index": "Euler",
#   "script_name": "string",
#   "send_images": true,
#   "save_images": false,
#   "alwayson_scripts": {}
# }

