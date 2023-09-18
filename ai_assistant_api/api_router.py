"""エンドポイントの定義
"""
from logging import getLogger
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn

from application import ChatGPT
from api_models.request import PromptReq


logger = getLogger(__name__)
logger.info('loaded api_router.py')


class ApiServer:
    """APIサーバークラス
    """

    def __init__(self):
        self.api = FastAPI()

        self.api.add_api_route('/status', self.status, methods=["GET"])
        self.api.add_api_route('/health', self.health, methods=["POST"])
        self.api.add_api_route('/chat', self.chat, methods=["POST"])

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

    def launch(self):
        """サーバーを開始する
        """
        uvicorn.run(self.api, host="0.0.0.0")
