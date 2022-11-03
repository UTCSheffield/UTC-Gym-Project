class MuscleGroup(db.Model):
    id = db.Column(db.Integer, nullable=False)
    
    machine_id = Column(Integer, ForeignKey("Machine_table.id"))
    machine = relationship("Machine")
    
    name = sa.Column(db.String, nullable=False)
