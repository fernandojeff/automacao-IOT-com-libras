# Controle de Dispositivos por Sinais (Protótipo)

Este projeto é um protótipo que permite que pessoas surdas controlem dispositivos domésticos por meio de sinais, utilizando a câmera de notebooks ou dispositivos móveis. Ele oferece uma solução acessível para tornar o ambiente doméstico mais interativo e adaptado às necessidades da comunidade surda.

## Funcionalidades

- **Reconhecimento de gestos**: Tradução de sinais em comandos para controlar dispositivos como luzes e temperatura.
- **Acessibilidade**: Focado em oferecer maior independência e conforto para a comunidade surda.
- **Dispositivos suportados**: Utiliza a câmera de notebooks ou smartphones para capturar sinais.

## Como Funciona

1. O usuário faz um sinal na frente da câmera do notebook ou smartphone.
2. O sistema reconhece o sinal usando a biblioteca **MediaPipe** e traduz para um comando.
3. O comando é enviado via protocolo MQTT para um **Home Assistant**.
4. O Home Assistant lê o tópico e envia o comando ("Ligar TV" ou "Desligar TV") para o **Google Assistente**, que executa a ação.

## Tecnologias Usadas

- **MediaPipe**: Biblioteca para detecção de gestos, usada para identificar sinais.
- **Paho MQTT**: Biblioteca para comunicação via protocolo MQTT, usada para enviar comandos.
- **HiveMQ**: Broker MQTT público utilizado para facilitar a comunicação ([Link para HiveMQ](https://www.hivemq.com/)).
- **Home Assistant**: Sistema de automação residencial utilizado para controlar dispositivos conectados ([Link para Home Assistant](https://www.home-assistant.io/)).
- **Google Assistente**: Para executar comandos de automação, como ligar ou desligar dispositivos.

## Como Rodar o Projeto

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/fernandojeff/automacao-IOT-com-libras.git
   ```

2. **Instale as dependências**:
   ```bash
   pip install mediapipe paho-mqtt
   ```

3. **Configure o MQTT e o Home Assistant** conforme necessário, conectando-os ao seu ambiente.

4. **Execute o projeto**:
   ```bash
   python main.py
   ```

## Demonstração

Assista ao vídeo de demonstração no YouTube:  
[Assista aqui no YouTube](https://youtu.be/TL4cY7_vLdI?si=6Lp8w4B84YX1UHsq)

## Contribuições

Contribuições são sempre bem-vindas! Se você tem sugestões, melhorias ou correções, sinta-se à vontade para abrir um pull request.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).
