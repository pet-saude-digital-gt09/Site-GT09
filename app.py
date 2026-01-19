from flask import Flask
from main_routes.routes import main_bp

# --- Configuração do Flask ---
app = Flask(__name__)

app.register_blueprint(main_bp)

# --- Roda o servidor ---
if __name__ == '__main__':
    app.run(debug=True)
