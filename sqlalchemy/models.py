from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

# cria aengine do banco
engine = create_engine('sqlite:///atividades.db', convert_unicode=True)

# commita automatico
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))

Base = declarative_base()

Base.query = db_session.query_property()


class Pessoas(Base):
    __tablename__ = 'pessoas'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return f'<pessoa {self.nome}>'


class Atividades(Base):
    __tablename__ = 'atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    # relacionando tabela
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoas')


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()