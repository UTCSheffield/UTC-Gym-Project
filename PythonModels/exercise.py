class Exercise(db.Model):
    id = db.Column(db.Integer, nullable=False)
    name = sa.Column(db.String, nullable=False)
    machine = sa.Column(db.String, nullable=False)
    measure = sa.Column(db.String, nullable=False)
