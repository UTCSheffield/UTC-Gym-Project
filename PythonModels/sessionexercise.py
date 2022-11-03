class SessionExercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #Session link?
    #Exercise link?
    #met lerel pex?
    start = db.Column(db.DateTime, nullable)
    end = db.Column(db.DateTime)
    reps = db.Column(db.Integer)
    
