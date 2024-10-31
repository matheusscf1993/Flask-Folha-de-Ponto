# app/models.py
from app import db
from datetime import datetime

class Ponto(db.Model):
    __tablename__ = 'ponto'

    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(50), nullable=False)
    horario_entrada = db.Column(db.DateTime, default=datetime.utcnow)
    horario_saida = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Ponto {self.usuario} - Entrada: {self.horario_entrada}, Saída: {self.horario_saida}>'
