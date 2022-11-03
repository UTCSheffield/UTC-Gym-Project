class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #USER LINK
    date = db.Column(db.DateTime) # we don't know what all  the datatypes are
    height = db.Column(db.Integer)
    resting-heartrate = db.Column(db.Integer)
