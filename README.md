# Aplicativo Garantias (SCGP) para arquiteturas monolíticas com Python e Django

Repositório do projeto SCGP que se baseia em arquitetura monolítica com Python e Django

## Referências

- [Desenvolvimento Web com Django 3 Cookbook](https://a.co/d/g9jbw3D) - 2020 - Novatec

## Passos para criação inicial do projeto (do zero)

> ❕**Atenção**
>
> * Os passos abaixo foram testados no Windows 11 com o PowerShell com Python 3.11 instalado. Caso você esteja usando outro sistema operacional, você pode precisar adaptar os comandos para o seu ambiente. Para mais informações sobre como preparar o computador para desenvolvimento com Python e Django, utilizando Git e VSCode, acesse a página que discorre sobre como [preparar o ambiente](https://maxwellamaral.github.io/lessons/softeng/).
>
> - Para construir um ambiente mais simples, basta seguir os passos 1.1 a 1.4 abaixo e executar o comando `py .\manage.py runserver` para visualizar o Django em execução. Ocorre que a preparação do ambiente como descrito abaixo é usado profissionalmente e é recomendado para quem deseja trabalhar com Python e Django.

1. **Preparando o ambiente** (passos para Windows usando o PowerShell)

    1. Como python instalado, crie um ambiente virtual com o comando `python -m venv .venv`
    2. Ative o ambiente virtual com o comando `.venv\Scripts\activate` ou execute o comando `.\active_wenv.bat`.
    3. Instale o Django com o comando `pip install django`.
    4. Execute o comando `django-admin startproject garantias .` para criar o projeto Django com o nome de `garantias` e o diretório raiz do projeto será o diretório atual.
    5. Crie as pastas com o comando `mkdir media,static,locale,externals,externals\apps,externals\libs,requirements` na pasta raiz do projeto.
    6. Na pasta `garantias` crie as pastas com o comando `mkdir apps,apps\core,settings,site_static,templates`
    7. Na pasta `garantias\site_static` crie as pastas com o comando `mkdir site,site\css,site\js,site\img,site\scss`
    8. A pasta deverá ter essa aparência:

       ```text
       dj                          <-- pasta raiz do projeto
       |-- externals               <-- pasta para os arquivos externos do projeto, como por exemplo, libs e apps de terceiros (não versionados)
       |-- garantias
       |   |-- apps                <-- pasta para os apps (módulos) do projeto
       |   |   |-- __init__.py     <-- arquivo de inicialização do app (toda pasta que contém um arquivo __init__.py é considerada um módulo)
       |   |   |-- core            <-- pasta core para códigos compartilhados entre os apps
       |   |   |   |-- __init__.py
       |   |-- settings
       |   |   |-- __init__.py
       |   |   |-- _base.py        <-- arquivo base de configuração onde foi renomeado de settings.py
       |   |   |-- dev.py          <-- arquivo de configuração de desenvolvimento
       |   |   |-- prod.py         <-- arquivo de configuração de produção
       |   |   |-- secrets.json    <-- arquivo de configuração de senhas e chaves
       |   |   |-- staging.py      <-- arquivo de configuração de homologação
       |   |   |-- test.py         <-- arquivo de configuração de testes
       |   |-- site_static
       |   |   |-- site            <-- pasta para os arquivos estáticos do projeto
       |   |   |   |-- css         <-- pasta para os arquivos css do projeto
       |   |   |   |-- img         <-- pasta para os arquivos de imagens do projeto
       |   |   |   |-- js          <-- pasta para os arquivos js do projeto
       |   |   |   |-- scss        <-- pasta para os arquivos scss do projeto
       |   |-- templates           <-- pasta para os templates do projeto
       |   |-- __init__.py         <-- arquivo de inicialização do projeto
       |   |-- asgi.py
       |   |-- urls.py             <-- arquivo de configuração de urls
       |   |-- wsgi.py
       |-- locale                  <-- pasta para os arquivos de tradução
       |-- media                   <-- pasta para os arquivos de mídia
       |-- requirements            <-- pasta para os arquivos de requirements
       |   |-- _base.txt           <-- arquivo base de requirements
       |   |-- dev.txt             <-- arquivo de requirements de desenvolvimento
       |   |-- prod.txt            <-- arquivo de requirements de produção
       |   |-- staging.txt         <-- arquivo de requirements de homologação
       |   |-- test.txt            <-- arquivo de requirements de testes
       |-- static                  <-- pasta para os arquivos estáticos do projeto
       |-- .gitignore              <-- arquivo de configuração do git
       |-- active_wenv.bat         <-- arquivo de ativação do ambiente virtual
       |-- manage.py               <-- arquivo de gerenciamento do projeto
       |-- LICENSE                 <-- arquivo de licença do projeto em inglês
       |-- LICENSE.pt-br.txt       <-- arquivo de licença do projeto em português
       |-- README.md               <-- arquivo de documentação do projeto
       ```

    9. Crie o arquivo `requirements\_base.txt` com o conteúdo inicial abaixo:

       ```requirements
       black==23.1.0
       click==8.1.3
       colorama==0.4.6
       Faker==18.3.1
       faker-commerce==1.0.3
       mypy-extensions==1.0.0
       packaging==23.0
       pathspec==0.11.1
       platformdirs==3.2.0
       python-dateutil==2.8.2
       six==1.16.0
       toml==0.10.2
       XlsxWriter==3.0.9

       django==4.2
       djangorestframework==3.14
       ```

2. **Configurando o projeto**

    1. Crie o arquivo `requirements\dev.txt` com o conteúdo inicial abaixo:

        ```requirements
        -r _base.txt

        coverage==7.2
        django-debug-toolbar==4.0
        selenium==4.8
        ```

    2. Em `garantias\settings\_base.py` altere o conteúdo da variável `BASE_DIR` para:

        ```python
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        ```

    3. Em `garantias\settings\prod.py` adicione a seguinte linha no início do arquivo:

        ```python
        from ._base import *
        ```

    4. Faça o mesmo para os arquivo `garantias\settings\staging.py` e `garantias\settings\test.py`.
    5. Em `garantias\settings\dev.py` adicione as seguintes linhas no início do arquivo:

        ```python
        from ._base import *

        DEBUG = True
        ALLOWED_HOSTS = ["*"]
        EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
        ```

    6. Em `.\manage.py`, `garantias\wsgi.py` e em `garantias\asgi.py` altere as seguintes linhas:

        ```python
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'garantias.settings')
        ```

        para

        ```python
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'garantias.settings.prod')
        ```

    7. Em `garantias\settings\_base.py` altere e adicione as seguintes linhas:

        ```python
        import os

        # ...

        TEMPLATES = [
            {
                'BACKEND': 'django.template.backends.django.DjangoTemplates',
                'DIRS': [
                    os.path.join(BASE_DIR, 'garantias', 'templates')
                ],
                'APP_DIRS': True,
                'OPTIONS': {
                    'context_processors': [
                        'django.template.context_processors.debug',
                        'django.template.context_processors.request',
                        'django.contrib.auth.context_processors.auth',
                        'django.contrib.messages.context_processors.messages',
                    ],
                },
            },
        ]

        # ...

        LOCALE_PATHS = [
            os.path.join(BASE_DIR, 'locale')
        ]

        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'garantias', 'static')
        ]

        STATIC_ROOT = os.path.join(BASE_DIR, 'static')
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

        ```

    8. Para executar o projeto, execute o comando abaixo:

        ```pwsh
         py .\manage.py runserver --settings=garantias.settings.dev
        ```

        > **Observação**: o comando acima deve ser executado na pasta raiz do projeto. O parâmetro `--settings` é obrigatório no ambiente do desenvolvedor para que o Django encontre os arquivos de configuração de desenvolvimento corretamente. Perceba que ele é composto pelo caminho do arquivo de configuração de desenvolvimento, que no caso é `garantias\settings\dev.py`.

    9. A aplicação deve estar disponível em `http://127.0.0.1:8000/`. Irá aparecer a página padrão de boas vindas do Django.
    10. Vamos esconder configurações e dados sensíveis do projeto, como por exemplo, o SECRET_KEY do Django. Edite `settings\_base.py` e adicione as seguintes linhas:

        ```python
        import os
        from django.core.exceptions import ImproperlyConfigured

        def get_secret(setting):
            """
            Configura a leitura das variáveis de ambiente
            """
            try:
                return os.environ[setting]
            except KeyError:
                error_msg = f"Set the {setting} environment variable"
                raise ImproperlyConfigured(error_msg)
        
        # ...
        SECRET_KEY = get_secret('DJANGO_SECRET_KEY')
        # ...
        ```

    11. Para incluir dependências externas ao projeto, vamos alterar novamente o arquivo `settings\_base.py` de modo que o Django consiga enxergar as dependências instaladas no ambiente virtual. Adicione as seguintes linhas:

        ```python
        import os
        import sys

        # ...

        # Este é o diretório do arquivo atual, que é o diretório base do projeto
        BASE_DIR = Path(__file__).resolve().parent.parent.parent
        # Este é o diretório que contém todas as bibliotecas e aplicativos externos
        EXTERNAL_BASE = os.path.join(BASE_DIR, 'externals')
        # Este é o diretório que contém todas as bibliotecas externas
        EXTERNAL_LIBS_PATH = os.path.join(EXTERNAL_BASE, 'libs')
        # Este é o diretório que contém todos os aplicativos externos
        EXTERNAL_APPS_PATH = os.path.join(EXTERNAL_BASE, 'apps')
        # Adicione todas as bibliotecas e aplicativos externos ao caminho
        sys.path = [EXTERNAL_LIBS_PATH, EXTERNAL_APPS_PATH] + sys.path
        ```

    12. Pronto. Ambiente configurado!
