from flask import Blueprint, url_for, current_app

from flask import render_template
from werkzeug.utils import redirect

# 첫 번째 인자 'main'은 이 블루프린트의 alias이다. < 이는 url_for 함수에서 자주 사용된다.

# 첫 번째 인자 'main'은 별칭임(사용자 정의)!
# 두 번째 인자 __name__에 의해 'main_views'가 인자로 전달됨
# 세 번째 기본 매개변수로 전달된 인자 '/'에 의해 최상위 경로는 /가 됨
# url_prefix에 대한 추가설명 -> 만약 /main/으로 지정했다면 hello_pybo 라우팅 함수를 호출하는 최상위 경로는 localhost:5000/main/가 되는 것
bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello/')
def hello_pybo():
    return 'Hello, Pybo!'

# 루트경로로 접근 시 리턴되는 템플릿
@bp.route('/')
def index():
    current_app.logger.info("INFO 레벨로 출력")
    return redirect(url_for('question._list'))