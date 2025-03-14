import hashlib
import base64
import string
import random

def derivar_chave(identificador: str, chave_mestra: str) -> str:
    """
    Usa PBKDF2-HMAC-SHA256 para derivar uma chave determinística a partir do identificador e chave mestra.
    Retorna um hash seguro e repetível.
    """
    salt = identificador.encode()  # Usa o identificador como salt fixo
    chave = hashlib.pbkdf2_hmac("sha256", chave_mestra.encode(), salt, 100000)
    
    # Codifica a chave em base64 para gerar um hash legível
    return base64.urlsafe_b64encode(chave).decode()

def gerar_senha(identificador: str, chave_mestra: str, comprimento: int = 16) -> str:
    """
    Gera uma senha forte e única para cada identificador, baseada em uma chave mestra.
    """
    chave_derivada = derivar_chave(identificador, chave_mestra)  # Chave determinística
    
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    
    # Usa a chave derivada como semente para um gerador aleatório determinístico
    random.seed(chave_derivada)
    senha = ''.join(random.choices(caracteres, k=comprimento))
    
    return senha

# 🛠 Exemplo de Uso
servico = "amon@gmail.com"
chave_mestra = "amon"

senha_gerada = gerar_senha(servico, chave_mestra)
print(f"Senha gerada: {senha_gerada}")
