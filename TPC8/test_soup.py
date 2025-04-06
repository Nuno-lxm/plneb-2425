from bs4 import BeautifulSoup
import requests, string, json


MAIN_URL = "https://www.atlasdasaude.pt"
dict = {}

def get_page(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    return soup

def detalhes_doenca(url):
    soup = get_page(url)

    div_content = soup.find("div", class_="node-doencas")
    div = div_content.find("div", class_="field-name-body").div.div

    res = {"Descricao": []}
    current_selection = "Descricao"

    for element in div:
        if element.name == "h2" and element.text.strip().lower() != "artigos relacionados":
            current_selection = element.text.strip()
            res[current_selection] = []
        
        elif element.name == "p" or element.name == "div":
            res[current_selection].append(element.text.strip())

        elif element.name == "ul":
            ul = []

            for li in element:
                if li.text.strip() != "":
                    ul.append(li.text.strip())

            res[current_selection].append(ul)
        
        elif element.name == "h3":
            current_selection = "Artigos Relacionados"

            if current_selection not in res:
                res[current_selection] = []
            
            res[current_selection].append(element.a["href"])

    site = div_content.find(class_="field-name-field-site")
    if site:
        res["site"] = site.find("div", class_="field-items").div.text.strip()

    nota = div_content.find(class_="field-name-field-nota")
    if nota:
        res["nota"] = nota.find("div", class_="field-items").div.text.strip()

    return res


def doencas_letra(letter):
    letter_url = MAIN_URL + "/doencasAaZ/" + letter
    soup = get_page(letter_url)
    tudo = soup.find_all(class_="views-row")

    for elem in tudo:
        ancora = elem.div.h3.a
        designacao = ancora.text.strip()
        resumo = elem.find("div", class_="views-field-body").div.text.strip().replace(" ", " ")

        url = MAIN_URL + ancora["href"]
        conteudo = detalhes_doenca(url)
        
        dict[designacao] = {"resumo" : resumo, "url" : url, "conteudo" : conteudo}
    
    return dict

res = {}

for letter in string.ascii_lowercase:
    print("Processing letter " + letter.upper())
    dict = doencas_letra(letter)
    res = res | dict

out_file = open("dict.json", "w", encoding="utf-8")
json.dump(res, out_file, ensure_ascii=False, indent=4)
out_file.close()