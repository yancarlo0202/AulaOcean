from flask import Flask, render_template

#app = Flask("meu app")

#@app.route('/')
#def hello():
#    return "Hello Yan!"

post = [
    {
        "título": "Minha primeira postagem",
        "texto": "teste"
    },

    {
        "título": "Minha segunda postagem",
        "texto": "teste"
    }
]

app = Flask(__name__)

@app.route('/')
def exibir_entradas():
    entradas = post
    return render_template('exibir_entrada.hmtl', entradas=entradas)


#@app.route('/novo')
#def novo():
#    return "<h1>Nova página</h1>"