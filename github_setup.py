import subprocess
import os
import sys
import re
from pathlib import Path

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar comando: {command}")
        print(f"Mensagem de erro: {e.stderr}")
        sys.exit(1)
    except Exception as e:
        print(f"Erro inesperado: {str(e)}")
        sys.exit(1)

def check_git_installed():
    try:
        subprocess.run(['git', '--version'], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Git não está instalado! Por favor, instale o Git primeiro.")
        print("Você pode baixar o Git em: https://git-scm.com/downloads")
        sys.exit(1)

def configure_git(email, name):
    if not validate_email(email):
        print("Email inválido! Por favor, insira um email válido.")
        return False
    
    print("Configurando Git...")
    try:
        run_command(f'git config --global user.email "{email}"')
        run_command(f'git config --global user.name "{name}"')
        print("Configuração do Git concluída com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao configurar Git: {str(e)}")
        return False

def generate_ssh_key(email):
    ssh_dir = Path.home() / '.ssh'
    ssh_dir.mkdir(exist_ok=True)
    
    key_path = ssh_dir / 'id_ed25519'
    
    if key_path.exists():
        print("Chave SSH já existe. Pulando geração.")
        return True
    
    print("Gerando chave SSH...")
    try:
        run_command(f'ssh-keygen -t ed25519 -C "{email}" -f "{key_path}" -N ""')
        print("Chave SSH gerada com sucesso!")
        return True
    except Exception as e:
        print(f"Erro ao gerar chave SSH: {str(e)}")
        return False

def display_public_key():
    key_path = Path.home() / '.ssh' / 'id_ed25519.pub'
    if not key_path.exists():
        print("Chave pública não encontrada!")
        return False
    
    try:
        with open(key_path, 'r') as f:
            public_key = f.read().strip()
        
        print("\nSua chave SSH pública é:")
        print("-" * 50)
        print(public_key)
        print("-" * 50)
        print("\nPor favor, adicione esta chave à sua conta GitHub:")
        print("1. Acesse GitHub.com")
        print("2. Clique na sua foto de perfil → Configurações")
        print("3. Clique em 'SSH and GPG keys' → 'New SSH key'")
        print("4. Cole sua chave e salve")
        return True
    except Exception as e:
        print(f"Erro ao ler chave pública: {str(e)}")
        return False

def test_github_connection():
    print("\nTestando conexão com GitHub...")
    try:
        result = subprocess.run(['ssh', '-T', 'git@github.com'], capture_output=True, text=True)
        if "successfully authenticated" in result.stderr.lower():
            print("Conexão com GitHub estabelecida com sucesso!")
            return True
        else:
            print("Não foi possível conectar ao GitHub. Verifique se você adicionou a chave SSH corretamente.")
            return False
    except Exception as e:
        print(f"Erro ao testar conexão: {str(e)}")
        return False

def main():
    print("Script de Configuração do GitHub")
    print("-" * 30)
    
    check_git_installed()
    
    while True:
        email = input("Digite seu email do GitHub: ").strip()
        if validate_email(email):
            break
        print("Email inválido! Por favor, tente novamente.")
    
    name = input("Digite seu nome de usuário do GitHub: ").strip()
    while not name:
        print("Nome de usuário não pode estar vazio!")
        name = input("Digite seu nome de usuário do GitHub: ").strip()
    
    if configure_git(email, name):
        if generate_ssh_key(email):
            if display_public_key():
                test_github_connection()

if __name__ == "__main__":
    main() 