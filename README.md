### Instalação:

Para instalar as depedências do projeto use:

> ```pip3 install -r requirements.txt```

### Manipulação do Banco de Dados:
Para criar tabelas do banco de dados execute os seguintes comandos:

- Abra o terminal _flask_:
> ```flask shell```
- Apague todas as tabelas se necessário:
> ```db.drop_all()```
- Agora crie todas as tabelas:
> ```db.create_all()```
- Adicione usuários da seguinute forma. Exemplo:
> ```user = User(username="admin", password="123")```

> ```db.session.add(user)```
- Por fim, grave todas as modificações realizadas:
> ```db.session.commit()```
- Para sair do terminal _flask shell_ use:
> ```exit()```