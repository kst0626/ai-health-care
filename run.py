from waitress import serve
from app import create_app
import os

app = create_app()

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))  # 환경 변수 PORT에서 포트 번호를 가져오고, 기본값으로 8080을 사용합니다
    serve(app, host='0.0.0.0', port=port)  # 0.0.0.0으로 설정하여 모든 IP에서 접근 가능하도록 합니다

