# CNH Scanner

Esta aplicação foi desenvolvida como forma de desafio técnico de avaliação para a vaga de Machine Learning na empresa Docket. E tem como intuito o reconhecimento de informações de identificação presentes no documento CNH.

## Requisitos

Para que a ferramenta possa ser executada adequadamente é necessário realizar a instalação do executável ``tesseract-ocr-w64-setup-v4.1.0.20190314.exe`` no Windows. Caso a ferramenta vá ser utilizada no Linux basta instalar o pacote do tesseract com o seguinte comando:

```bash
sudo apt update
sudo apt install tesseract-ocr
```

Além disso, pode ser necessário alterar no script de OCR o caminho de onde esta contido o binário do Tesseract.

Você também precisará de Python 3 e pip. É altamente recomendado utilizar ambientes virtuais com o virtualenv e o arquivo `requirements.txt` para instalar os pacotes de dependências da ferramenta:

Linux

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Windows

```bash
> pip3 install virtualenv
> virtualenv ..\venv -p python3
> ..\venv\Scripts\activate
> pip install -r requirements.txt
```

Quando finalizado, você pode desativar o ambiente virtual do virtualenv com:

```bash
$ deactivate
```

## Executando

Este programa foi implementado para ser usado como um módulo Python, portando para utilizá-lo é necessário importá-lo em seu código principal da mesma forma que se importa uma biblioteca em um código Python. A seguir um exemplo de uso:

```python
from glob import glob
from ocr import search_cpf

test_files = glob('photos/*')
print('Founded files:')
print(test_files)

for test_file in test_files:
  search_cpf(test_file, is_testing=False)
```

Como pode ser visto no exemplo acima, para usar o programa basta importá-lo com o comando `from ocr import search_cpf` e então chamar a função `search_cpf` contida no script, passando os argumentos necessários.

### Argumentos

Como informado acima, este programa contêm alguns argumentos, sendo eles os seguintes:

* **filename**: Nome do arquivo de CNH em formato ``string``. (Parâmetro obrigatório)
* **is_testing**: Informa se o programa deve apresentar uma depuração mais avançada do que esta acontecendo internamente na função. (Por padrão recebe ``False``)