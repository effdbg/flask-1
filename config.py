# SQLalchemy를 사용해 파이썬코드를 sqlite 쿼리로 변경하는 구성파일이다

import os

BASE_DIR = os.path.dirname(__name__)

# 데이터베이스 경로
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))

# 이벤트 처리 옵션, 이 옵션은 파이보(지금 다루는 라우팅)에 필요하지 않으므로 false로 설정
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "dev"