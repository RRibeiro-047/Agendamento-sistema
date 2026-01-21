from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)

# Configuração do banco de dados
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# Criar tabela se não existir
def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        servico TEXT NOT NULL,
        data TEXT NOT NULL,
        hora TEXT NOT NULL,
        data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

# Rota principal
@app.route("/")
def index():
    return render_template("index.html")

# Rota para agendamento
@app.route("/agendar", methods=["POST"])
def agendar():
    try:
        data = request.json
        
        # Validação dos dados
        if not all(key in data for key in ["nome", "servico", "data", "hora"]):
            return jsonify({"status": "error", "message": "Dados incompletos"}), 400

        # Conectar ao banco de dados
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Inserir no banco de dados
        cursor.execute("""
        INSERT INTO agendamentos (nome, servico, data, hora)
        VALUES (?, ?, ?, ?)
        """, (data["nome"], data["servico"], data["data"], data["hora"]))
        
        conn.commit()
        conn.close()
        
        return jsonify({
            "status": "success", 
            "message": "Agendamento realizado com sucesso!"
        })
        
    except sqlite3.Error as e:
        return jsonify({
            "status": "error",
            "message": f"Erro no banco de dados: {str(e)}"
        }), 500
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": f"Ocorreu um erro: {str(e)}"
        }), 500

# Inicializar o banco de dados quando o aplicativo iniciar
with app.app_context():
    init_db()


# Rota para o painel de administração
@app.route("/admin")
def admin():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        # Ordenar por data de criação, mais recentes primeiro
        cursor.execute("""
        SELECT id, nome, servico, data, hora, 
               strftime('%d/%m/%Y %H:%M', data_criacao) as data_formatada 
        FROM agendamentos 
        ORDER BY data_criacao DESC
        """)
        
        agendamentos = cursor.fetchall()
        conn.close()

        return render_template("admin.html", agendamentos=agendamentos)
    
    except sqlite3.Error as e:
        return f"Erro ao acessar o banco de dados: {str(e)}", 500
    except Exception as e:
        return f"Ocorreu um erro: {str(e)}", 500


if __name__ == "__main__":
    app.run(debug=True)
