# Calculadora_Online
Calculadora que realiza cálculos através de um servidor remoto transparentemente.

<p align="center">
  <img src="https://github.com/jpdik/Calculadora_Online/blob/master/img/example.png?raw=true" width="150"/>
</p>

## Deploy automático
Você pode fazer um deploy do exemplo aqui. <br>
<a href="https://heroku.com/deploy?template=https://github.com/jpdik/Calculadora_Online">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>

# Configurar Heroku para Python
Se ainda não o tiver, instale o heroku pelo comando:

### MacOS
Com homebrew:
<pre>
brew install heroku
</pre>

### Windows
Download <a href="https://cli-assets.heroku.com/branches/v6/heroku-windows-386.exe">32-bit</a> ou <a href="https://cli-assets.heroku.com/branches/v6/heroku-windows-amd64.exe">64-bit</a>.

### Linux
A forma que considero facil é através do npm:
<pre>
$ npm install -g heroku-cli
</pre>

## Fazendo login
Realize sua credencial de acordo com os dados cadastrados no site:

<pre>
$ heroku login
Enter your Heroku credentials.
Email: python@example.com
Password:
...
</pre>

## Criando Aplicação
Para criar a aplicação que vc utilizará o seu programa, vá até o diretório do mesmo e use o comando:

<pre>
$ heroku create [NomeAplicação]
</pre>

Será criado um uma aplicativo contendo na URL o parâmetro passado na função:

<pre>
NomeAplicação.herokuapp.com
</pre>

Caso não passe ele gerará um nome aleatório e o exibirá.

Através deste link voçê terá acesso a sua aplicação.

## Configurando maquina antes do Upload
Precisamos passar informações importantes para o heroku através de arquivos de configuração.

Precisamos criar e modificar os arquivos de configuração `Procfile`, `requirements.txt` e `runtime.txt`.

#### Procfile
Aqui passamos a configuração para rodar o servidor. iremos utilizar o `guicorn`. no lugar de app deve ser substituído pelo nome do arquivo principal da aplicação (`main`).

O arquivo `Procfile` deverá ficar da seguinte forma:

> web: gunicorn app:app

#### requirements.txt
Todos os requisitos para rodar a aplicação (bibliotecas) devem ser informadas neste arquivo juntamente de suas versões.
Temos duas formas de obter estes valores:

`pip freeze`: É a forma mais simples, mas ele pega todas as bibliotecas do pip, então será necessário ajustes, o que não é muito bom.
<pre>
pip freeze > requirements.txt
</pre>

`pipreqs`: É mais rápido e só entrega o que precisa. Basta instalá-lo. e passar um parâmetro para o comando com caminho de onde ele será gerado.

<pre>
$ pip install pipreqs
$ pipreqs /path/to/project
</pre>

O arquivo `requirements.txt` ficará parecido com isto:

> gunicorn==19.7.1
> requests==2.9.1
> Flask==0.12.2

As vezes o guicorn não é reconhecido, precisando ser inserido manualmente.

#### runtime.txt
Precisamos informar para o heroku a versão do python também. Ele está prédefinido como python 3, então através deste arquivo o modificamos e deixamos parecido com este arquivo `runtime.txt`:

>python-2.7.12

## Fazendo Upload da Aplicação
O heroku tem uma simples integração com o Github. Para realizar o upload basta usar o comando:

<pre>
 $ git push heroku master
</pre>

Pronto! Sua aplicação será instalada passo a passo pelo console baseado nas suas configurações. Você poderá ver toda a instalação e todos os erros que podem acontecer durante ela. Se ela tiver total sucesso terá a seguinte mensagem.

<pre>
remote: Verifying deploy... done.
</pre>

Para checar erros de execução, verifique os logs:

<pre>
heroku logs
</pre>

# Informações adicionais
Caso não consiga realizar os cálculos, provavelmente o servidor que está sendo utlizado para rodar o script `Servidor/sv_calc.py` está offline. Você precisará modificar o IP do socket dele e do arquivo `app.py`
