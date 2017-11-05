from flask import Flask, render_template, request, redirect, url_for, jsonify
import core.functions as sis500
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getData', methods=['GET','POST'])
def getData():
    if request.method == "POST":
        pergunta = request.form.get("pergunta")
        livro = request.form.get("livro")
        return json.dumps(sis500.run(pergunta,livro), ensure_ascii=False)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=8080, debug=True)