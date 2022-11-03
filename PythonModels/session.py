class Session(db.Model):
    id = db.Column(db.Integer,nullable=False)
    User = sa.Column(db.String, nullable=False)
    location = sa.Column(db.String, nullable=False)
    startDateTime = sa.Column(db.DateTime, nullable=False)
    endTime = sa.Column(db.DateTime, nullable=False)
