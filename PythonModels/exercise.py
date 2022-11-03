class Exercise(db.Model):
    id = db.Column(db.Integer, nullable)
    name = sa.Column(db.String, primary_key=True)
    machine = sa.Column(db.String, primary_key=True)
    measure = sa.Column(db.String, primary_key=True)
