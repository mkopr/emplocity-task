import os

from emplocity import database
from emplocity.models import FileData
from emplocity.pdf_parsing import parse_pdf


def add_to_database():
    result = parse_pdf()
    name = os.path.basename(result['name'])
    pages = result['pages']
    data = result['data']
    data = data.decode('utf-8')
    characters = result['characters']
    words = result['words']
    lines = result['lines']

    if not FileData.query.filter_by(name=name).all():
        try:
            add_data = FileData(
                name=name,
                pages=pages,
                text=data,
                characters=characters,
                words=words,
                lines=lines,
            )
            database.session.add(add_data)
            database.session.commit()

        # If unique name is stored in database
        except:
            database.session.rollback()
            raise
        finally:
            database.session.close()
