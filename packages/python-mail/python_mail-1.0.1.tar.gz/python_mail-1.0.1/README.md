# Python Mail

## Sumário

> * [Introdução](#introdução)
> * [Instalando o módulo](#instalando-o-módulo)
> * [Configurando a conexão](#configurando-a-conexão)
>   * [Linux](#variáveis-de-ambiente-no-linux)
>   * [Windows](#variáveis-de-ambiente-no-windows)
> * [Exemplos](#exemplos)
>   * [Configuração inicial](#configuração-inicial)
>   * [Filtrando mensagens](#buscando-mensagens)
>   * [Resultado](#resultado)

## Introdução

Esse módulo foi criado com o objetivo de realizar a busca de mensagens na caixa de e-mail de forma simplificada e intuitiva utilizando o módulo imaplib para conexão. 


## Instalando o módulo

  - Para a instalação utilize:

  ```bash
  $ pip install python-mail 
  ```
  
  
### Configurando a conexão
   A conexão com a caixa de e-mail é feita através de variáveis de ambiente.


  #### Variáveis de ambiente no Linux
   - Configurando o servidor:

      ```bash
      $ export CONNECT-IMAP'imap.servidor.com' 
      ```
  
   - Configurando o email:

      ```bash
      $ export EMAIL='email@dominio.com' 
      ```
  
   - Configurando a senha:

      ```bash
      $ export PASSWD='password' 
      ```
  
  #### Variáveis de ambiente no Windows
   - Configurando o servidor:

      ```batch
      > set CONNECT-IMAP='imap.servidor.com' 
      ```
  
   - Configurando o email:

      ```batch
      > set EMAIL='email@dominio.com' 
      ```
  
   - Configurando a senha:

      ```batch
      > set PASSWD='password' 
      ```
## Exemplos

  ### Configuração inicial

  ``` python
      from python_mail.Search import Search

      # deve-se passar em qual caixa a busca será feita
      search = Search("inbox")

  ```

  ### Filtrando mensagens
  Os filtros podem ser feitos por: Body, From e Subject.

  ``` python
      
      id_message = search.search_body('Body Message')

      id_message = search.search_from('example@email.com')

      id_message = search.search_subject('Subject Message')

  ```

  O retorno dos métodos acima serão o ID das mensagens que foram encontradas.

  ### Filtrando mensagens


    - Para obter o conteúdo completo das mensagens:

    ``` python
        
        data_message = search.result_message(id_message)

    ```

    - Para obter a data das mensagens:
    
    ``` python
        
        data_message = search.result_date(id_message)

    ```

    - Para saber o remetente das mensagens:
    
    ``` python
        
        data_message = search.result_from(id_message)

    ```

    - Para saber o destinatário das mensagens:
    
    ``` python
        
        data_message = search.result_to(id_message)

    ```

  Todos os métodos listado acima devem receber uma lista como parâmetro.


