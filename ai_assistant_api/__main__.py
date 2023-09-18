"""サーバー起動
"""
import log_setting  # noqa: F401
from api_router import ApiServer


if __name__ == '__main__':
    apiserver = ApiServer()
    apiserver.launch()
