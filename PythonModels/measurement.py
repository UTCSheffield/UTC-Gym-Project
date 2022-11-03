class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #USER LINK
    date = db.Column(db.DateTime, nullable=False) # we don't know what all  the datatypes are
    height = db.Column(db.Integer, nullable=False)
    resting-heartrate = db.Column(db.Integer, nullable=False)
