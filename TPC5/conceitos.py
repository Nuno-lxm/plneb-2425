from flask import Flask, request, render_template
import json

db_file = open('conceitos_.json', encoding='utf-8')
db = json.load(db_file)
db_file.close()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>Hello, World!</p>'

@app.route('/conceitos')
def conceitos():
    designacoes = list(db.keys())
    return render_template('conceitos.html', designacoes=designacoes, title='Lista de Conceitos')

@app.route('/conceitos/<designacao>')
def conceito_detalhe(designacao):
    descricao = db[designacao]
    return render_template('conceito_detalhes.html', designacao=designacao, descricao=descricao)

@app.post('/conceitos')
def adicionar_conceito():
    data = request.get_json()
    #{'designacao': '', 'descricao': ''}
    db[data['designacao']] = data['descricao']

    f_out = open('conceitos_.json', 'w', encoding = 'utf-8')
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()

    return data


@app.route('/api/conceitos')
def api_conceitos():
    return db

@app.route('/api/conceitos/<designacao>')
def api_conceito(designacao):
    return {'designacao': designacao, 'descricao': db[designacao]}

app.run(host='localhost', port=4002, debug=True)
