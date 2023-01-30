# Polímata Chatbot

Pacote inicial de código aberto para desenvolvimento de chatbots contextuais voltados à ambientes escolares.

## Tecnologias do Projeto:

* [Rasa](https://rasa.com/) - Inteligência Artificial do Bot
* [Docker](https://www.docker.com/) - Tecnologia de conteinerização
* [Docker Compose](https://docs.docker.com/compose/) - Orquestrador de containers Docker
* [Telegram](https://telegram.org/) - Aplicativo de mensagens instantâneas

## Instalação e configuração:
Para testar o chatbot localmente use os seguintes comandos:

**1º Passo**: Para instalar clone o repositório:
```
git clone https://github.com/luan-github/polimata-chatbot.git
```

**2º Passo**: Treine um modelo de conversação:

Acesse o diretório rasa_server:
```
cd polimataBot/rasa_server
```
Execute:
```
rasa train
```

Ou, caso você não tenha o rasa 3.x intalado, use:
```
docker run --user 1000 -v $(pwd):/app rasa/rasa:3.4.1-full train --domain domain.yml --data data --out models
```

**3º Passo**: Inicie os conteiners usando o docker compose :

Volte ao diretório raiz do projeto:
```
cd ..
```

Para iniciar os containers:
```
docker compose up
```

**4º Passo**: Para interagir com o chatbot via terminal:
```
docker exec -it polimataBot rasa shell -p <porta-disponível>
```

Ou
```
docker compose exec -it rasa-server rasa shell -p <porta-disponível>
```

**5º Passo**: Para ensinar novos dialogos de forma automatizada:
```
docker exec -u root -it polimataBot rasa interactive -p <porta-disponível>
```

**6º Passo**: Para parar os containers:
```
docker compose down
```

## Configurar acesso via Telegram:
**1º Passo**: crie um chatbot no Telegram, interagindo com o [BotFather](https://t.me/BotFather), para obter um Token de acesso e novo nome de chatbot.

**2º Passo**: edite o arquivo credentials.yml, na pasta rasa_server, removendo os símbolos '#' que comentam as linhas referentes a configuração do Telegram e preencha os valores dos parametros com os dados do bot criado, exemplo:
```
telegram:
  access_token: "<XXXXXX_Token de acesso_XXXXX>"
  verify: "<nome do chatbot sem o símbolo @>"
  webhook_url: "<https:url_para_a_qual_o_Telegram_deve_enviar_as_mensagens>/webhooks/telegram/webhook"
```

Você pode usar a aplicação [ngrok](https://ngrok.com) para gerar a url necessária acima, com o comando:
```
./ngrok http 5005
```

Para informações mais detalhadas de configuração do Telegram e outros canais acesse a [documentação do framework Rasa aqui](https://rasa.com/docs/rasa/messaging-and-voice-channels/).

**3º Passo**: Para executar os containers:
```
docker compose up
```

Caso queira alterar os nomes dos containers no arquivo docker-compose.yml lembre-se de fazer as correspondentes alterações no arquivo endpoints.yml e demais comandos exemplificados nesta página.

Uma vez que já tenha gerado um modelo de conversação não será mais necessario acesar a pasta rasa_server via terminal para treinar o chatbot novamente. Você poderá usar:
```
docker exec -u root -it polimataBot rasa train --domain domain.yml --data data --out models
```

## Como Contribuir ou obter ajuda:
Toda contribuição é bem vinda, para participar você deve:

- Criar uma issue descrevendo uma funcionalidade que você gostaria de desenvolver ou contribuir com as já criadas.
- Escrever seu código, testes e documentação.
- Abrir um pull request descrevendo as suas alterações propostas.
- Aguardar que seu pull request seja revisado e que eventualmente você seja solicitado a realizar algumas alterações.
- Caso tenha dificuldades buscando informações relacionados ao projeto você também pode criar uma issue com a tag `duvida`.

## Sugestões de fontes para estudo:
* [Documentação do framework Rasa](https://rasa.com/docs/rasa/) - Para aprender como criar novos diálogos de forma manual ou novas funcionalidades para o chatbot.
* [Rasa no youtube](https://www.youtube.com/@RasaHQ/featured) - Canal de divulgação da equipe que mantém o framework com tutoriais de configuração.
* [Código fonte do livro Docker Para Desenvolvedores](https://github.com/gomex/docker-para-desenvolvedores)
* [Livro Pro Git](https://git-scm.com/book/en/v2)

## Licença:
Este software foi desenvolvido sob a licença [GPL3](https://github.com/luan-github/polimata-chatbot/blob/main/LICENSE).
