class SessionExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #Session link?
    #Exercise link?
    #met lerel pex?
    start = db.Column(db.DateTime, nullable=False)
    end = db.Column(db.DateTime, nullable=False)
    reps = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float, nullable=False)
    
