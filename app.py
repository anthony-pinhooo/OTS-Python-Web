from flask import Flask, render_template

app = Flask("meu app")

#Mock para Teste
posts = [
    {
        "titulo": "Minha primeira postagem",
        "texto": "Era uma casa muito engraça, não tinha teto, não tinha nada"
    },
    {
        "titulo": "Segundo Post",
        "texto": "Vai Neymar, tu gosta de bater né, tu é cachorro"
    }
]



@app.route("/")
def exibir_entradas():
    entradas = posts
    #importando o template html
    return render_template('exibir_entradas.html', entradas=entradas)