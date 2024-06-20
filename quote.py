import requests

def generate_quote():
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']

        return f'{quote} - {author}'

    else:
        return 'failed to get quote'

#printing random generated code

print(generate_quote())