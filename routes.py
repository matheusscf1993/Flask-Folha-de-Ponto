# app/routes.py
from flask import request, jsonify
from datetime import datetime
from models import Ponto
from app import db


def register_routes(app):
    # Rota para registrar a entrada
    @app.route('/ponto/entrada', methods=['POST'])
    def registrar_entrada():
        dados = request.get_json()
        usuario = dados.get('usuario')

        if not usuario:
            return jsonify({"error": "Usuário é obrigatório"}), 400

        novo_ponto = Ponto(usuario=usuario)
        db.session.add(novo_ponto)
        db.session.commit()

        return jsonify({"message": "Entrada registrada com sucesso"}), 201

    # Rota para registrar a saída
    @app.route('/ponto/saida/<int:ponto_id>', methods=['POST'])
    def registrar_saida(ponto_id):
        ponto = Ponto.query.get(ponto_id)

        if not ponto:
            return jsonify({"error": "Registro de entrada não encontrado"}), 404
        if ponto.horario_saida:
            return jsonify({"error": "Saída já registrada para este ponto"}), 400

        ponto.horario_saida = datetime.utcnow()
        db.session.commit()

        return jsonify({"message": "Saída registrada com sucesso"}), 200

    # Rota para listar todos os pontos
    @app.route('/pontos', methods=['GET'])
    def listar_pontos():
        pontos = Ponto.query.all()
        resultado = [{"usuario": p.usuario, "entrada": p.horario_entrada, "saida": p.horario_saida} for p in pontos]
        return jsonify(resultado)
