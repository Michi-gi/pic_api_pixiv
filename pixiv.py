""" api for Pixiv """
import os
import mimetypes
import json

from flask import Flask, send_file
from flask import request

from pixivpy3 import AppPixivAPI

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

image_path = os.getenv("IMAGE_DIR")
refresh_token = os.getenv("REFRESH_TOKEN")

pixiv_app = AppPixivAPI()

def login():
    """ login """
    pixiv_app.auth(refresh_token=refresh_token)

login()

@app.route('/pic/<pic_id>')
def get_pic_profile(pic_id):
    """ get pic profile """
    print(pic_id)
    picture_detail = pixiv_app.illust_detail(pic_id)
    if "error" in picture_detail:
        print(picture_detail["error"])
        if "OAuth" in picture_detail["error"]["message"]:
            print("error. relogin.")
            login()
            picture_detail = pixiv_app.illust_detail(pic_id)

    print(picture_detail)
    return picture_detail

@app.route('/author/<author_id>')
def get_author_profile(author_id):
    """ get author profile """
    author_detail = pixiv_app.user_detail(author_id)
    if "error" in author_detail:
        if "OAuth" in author_detail["error"]["message"]:
            print("error. relogin.")
            login()
            author_detail = pixiv_app.user_detail(author_id)

    print(author_detail)
    return author_detail

@app.route('/author/<author_id>/pics')
def get_pics_of_author(author_id):
    """ get pics specified author ID """
    page_str = request.args.get("page")
    page = int(page_str) if page_str is not None else 1
    off = (page - 1) * 30
    pics = pixiv_app.user_illusts(author_id, offset=off)
    if "error" in pics:
        if "OAuth" in pics["error"]["message"]:
            print("error. relogin.")
            login()
            pics = pixiv_app.user_illusts(author_id, offset=off)

    print(pics)
    return pics

@app.route('/download')
def download():
    """ download pic """
    url = request.args.get("page")
    print(f"url: {url}")
    filename = os.path.basename(url)
    filePath = image_path + "/" + filename
    if not os.path.exists(filePath):
        print(f"download to {filePath}")
        pixiv_app.download(url, path=image_path)
    else:
        print(f"found {filePath}")

    return send_file(filePath, mimetype=mimetypes.guess_type(url)[0])

if __name__ == "__main__":
    app.run(debug = True)
