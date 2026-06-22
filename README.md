🧠 Aplicativo Web de Saúde Mental

Este projeto é uma aplicação web desenvolvida com Django, com foco em estudo e prática de desenvolvimento web. Ele permite rodar um sistema completo localmente no computador.

 🚀 COMO RODAR O PROJETO

Este projeto funciona da mesma forma independentemente de como foi obtido: seja por Git Clone, download em ZIP ou abertura direta da pasta no VS Code. O processo final para execução é sempre o mesmo.


💻 ABRINDO O PROJETO NO COMPUTADOR

Se você baixou o projeto em ZIP, extraia o arquivo e abra a pasta no VS Code em "File → Open Folder".

Se você clonou o projeto com Git, use este comando no terminal:
git clone https://github.com/hugssmari/Aplicativo-Web-Sa-de-Mental-2025.git  

e depois este para localizar o arquivo
cd Aplicativo-Web-Sa-de-Mental-2025

Depois disso, abra a pasta no VS Code (opcional, mas recomendado).

Se você já tem a pasta no computador, basta abrir diretamente no VS Code.



AVISO: Todos os comandos podem ser executados em qualquer terminal (VS Code, PowerShell, CMD ou Terminal do Mac/Linux), desde que o usuário esteja dentro da pasta do projeto e com o ambiente virtual ativado.



🧭 ABRINDO O TERMINAL
No VS Code, clique em "Terminal → New Terminal".  
Certifique-se de que o terminal está dentro da pasta do projeto.


🐍 CRIANDO O AMBIENTE VIRTUAL (OBRIGATÓRIO)
Digite este código no terminal do projeto

python -m venv venv

▶️ ATIVANDO O AMBIENTE VIRTUAL
ative o ambiente virtual no terminal do vs code dentro da pasta do projeto ou no powershell, cmd, terminal mac/Linux

No Windows:

venv\Scripts\activate

No Mac/Linux:

source venv/bin/activate

Se funcionar corretamente, aparecerá (venv) no início da linha do terminal.


📦 INSTALANDO O DJANGO

Este projeto não utiliza requirements.txt, então o Django deve ser instalado manualmente:

pip install django


🗄️ MIGRAÇÕES DO BANCO DE DADOS

python manage.py migrate


🚀 INICIANDO O SERVIDOR

python manage.py runserver


🌐 ACESSANDO O PROJETO

Abra o navegador e acesse:

http://127.0.0.1:8000/



 ⚠️ POSSÍVEIS PROBLEMAS

Se aparecer o erro "No module named django", significa que o Django não está instalado no ambiente virtual. Resolva com:

pip install django

Se o site não abrir, verifique se o servidor está rodando com o comando runserver.


🧠 RESUMO DO PROCESSO

1. Abrir o projeto (ZIP, Git ou pasta)
2. Abrir terminal no VS Code
3. Criar ambiente virtual
4. Ativar ambiente virtual
5. Instalar Django
6. Rodar migrate
7. Rodar server
8. Abrir no navegador



👩‍💻 AUTOR

Desenvolvido por Mariana Carvalho como projeto de estudo em desenvolvimento web com Django.
