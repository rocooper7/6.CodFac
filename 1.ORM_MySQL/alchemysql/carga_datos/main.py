import argparse
import logging
logging.basicConfig(level=logging.INFO)

import pandas as pd

from article import Article
from base import Base, engine, Session


logger = logging.getLogger(__name__)


def main(filename):
    Base.metadata.create_all(engine)
    session = Session()
    articles = pd.read_csv(filename,encoding='latin1')

    for index, row in articles.iterrows():
        logger.info('Loading article id {} into DB'.format(row['uid']))
        article = Article(row['uid'],
                          row['area'],
                          row['gerente'],
                          row['fecha'],
                          row['banda'],
                          row['calificacion'],
                          row['salario'],
                          row['seguro'])
        session.add(article)

    session.commit()
    session.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename',
                        help='The file you want to load into the db',
                        type=str)

    args = parser.parse_args()

    main(args.filename)
