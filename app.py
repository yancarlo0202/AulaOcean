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

@app.route('/')
def exibir_entradas():
    entradas = post
    return render_template('exibir_entrada.hmtl', entradas=entradas)


@app.route('/login')
def login():
    returnrender_template('login.html')