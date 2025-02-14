# Script de Automação de Airdrops Web3

Este projeto é um script de automação desenvolvido em Python utilizando a biblioteca `pyautogui` para automatizar o processo de farming de airdrops Web3 nas plataformas Functor e Plaza Network. O script foi projetado para ser executado uma vez por dia e realiza ações como abrir navegadores, acessar páginas de airdrops, conectar carteiras e realizar operações de compra e venda de tokens.

## Funcionalidades Principais

### Automação de Airdrops:
- **Functor**: Funciona em qualquer navegador, mas foi testado no Brave e Chrome.
- **Plaza Network**: Configurado para abrir no Brave, acessando diretamente pela barra de favoritos (clicando na primeira opção).

### Execução Diária:
- O script é projetado para rodar uma vez por dia.

### Segurança:
- O código é seguro e não contém arquivos maliciosos. Pode ser verificado por ferramentas como o ChatGPT para análise.

## Requisitos

- **Python 3.x**: Certifique-se de ter o Python instalado em sua máquina.

### Bibliotecas Python:
- `pyautogui`: Para controle do mouse e teclado.
- `subprocess`: Para executar comandos do sistema.
- `os`: Para manipulação de arquivos e diretórios.
- `datetime`: Para manipulação de datas e horários.
- `random`: Para gerar números aleatórios.

Instale as bibliotecas necessárias utilizando o comando:
```bash
pip install pyautogui
```
  # Como Usar

## 1. Baixe o Python
Se você ainda não tem o Python instalado, baixe e instale a versão mais recente do [site oficial](https://www.python.org/).

## 2. Crie um Atalho na Inicialização
- Pressione `WIN + R`, digite `shell:startup` e pressione `Enter`.
- Crie um atalho para o script Python na pasta que abrir. Isso fará com que o script seja executado automaticamente ao iniciar o computador.

## 3. Execute o Script
- Execute o script manualmente ou aguarde a execução automática na inicialização.

## 4. Verifique o Log
- O script gera um arquivo de log chamado `registro_acao.txt` no mesmo diretório, onde são registradas todas as ações realizadas.

---

# Personalização

## Resolução da Tela
O script foi otimizado para telas com resolução 1920x1080. Se a resolução da sua tela for diferente, ajuste as coordenadas do mouse no código.

## Navegador
O script foi testado no Brave e Chrome. Para outros navegadores, ajuste os caminhos e comandos conforme necessário.

## Tempos de Espera
Os tempos de espera (`time.sleep`) podem ser ajustados conforme a velocidade de carregamento das páginas.

---

# Aviso Importante

## Risco de Sybil
Este tipo de automação pode ser interpretado como um comportamento sybil (identificação de múltiplos usuários ou bots para fins de manipulação). Ao rodar este script, você pode ser identificado como um sybil, o que pode afetar sua participação em algumas plataformas, dependendo das regras delas.

## Use por Sua Conta e Risco
O script foi desenvolvido para fins educacionais e de automação de tarefas repetitivas. Certifique-se de que o uso deste script esteja em conformidade com os termos de serviço das plataformas envolvidas.

---

# Segurança
O código é seguro e não contém arquivos maliciosos. Se você tiver dúvidas sobre a segurança do script, pode pedir para o ChatGPT ou outra ferramenta de análise de código verificar o arquivo.

---

# Contribuição
Sinta-se à vontade para contribuir com melhorias, correções de bugs ou novas funcionalidades. Abra uma issue ou envie um pull request.
