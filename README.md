# GitHub Setup Script

Script em Python para automatizar a configuração inicial do Git e GitHub, facilitando o processo de configuração do ambiente de desenvolvimento.

## Funcionalidades

- Configuração automática do Git com nome de usuário e email
- Geração de chave SSH para autenticação no GitHub
- Validação de email e inputs
- Teste de conexão com o GitHub
- Verificação de dependências (Git)

## Requisitos

- Python 3.6 ou superior
- Git instalado no sistema

## Como Usar

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/github-setup-script.git
cd github-setup-script
```

2. Execute o script:

```bash
python github_setup.py
```

3. Siga as instruções na tela:
   - Digite seu email do GitHub
   - Digite seu nome de usuário do GitHub
   - O script irá configurar o Git e gerar sua chave SSH
   - Adicione a chave SSH ao seu GitHub conforme as instruções

## O que o Script Faz

1. **Verificação de Dependências**

   - Verifica se o Git está instalado no sistema

2. **Configuração do Git**

   - Configura o nome de usuário global
   - Configura o email global
   - Valida o formato do email

3. **Geração de Chave SSH**

   - Gera uma chave SSH ED25519
   - Salva a chave no diretório ~/.ssh
   - Exibe a chave pública para adicionar ao GitHub

4. **Teste de Conexão**
   - Testa a conexão SSH com o GitHub
   - Verifica se a autenticação está funcionando

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

