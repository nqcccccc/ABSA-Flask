from flask import Flask, render_template, request
from flask_assets import Environment, Bundle

from phobert_absa import predict_qab

app = Flask(__name__)

assets = Environment(app)
assets.url = app.static_url_path
assets.debug = True

scss = Bundle('scss/main.scss', filters='pyscss', output='gen/all.css')
assets.register('scss_all', scss)

@app.route('/', methods=['GET'])
def index():
    return render_template('main.html')


@app.route('/result', methods=['POST'])
def result():
    text = request.form['text']
    result = predict_qab(text)
    return '---'.join(result)

# if __name__ == '__main__':
#     app.run(debug=True)