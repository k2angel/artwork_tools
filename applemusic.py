import os
from io import BytesIO

import requests
import win32clipboard
from PIL import Image


def main(url):
    # 画像urlを取得
    res = requests.post(
        "https://clients.dodoapps.io/playlist-precis/playlist-artwork.php",
        data={"url": url},
    ).json()
    img_url = res["large"]
    print(img_url)
    # 画像をダウンロード
    img_res = requests.get(img_url)
    img = Image.open(BytesIO(img_res.content))
    # 画像を保存
    img.save(os.path.join(dir_, os.path.basename(img_url)))
    print("saved!")
    # 画像をクリップボードにコピー
    with BytesIO() as output:
        img.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()
    print("clipped!")


dir_ = "./img/applemusic"

if __name__ == "__main__":
    if not os.path.exists(dir_):
        os.makedirs(dir_)
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    while True:
        url = input("[URL] > ")
        main(url)
        print("")
