# S2-Entrega-Teste-Tecnico-Backend

## Sobre o propjeto:
****
#### Este projéto foi feito em **Python** utilizando o FrameWork **Django**, o mesmo tem o intuito de receber um arquivo.txt com uma formatação especifica e transpilar os dados do arquivo.txt para um banco de dados **Sqlite**, assim os tornando os dados acessiveis em uma busca por nome da loja onde é rotornado todas as trasações feitas por aquela loja e um valor total para todas as transações feitas.

### Tecnologias utilizadas:
* #### Python | Linguaguem
* #### Django-Rest-Framework | FrameWork
* #### Drf-Spectacular | documentação


## Passo a Passo para instalação e utilização local da Aplicação:
****

 ### 1. `Faça o Clone em uma pasta local.`
 
 ### 2. `Crie o ambiente virtual`
```
python -m venv venv
```

 ### 3. `Ative o venv`
```bash
# linux:
source venv/bin/activate
# windows:
.\venv\Scripts\activate
```

 ### 4. `Instale as dependências`
```
pip install -r requirements.txt
```
 ### 5. `Execute as migrações`
```
python manage.py migrate
```

 ### 6. `Inicie o servidor local`
 ```
 python manage.py runserver
 ```


 ### 7. `Para Utilização do formulario de envio e documentação utilize a rota:`
```
http://localhost:8000/api/docs/
```

 #### 8. `Rota de Post:`
##### `Altere` em `Request Body` a opção `application/json` para `multipart/form-data`
##### assim será possivel selicionar o arquivo `diretamente de seu computador!`
