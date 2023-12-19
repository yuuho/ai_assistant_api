"""サーバー起動
"""
import log_setting
from api_router import ApiServer


if __name__ == '__main__':
    apiserver = ApiServer()
    # サーバーの起動
    apiserver.launch(log_setting.get_uvicorn_logconf())
