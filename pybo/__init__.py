from flask import Flask

# migrate와  sql alchemy 라이브러리 임포트
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import MetaData

# config.py를 읽기 위한 config 라이브러리 임포트
import config

from flaskext.markdown import Markdown

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()

# create_app은 애플리케이션 팩토리 라고함(용어숙달요망)
def create_app():
    app = Flask(__name__)

    # config파일을 읽을 수 있게 app을 변조
    app.config.from_object(config)

    # 하기 두 줄이 app과 db,migrate를 연결하는 코드
    db.init_app(app)
    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)


    # models모듈에 정의한 클래스(=테이블)를 사용하기 위해 임포트
    from . import models

    # main_view에 정의한 bp 블루프린트 인스턴스를 app에 등록한다.
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    
    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime
    
    # markdown
    Markdown(app, extensions=['nl2br', 'fenced_code'])
    
    return app