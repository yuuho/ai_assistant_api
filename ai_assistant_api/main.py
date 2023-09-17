"""doc
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import uvicorn


class ApiServer:
    """APIサーバークラス
    """

    def __init__(self):
        self.app = FastAPI()

        self.app.add_api_route('/status', self.status)
        self.app.add_api_route('/health', self.health)

        # ルートに静的ファイルを置くときはAPI定義後に追加する
        static_path = str((Path(__file__).parent / 'static').resolve())
        self.app.mount('/', StaticFiles(directory=static_path, html=True),
                       name="static")

    def status(self):
        """サーバーステータスを表示
        """
        return {"status": "OK"}

    def health(self, req):
        """ヘルスチェック詳細情報を表示
        """
        print(req)
        return {"status": "OK"}

    def launch(self):
        """サーバーを開始する
        """
        uvicorn.run(self.app, host="0.0.0.0")


if __name__ == '__main__':
    apiserver = ApiServer()
    apiserver.launch()
