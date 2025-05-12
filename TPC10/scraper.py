from bs4 import BeautifulSoup
import requests, json

MAIN_URL = "https://revista.spmi.pt/index.php/rpmi/issue/archive"
dict = {}

def get_page(url):
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')

    return soup

def get_issue_urls(soup):
    issue_urls = []

    ul = soup.find("ul", class_="issues_archive")
    for li in ul.find_all("li"):
        a = li.find("a", class_="title")
        if a and a.get("href"):
            issue_urls.append(a["href"])

    return issue_urls

def get_article_urls(soup):
    article_urls = []
    sections = soup.find_all("div", class_="section")
    for section in sections:
        if section.h2.text.strip() in ["Editorial", "Imagens em Medicina"]:
            print("Skipping section:", section.h2.text.strip())
            continue
        else:
            print("Processing section:", section.h2.text.strip())
        
        ul = section.find("ul", class_="cmp_article_list articles")
        h3_list = ul.find_all("h3", class_="title")
        for h3 in h3_list:
            url = h3.a["href"]
            article_urls.append(url)

    return article_urls

def get_authors(section):
    authors = []
    for li in section.find_all("li"):
        name = li.find("span", class_="name")
        affiliation = li.find("span", class_="affiliation")
        orcid = li.find("span", class_="orcid")
        
        author = {
            "name": name.text.strip() if name else None,
            "affiliation": affiliation.text.strip() if affiliation else None,
            "orcid": orcid.text.strip() if orcid else None
        }
        
        if author["name"]:
            authors.append(author)

    return authors

def get_article_details(soup):
    article = {}
    title = soup.find("h1", class_="page_title")
    title = title.text.strip()

    abstract = soup.find("section", class_="item abstract")
    article["abstract"] = abstract.text.strip().replace("Abstract\n", "").replace("\n", " ") if abstract else None

    doi_section = soup.find("section", class_="item doi")
    doi = doi_section.find("a")["href"] if doi_section else None
    article["doi"] = doi

    keywords_section = soup.find("section", class_="item keywords")
    keywords = keywords_section.span.text.strip().replace("\t", "") if keywords_section else None
    article["keywords"] = keywords

    date_div = soup.find("div", class_="item published")
    date = date_div.section.div.text.strip() if date_div else None
    article["date"] = date

    authors = get_authors(soup.find("section", class_="item authors"))
    article["authors"] = authors

    return title, article


soup = get_page(MAIN_URL)
issue_number = 1

while next:
    issue_urls = get_issue_urls(soup)
    next = soup.find("a", class_="next")["href"]

    for issue_url in issue_urls:
        print("Issue", issue_number)
        issue_number += 1
        article_number = 1
        soup = get_page(issue_url)
        article_urls = get_article_urls(soup)

        for article_url in article_urls:
            print("Article", article_number)
            article_number += 1
            article = get_page(article_url)
            title, article_details = get_article_details(article)

            article_details["url"] = article_url
            dict[title] = article_details

        with open("articles.json", "w", encoding="utf-8") as f:
            json.dump(dict, f, ensure_ascii=False, indent=4)
            
    soup = get_page(next)