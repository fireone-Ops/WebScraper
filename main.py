from parser import parse_html
from scraper import validacao


def main():
    url = input("Digite a URL: ")
    response = validacao(url)
    if response is not None:
        html_content = response.text
        soup = parse_html(html_content)
        print(soup.prettify())
    else:
        print("Falha na validação da URL.")


if __name__ == "__main__":
    main()