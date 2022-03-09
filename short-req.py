import requests


req = requests.get('https://www.alura.com.br/')
print(req.headers)

# req.status_code -retorna o status da requisição
# req.headers     -retorna os hearders da requisição
# req.headers['Content-Type'] - retorna o content type
# req.text        - retorna o html (formato texto) da requisição
