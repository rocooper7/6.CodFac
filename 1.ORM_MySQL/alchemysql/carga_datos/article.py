from sqlalchemy import Column, String, Integer,VARCHAR,Text,Date,Float

from base import Base


class Article(Base):
    __tablename__ = 'carga'

    id = Column(VARCHAR(10),primary_key=True)
    area = Column(Text)
    gerente = Column(Text)
    fecha = Column(Text)
    banda = Column(Text)
    calificacion = Column(Integer)    
    salario = Column(Float)    
    seguro = Column(Float)

    def __init__(self, uid, area, gerente, fecha, banda, calificacion, salario, seguro):
        self.id = uid
        self.area = area
        self.gerente = gerente
        self.fecha = fecha
        self.banda = banda    
        self.calificacion = calificacion
        self.salario = salario
        self.seguro = seguro
        

