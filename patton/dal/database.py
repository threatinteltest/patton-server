from contextlib import contextmanager

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

from patton.config import DB_URL


engine = sqlalchemy.create_engine(DB_URL, client_encoding='utf8')


Base = declarative_base()


@contextmanager
def session_ctx(*args, **kwargs):
    session = Session(*args, bind=engine, **kwargs)
    try:
        session.begin(subtransactions=True)
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


# INFO: we need to `load` to Base the Models
from . import models  # noqa

Base.metadata.create_all(engine)