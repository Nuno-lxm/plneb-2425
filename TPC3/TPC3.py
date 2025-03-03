import re

def limpa_descricao(descricao):
    descricao = descricao.strip()
    descricao = re.sub(r"\n", " ", descricao)
    return descricao


file = open("data/dicionario_medico.txt", encoding="utf-8")
texto = file.read()
file.close()


texto = re.sub(r"\f(?=[a-zØ-öø-ÿ])", "", texto)
texto = re.sub(r"\n\f", "", texto)


texto = re.sub(r"\n\n", "\n@", texto)


conceitos = re.findall(r"@(.*)\n([^@]*)", texto)
result = [(designacao, limpa_descricao(descricao)) for designacao, descricao in conceitos]


html = """
<!DOCTYPE html>
    <body>
    <h3>Dicionário de Conceitos Médicos</h3>
    <p> Este dicionário foi desenvolvido para a aula de PLNEB 2024/2025<p>"""

for designacao, descricao in result:
    html +=  f"""
        <div>
        <p><b>{designacao}</b></p>
        <p>{descricao}</p>
        </div>
        <hr/>
    """

html += """
        </div>
    </body>
</html>
"""

html_file = open("output.html", "w", encoding="utf-8")
html_file.write(html)
html_file.close()