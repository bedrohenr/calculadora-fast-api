# Calculadora com Fast API

Calculadora pela web XD

## Funcionamento

Inicialize o servidor web e utilize os endpoints como função da calculadora.

Você deve enviar uma requisição **POST** com um JSON no exemplo a seguir:

```
{
    "first_number": 0,
    "second_number": 0
}
```
Para um dos endpoints a seguir:
- [localhost:8000/soma](localhost:8000/soma): Soma
- [localhost:8000/subt](localhost:8000/subt): Subtração
- [localhost:8000/multi](localhost:8000/multi): Multiplicação
- [localhost:8000/div](localhost:8000/div): Divisão
- [localhost:8000/expo](localhost:8000/expo): Exponenciação

## Execução

Clone o e entre na pasta do projeto.

```bash
git clone https://github.com/bedrohenr/calculadora-fast-api.git
```

e Entre na pasta do projeto:

```bash
cd calculadora-fast-api
```

É recomendado você utilizar um **[ambiente virtual](https://fastapi.tiangolo.com/virtual-environments/#check-the-virtual-environment-is-active)**.

Instale o Fast API e suas dependências com o comando a seguir:

```bash
pip install "fastapi[standard]"
```

E em seguida, rode o projeto iniciando o servidor web:


```bash
fastapi dev main.py
```
