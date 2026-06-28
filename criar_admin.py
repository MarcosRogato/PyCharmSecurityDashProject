from werkzeug.security import generate_password_hash
from database import conectar, criar_tabela_usuarios, inserir_usuario

criar_tabela_usuarios()
senha_hash = generate_password_hash('admin123')
inserir_usuario('admin', senha_hash)
print("Usuário admin criado com sucesso!")
