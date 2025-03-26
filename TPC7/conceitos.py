from flask import Flask, request, render_template
from funcs import find
import json

db_file = open('conceitos.json', encoding='utf-8')
db = json.load(db_file)
db_file.close()

app = Flask(__name__)

@app.get('/')
def hello_world():
    return render_template("home.html")

@app.get('/conceitos')
def conceitos():
    designacoes = list(db.keys())
    return render_template('conceitos.html', designacoes=designacoes, title='Lista de Conceitos')

@app.get('/conceitos/<designacao>')
def conceito_detalhe(designacao):
    if designacao in db:
        return render_template('conceito_detalhes.html', designacao=designacao, descricao = db[designacao])

    return render_template('conceito_detalhes.html', designacao="Erro", descricao="Descrição não encontrada")

@app.get('/pesquisa')
def pesquisa():
    query = request.args.get('query')
    word_boundary = request.args.get('word_boundary') == 'on'
    match_case = request.args.get('match_case') == 'on'

    if not query:
        return render_template('pesquisa.html', title='Pesquisa')

    res = find(db, query, word_boundary, match_case)

    return render_template('pesquisa.html', conceitos=res, query=query, word_boundary=word_boundary, match_case=match_case, title='Pesquisa')

@app.get('/conceitos/tabela')
def conceitos_tabela():
    return render_template("tabela.html", conceitos=db)

@app.post('/conceitos')
def adicionar_conceito():
    descricao = request.form.get("descricao")
    designacao = request.form.get("designacao")
    
    db[designacao] = descricao
    f_out = open('conceitos_.json', 'w', encoding = 'utf-8')
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()

    designacoes = list(db.keys())
    return render_template('conceitos.html', designacoes=designacoes, title='Lista de Conceitos')
    
@app.delete("/conceitos/<designacao>")
def delete_conceito(designacao):
    if designacao in db:
        f_out = open("conceitos_.json", "w", encoding="utf-8")
        del db[designacao]
        json.dump(db, f_out, indent=4, ensure_ascii=False)
        f_out.close()
        return {"success": True, "message": "Conceito apagado com sucesso!", "redirect_url": "/conceitos"}

    return{"success": False, "message": "conceito não existe", "redirect_url": "/conceitos"}

@app.get('/api/conceitos')
def api_conceitos():
    return db

@app.get('/api/conceitos/<designacao>')
def api_conceito(designacao):
    return {'designacao': designacao, 'descricao': db[designacao]}


@app.post('/api/conceitos')
def adicionar_conceito_api():
    data = request.get_json()
    #{'designacao': '', 'descricao': ''}
    db[data['designacao']] = data['descricao']

    f_out = open('conceitos_.json', 'w', encoding = 'utf-8')
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()

    return data

app.run(host='0.0.0.0', port=4002, debug=True)