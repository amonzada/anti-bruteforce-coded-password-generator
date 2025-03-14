# Gerador "Determinístico" de Senhas (Anti-BruteForce)

## ❓ Contexto e Necessidade

Com o aumento do número de serviços online, lembrar de senhas seguras para cada plataforma se tornou um desafio. Muitas pessoas reutilizam senhas, o que as torna vulneráveis a ataques como vazamentos de dados e força bruta.

Este gerador de senhas resolve esse problema ao permitir que você memorize **apenas uma chave mestra**, a partir da qual todas as suas senhas são geradas de forma **determinística e segura**. Assim, não há necessidade de armazenar senhas individuais, pois elas podem ser recriadas sempre que necessário.

## 🔐 Impacto na Segurança Digital

- Evita a reutilização de senhas
- Garante que cada site tenha uma senha única
- Usa algoritmos criptográficos seguros
- Permite a criação de senhas fortes sem precisar armazená-las

⚠️ **Vulnerabilidades a considerar:**
- Se alguém descobrir sua **chave mestra**, poderá gerar todas as suas senhas. **Use uma chave mestra forte**
- Você precisará do script sempre que quiser recuperar uma senha. **Faça backup do script**
- **Recomenda-se ativar 2FA** (autenticação de dois fatores) sempre que possível.
- Para serviços essenciais (bancos, emails principais), **considere anotar a senha e guardá-la em local seguro**.

---

## 🚀 Como Funciona
O gerador utiliza **hashes criptográficos** para transformar um identificador (exemplo: e-mail ou site) e uma chave mestra em uma senha segura e única.

Dois métodos são disponibilizados:
- **Gerador Simples:** Utiliza SHA-256 para criar senhas a partir da combinação do identificador e chave mestra.
- **Gerador Completo:** Usa PBKDF2-HMAC-SHA256 para aumentar a segurança e gera senhas mais complexas.

---

## 🛠 Como Usar
### Clone o repositório e execute o script:

```bash
git clone https://github.com/amonzada/anti-bruteforce-coded-password-generator
cd anti-bruteforce-coded-password-generator
python gerador_x.py
```

- Insira seu identificador e chave mestra (no arquivo), e o sistema gerará sua senha.

### Gerador Simples

📌 **Explicação:**
- Usa SHA-256 para gerar um hash único.
- Converte o hash para Base64 para aumentar a variabilidade dos caracteres.
- Remove caracteres especiais e corta a senha para o comprimento desejado.

🔸 **Desvantagem:** Menos seguro que o método completo, pois não usa um salt robusto.

---

### Gerador Completo

📌 **Explicação:**
- Usa **PBKDF2-HMAC-SHA256** para criar um hash seguro com 100.000 iterações.
- O **identificador** é usado como um salt fixo, garantindo que cada site tenha uma senha única.
- A chave derivada serve como **semente** para um gerador aleatório determinístico.
- Garante senhas fortes e complexas, com letras, números e caracteres especiais.

✅ **Vantagens:**
- Muito mais seguro do que o método simples.
- Difícil de inverter ou quebrar sem a chave mestra.

---

## 🛠 Contribuições e Futuro

Estou trabalhando em uma forma de manter o script acessível e seguro na maior parte do tempo.

Então assim que eu puder, vou trazer novas atualizações, como uma extensão para navegador.

Sinta-se à vontade para sugerir melhorias, abrir issues e enviar pull requests! 🚀

🔒 **Mantenha sua chave mestra segura!** 🔒
