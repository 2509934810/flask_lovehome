# from sqlalchemy import create_engine, MetaData
# from sqlalchemy.orm import scoped_session, sessionmaker

# from backend import app

# engine = create_engine(app.config['DATABASE'], convert_unicode=True)
# metadata = MetaData()
# db_session = scoped_session(sessionmaker(bind=engine, autocommit=False, autoflush=False))

# def init_db():
#     metadata.create_all(bind=engine)