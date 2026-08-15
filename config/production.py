from config.default import *

# db경로
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'a\x99qD\xb2\xe6}\x9b9\xa0\xc2\xdb\x04\xc9\xd6H'