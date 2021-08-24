import os
import json
import site
from io import BytesIO

from flask import send_from_directory, request, render_template, abort, Markup, send_file
from flask import current_app as app

from trdg.generators import (
    GeneratorFromStrings,
)


site_packages = site.getsitepackages()[0]
font_dir = os.path.join(site_packages, 'trdg', 'fonts', 'latin')

@app.route('/')
def serve_index():
    return send_from_directory('../www/', 'home.html')

def ok(resp):
    return json.dumps(resp), 200, {'ContentType': 'application/json'}

@app.route('/image/<word>.jpg')
def image(word):
    generator = GeneratorFromStrings(
        [word],
        count=10,
        random_skew=True,
        text_color='#000000,#999999',
        distorsion_type=0,
        size=96
    )

    # for img, lbl in generator:
    #     print(type(img), type(lbl))
    #     print(img, lbl)
    #     print("\n")
    img = generator.next()[0]

    img_io = BytesIO()
    img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')
