import hashlib
import base64

def gerar_senha(identificador: str, chave_mestra: str, comprimento: int = 16) -> str:
    # Concatena o identificador (ex: email) com a chave mestra
    entrada = identificador + chave_mestra
    
    # Gera um hash SHA-256
    hash_bytes = hashlib.sha256(entrada.encode()).digest()
    
    # Converte o hash para base64 para ter caracteres mais variados
    senha = base64.b64encode(hash_bytes).decode('utf-8')
    
    # Remove caracteres especiais e limita o tamanho
    senha = ''.join(filter(str.isalnum, senha))[:comprimento]
    
    return senha

# Exemplo de uso
servico = str(input("Digite o identificador do serviço: "))
chave_mestra = "amon(editar)"

senha_gerada = gerar_senha(servico, chave_mestra)
print(f"Senha gerada: {senha_gerada}")
