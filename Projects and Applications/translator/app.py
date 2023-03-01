from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from langdetect import detect
from PIL import Image
import pytesseract
import argostranslate.package
import argostranslate.translate
from libretranslatepy import LibreTranslateAPI

app = Flask(__name__)

cors = CORS(app, resources={r"/translate_text": {"origins": "*"}})
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

def translate(text, lang):
    argostranslate.package.update_package_index()
    available_packages = argostranslate.package.get_available_packages()
    
    lang_from = detect(text)
    package_to_install = next(filter(lambda x: x.from_code == detect(text) and x.to_code == lang, available_packages))
    argostranslate.package.install_from_path(package_to_install.download())
    
    return argostranslate.translate.translate(text, lang_from, lang)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate_text', methods=['POST'])
def translate_text():
    text = str(request.form['data'])
    lang = str(request.form['lang'])
    
    result = {
        "output": translate(text, lang)
    }
    return jsonify(result), 200, {'Access-Control-Allow-Origin': '*'}

@app.route('/translate_img', methods=['POST'])
def translate_img():
    image_file = request.files['file']
    image = Image.open(image_file)
    text = str(pytesseract.image_to_string(image.convert('L'))).strip()
    print(text)
    lang = str(request.form['lang'])
    print(translate(text, lang))
    result = {
        "output": translate(text, lang)
    }
    print(result)
    return jsonify(result), 200, {'Access-Control-Allow-Origin': '*'}

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3001)