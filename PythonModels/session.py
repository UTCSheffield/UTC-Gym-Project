class Session(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    User = sa.Column(db.String, primary_key=True)
    location = sa.Column(db.String, primary_key=True)
    startDateTime = sa.Column(db.DateTime, primary_key=True)
    endTime = sa.Column(db.DateTime, primary_key=True)
