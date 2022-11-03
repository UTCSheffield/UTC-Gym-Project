class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = sa.Column(db.String, primary_key=True)
    machine = sa.Column(db.String, primary_key=True)
    measure = sa.Column(db.String, primary_key=True)
