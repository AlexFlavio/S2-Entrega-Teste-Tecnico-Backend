# S2-Entrega-Teste-Tecnico-Backend

##### Este projéto foi feito em **Django**, o mesmo tem o intuito de receber um arquiv.txt em uma formatação especifica e transpilar os dados do arquivo para um banco de dados **Sqlite**, assim os tornando acessiveis em uma busca por nome da loja onde é rotornado todas as tranações feitas por aquela lojá e um valor total para todas as transações feitas.

## Passo a Passo para instalação e utilização local da Aplicação:


1. ### Faça o Clone em uma pasta local.

2. ### Crie o `ambiente virtual`
```
python -m venv venv
```

3. ### `Ative o venv`
```bash
# linux:
source venv/bin/activate
# windows:
.\venv\Scripts\activate
```

4. ### Instale as dependências
```
pip install -r requirements.txt
```
5. ### Execute as migrações
```
python manage.py migrate
```

6. ### Inicie o servidor local
 ```
 python manage.py runserver
 ```


7. ### Para Utilização do formulario utilize a rota:
```
http://localhost:8000/api/docs/
```

8. #### Rota de Post:
##### `Altere` em `Request Body` a opção `application/json` para `multipart/form-data`
