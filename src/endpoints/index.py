import base64
import os

from flask import render_template, request

from src.utils import blend


SRC_HEAD = 'data:image/png;base64,'


#
# SSポップアップ
#


def register(app):

    @app.route(r'/', methods=['GET'])
    def index():
        """
        初期ページ
        """
        b64_left = get_image_b64('left.png')
        b64_right = get_image_b64('right.png')

        src_left = SRC_HEAD + b64_left
        src_right = SRC_HEAD + b64_right

        return render_template('index.html',
            src_left=src_left,
            src_right=src_right
        )


    def get_image_b64(filename):
        """
        static/img以下の画像ファイルをstr型のbase64で読み込む
        """
        image_dir = 'static/img/'

        with open(image_dir + filename, 'rb') as f:
            data = base64.b64encode(f.read())

        return data.decode('utf-8')
