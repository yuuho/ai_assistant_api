"""エンドポイントの定義
"""
from logging import getLogger
from pathlib import Path

from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from application import ChatGPT
from api_models.request import PromptReq
from auth import db_api, auth_api, database_initialize


logger = getLogger(__name__)
logger.info('loaded api_router.py')

origins = [
    "http://localhost:5173",
]


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class ApiServer:
    """APIサーバークラス
    """

    def __init__(self):
        self.api = FastAPI()

        self.api.add_middleware(
            CORSMiddleware,
            allow_origins=origins,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        self.api.add_api_route('/status', self.status, methods=["GET"])
        # self.api.add_api_route('/health', self.health, methods=["POST"])
        self.api.add_api_route('/chat', self.chat, methods=["POST"])

        # 認証機能
        database_initialize()
        self.api.include_router(db_api.router)
        self.api.include_router(auth_api.router)

        self.api.add_api_route('/secret', self.secret, methods=["POST"])

        # ルートに静的ファイルを置くときはAPI定義後に追加する
        static_path = str((Path(__file__).parent / 'static').resolve())
        self.api.mount('/', StaticFiles(directory=static_path, html=True),
                       name="static")

        self.chat_app = ChatGPT()

    def status(self):
        """サーバーステータスを表示
        """
        print('status ok!!')
        return {"status": "OK"}

    def health(self, req):
        """ヘルスチェック詳細情報を表示
        """
        print(req)
        return {"status": "OK"}

    def chat(self, req: PromptReq):
        """一回だけの応答
        """
        prompt = req.prompt
        ret = self.chat_app.chat(prompt)
        return {"result": ret}

    def secret(self, token: str = Depends(oauth2_scheme)):
        """ログインしていないと取得できない情報を返す
        """
        return {"result": f"secret info : {token}"}

    def launch(self, uvicorn_logconf):
        """サーバーを開始する
        """
        # TODO TBD: hot reload するには self.api を文字列として渡さなければいけない。
        # uvicorn.run(self.api, host="0.0.0.0", reload=True)
        uvicorn.run(self.api, host="0.0.0.0", log_level="debug",
                    log_config=uvicorn_logconf)
