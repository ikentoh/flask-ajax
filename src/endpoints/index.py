import base64
import os

from flask import render_template, request

from src.utils import blend


SRC_HEAD = 'data:image/png;base64,'

b64_left = str()
b64_right = str()


#
# トップページの表示
#


def register(app):

    @app.route(r'/', methods=['GET'])
    def index():
        """
        初期ページ
        """
        global b64_left
        global b64_right

        b64_left = get_image_b64('left.png')
        b64_right = get_image_b64('right.png')

        src_left = SRC_HEAD + b64_left
        src_right = SRC_HEAD + b64_right

        return render_template('index.html',
            src_left=src_left,
            src_right=src_right
        )


    @app.route(r'/blend', methods=['POST'])
    def get_blend():
        """
        blend画像を生成し、ajax通信に応じて返却する
        """
        blend_alpha = int(request.get_data()) / 100
        b64_blend = blend.generate(b64_left, b64_right, blend_alpha)

        src_blend = SRC_HEAD + b64_blend

        return src_blend


    def get_image_b64(filename):
        """
        static/img以下の画像ファイルをstr型のbase64で読み込む
        """
        image_dir = 'static/img/'

        with open(image_dir + filename, 'rb') as f:
            data = base64.b64encode(f.read())

        return data.decode('utf-8')
