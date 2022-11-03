class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = sa.Column(sa.Integer, primary_key=True)
    machine = sa.Column(sa.Integer, primary_key=True)
    measure = sa.Column(sa.Integer, primary_key=True)
