# pic_api_pixiv
これは[pic_api](https://github.com/Michi-gi/pic_api)から呼び出されること前提の、Pixiv APIアクセス用のAPIです。基本的に[PythonのPixiv API](https://github.com/upbit/pixivpy)を呼び出すエンドポイントを提供しているだけです。

## 利用方法
ターミナルから下記のようにPythonのライブラリーをインストールします。必要に応じて仮想環境を用意してください。

```
pip install gppt
pip install pixivpy
pip install Flask
pip install gunicorn
```
下記の環境変数を指定してください。
｜変数|説明|
|---|---|
|IMAGE_DIR|画像キャッシュ用ディレクトリー|
|REFRESH_TOKEN|認証用REFRESH TOKEN|

※REFRESH TOKENの取得方法は https://gist.github.com/ZipFile/c9ebedb224406f4f11845ab700124362 を参照。

これが終われば次のコマンドで実行してください。
```
gunicorn --bind=0.0.0.0:5000 pixiv:app
```
## 利用ライブラリー
- Flask
- gunicorn
- [pixivpy](https://github.com/upbit/pixivpy)
- [get-pixivpy-token](https://github.com/eggplants/get-pixivpy-token)