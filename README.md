### Instalação:

Para instalar as depedências do projeto use:

```shell
pip3 install -r requirements.txt
```

### Manipulação do Banco de Dados:
Para criar tabelas do banco de dados execute os seguintes comandos:

- Abra o terminal _flask_:
```shell
flask shell
```

- Apague todas as tabelas se necessário:
```shell
db.drop_all()
```

- Agora crie todas as tabelas:
```shell
db.create_all()
```

- Adicione usuários da seguinute forma. Exemplo:
```shell
user = User(username="admin", password="123")
db.session.add(user)
```

- Por fim, grave todas as modificações realizadas:
```shell
db.session.commit()
```

- Para sair do terminal _flask shell_ use:
```shell
exit()
```
