# Pool_budget
**Pool_budget**  is an application to calculate some information to build a swimming-pool

## Recursos utilizados
- [x] Python 3.8
- [x] Django 3.0
  - [x] django-debug-toolbar 2.2
- [x] SQLite  
- [x] HTML
- [x] CSS
- [x] JavaScript
- [x] Bootstrap
  
## Screenshots
![image](https://user-images.githubusercontent.com/52714788/84071140-9b63e500-a9a3-11ea-87e8-e97b7fea9669.png)
![image](https://user-images.githubusercontent.com/52714788/84072560-c0595780-a9a5-11ea-9843-3f29f2f8d0cd.png)
![image](https://user-images.githubusercontent.com/52714788/84072645-e41c9d80-a9a5-11ea-8c8d-96dbf2d6a90e.png)

## Como instalar? *How to install?*

**Clone o repositório.**
*Clone this repository*

$ 'git clone https://github.com/leopesi/pool_budget.git'


**Crie um virtualenv**

- 'pip install virtualenv'
- virtualenv nome_da_virtualenv

**Ativando uma virtualenv**

- souce nome_da_virtualenv/bin/activate (Linux ou macOS)
- nome_da_virtualenvScriptsactivate (Windows)

**Instale as depêndencias.**
- pip install -r requirements.txt

**Rode as Migrações**
1. python manage.py makemigrations
2. python manage.py migrate

**Crie um super usuário.**
- python manage.py createsuperuser

**Rode o servidor.**
- python manage.py runserver
