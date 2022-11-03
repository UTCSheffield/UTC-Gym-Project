class Machine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, nullable=False)
    muscle_group = db.Column(db.String, nullable=False)
