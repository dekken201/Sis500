from flask import Flask, render_template, request, redirect, url_for
import core.functions as sis500

app = Flask(__name__)
resposta = {"resposta":""}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getData', methods=['GET','POST'])
def getData():
    if request.method == "POST":
        pergunta = request.form.get("data")
        global resposta
        resposta["resposta"] = sis500.run(pergunta, "algodao")
        return resposta["resposta"]
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(port=8080, debug=True)