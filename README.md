# POC_injection_RDS_AWS

O objetivo desta POC é demonstrar de forma simples uma ingestão de dados para o PostgreSQL via RDS na AWS

Tarefas:

- Fazer download do Dataset : https://dados.gov.br/dados/conjuntos-dados/ifn-inventario-florestal-nacional OK
- Criar usuário na AWS OK
- Criar uma instância do RDS OK
- Criar um Database PostgreSQL via RDS OK
  ![image](https://github.com/gsvimieiro/POC_injection_RDS_AWS/assets/25323854/11807007-b3ed-4e53-bdb9-05a1f8cd2e66)
- Observação importante:
  -   Ao criar o Database, por questões didáticas, este precisa ser acesso Público
  -   Porém não basta ter acesso público, tem que criar um Security Group apontando a entrada de acesso para o PostgreSQL porta 5432 via o próprio IP

    ![image](https://github.com/gsvimieiro/POC_injection_RDS_AWS/assets/25323854/97ae2ab6-e146-4c34-953f-b79b3e221df3)

- Instalar o DBeaver OK
- Criar uma conexão ao banco PostgreSQL via DBeaver OK

  ![image](https://github.com/gsvimieiro/POC_injection_RDS_AWS/assets/25323854/a8b0f4af-bca3-42e8-a60a-f7d2eceeb4b2)

- Executar a aplicação
