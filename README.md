# Projeto Django: Recibo GrupoCyber

* Breve Resumo:

Projeto de geração de recibo para empresa Grupocyber com funcionalidades CRUD de gerenciamento de cliente, gerenciamento de usuário do sistema, gerenciamento de recibo, persistencia de dados em banco de dados, deshboard iterando com os dados coletados e relatório demostrativo de clientes, recibos e usuários do sistema.

* Funcionalidades e Demonstração da Aplicação

Acesso a plataforma
![image](https://github.com/user-attachments/assets/1818a0ff-dcc1-4f4f-8daf-04dd1c456821)


Cadastro de Usuario
![image](https://github.com/user-attachments/assets/6830ad60-8c79-4410-ba07-b5aafd3efa76)

Gerenciando Usuario
![image](https://github.com/user-attachments/assets/b66d568a-f27d-42b4-b4c4-aab4c54cc084)

Cadastro de Cliente
![image](https://github.com/user-attachments/assets/c2c68ec3-976f-40ce-bd3c-7add7d8a1f63)

Gerenciando Clientes
![image](https://github.com/user-attachments/assets/c6c9df5f-821b-4343-8378-2d2ec5c7b31b)

Cadastro de Recibo
![image](https://github.com/user-attachments/assets/80b45e02-4477-454c-94fd-ca3f97cdd858)

Gerenciando Recibos
![image](https://github.com/user-attachments/assets/b7c341a4-3ff6-4b82-a340-1b0381e11a54)

Dashboard com gráfico simples
![Screenshot from 2024-07-15 08-28-07](https://github.com/user-attachments/assets/76c77b59-7b87-4bf9-985a-9e27988dba59)

* Tecnologias utilizadas

  * Python
  * Django
  * Conexão com banco de dados SQLite
  * Dotenv
  * Pandas
  * Plotly
    
* Pessoas Desenvolvedoras do Projeto

  Autores

| [<img loading="lazy" src="https://avatars.githubusercontent.com/u/9308189?v=4" width=115><br><sub>Ericson Nascimento</sub>](https://github.com/ericsonnascimento) |
| :---: |

* Conclusão

Com a comclusão do projeto, concegui observar que sempre temos o que aprender nesta área tão apaixonante, provavelmente meus próximos passos serão ampliar cada vez mais as funcionalidades deste projeto.

# De desenvolvedor para desenvolvedor:

1. Primeiro passo é criar um ambiente virtual do tipo venv:

   `python -m venv venv`
   
2. Vamos ativar o ambiente e instalar as dependências (estou utilizando o windows):

   `.\venv\Scripts\activate`
   `pip install -r .\requeriments.txt`

   Caso ocorra algum erro na instalação, abra o requirements.txt e instale manualmente cada uma das bibliotecas:
   Django, Python-dotenv, Pandas, Plotly, Numpy
   
3. Terceiro, basta rodar o comand `runserver` para que o banco de dados sqlite seja criado, não esqueça de para o servidor com ctrl+c que possibilitará rodar os comandos logo a baixo:
   
   `python .\manage.py runserver`

4. Em seguida vamos popular o DB rodando o comando:
   
   `python .\manage.py migrate`
   
6. Feito isso podemos criar o usuário admin:

   `python manage.py createsuperuser`

7. Precisamos agora gerar um arquivo .env onde são guardados os dados sensiveis do projeto.

   * Estou guardando nesse arquivo a variável SECRET_KEY = 'sequencia_de_numeros_e_letras'

8. Para que o *Dashboard* não aprente error ao abrir pela primeira vez, vamos adicionar algumas informações através do /admin:

   `python .\manage.py runserver`
   
   http://127.0.0.1:8000/admin (logue com a conta criada superuse e insira um cliente e um recibo)

10. Agora podemos ir para http://127.0.0.1:8000, logar com a conta e em seguida seremos redirecionados para o *Dashboard*.

   
 
