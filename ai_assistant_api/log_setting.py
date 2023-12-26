"""logging の初期化
"""
import logging
from logging import config
import os
from pathlib import Path

import uvicorn
import yaml


def get_logconf():
    """ログ設定ファイルから設定オブジェクトを作成

    ログ設定ファイルを読み込み、ログ出力先等のパス設定をしつつ
    dict 形式でログ設定を作成
    """
    # ログ出力ディレクトリ
    LOGDIR = os.environ.get('AI_ASSISTANT_LOGDIR', 'var/logs')

    # logging 設定ファイルの読み込み
    config_file_path = (Path(__file__).parent / 'logconf.yaml').resolve()
    dict_conf = yaml.load(config_file_path.read_text(), Loader=yaml.FullLoader)

    # logファイル保存用ディレクトリがなければ作成
    # log保存ルートディレクトリが指定されていれば置き換え
    for v in dict_conf['handlers'].values():
        if 'filename' not in v.keys():
            continue
        v['filename'] = v['filename'].replace('$LOGDIR', LOGDIR)
        Path(v['filename']).parent.mkdir(parents=True, exist_ok=True)

    return dict_conf


def get_uvicorn_logconf():
    """TODO

    uvicorn に渡すログ設定を作成
    """
    return uvicorn.config.LOGGING_CONFIG


''' uvicorn のデフォルト設定
{'version': 1,
 'disable_existing_loggers': False,
 'formatters': {
    'default': {'()': 'uvicorn.logging.DefaultFormatter',
                'fmt': '%(levelprefix)s %(message)s', 'use_colors': None},
    'access': {'()': 'uvicorn.logging.AccessFormatter',
                'fmt': '%(levelprefix)s %(client_addr)s -
                                "%(request_line)s" %(status_code)s'}},
 'handlers': {
    'default': {'formatter': 'default', 'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stderr'},
    'access': {'formatter': 'access', 'class': 'logging.StreamHandler',
                'stream': 'ext://sys.stdout'}},
 'loggers': {
    'uvicorn': {'handlers': ['default'], 'level': 'INFO', 'propagate': False},
    'uvicorn.error': {'level': 'INFO'},
    'uvicorn.access': {'handlers': ['access'], 'level': 'INFO',
                        'propagate': False}}}
'''


class Util:

    # デバッグ用途: ロガーを文字列に
    @staticmethod
    def logger2string(lg):
        string = str(id(lg))
        if type(lg) is logging.PlaceHolder:
            return string
        else:
            for hd in sorted(lg.handlers, key=lambda x: id(x)):
                string += '_'+str(id(hd))
        return string

    # デバッグ用途: 存在するすべてのロガーを文字列化
    @staticmethod
    def get_logger_tree():
        return {k: Util.logger2string(v) for k, v in
                logging.getLogger().manager.loggerDict.items()}

    # 全ロガーの比較
    @staticmethod
    def compare_logger_tree(tree1, tree2):
        string = ""
        for k in tree1:
            if tree2[k] == tree1[k]:
                continue
            string += f'{str(k)} : {str(tree2[k])} -> {str(tree1[k])}\n'
        return string

    # 全ロガーの名前を取得
    @staticmethod
    def get_logger_set():
        return set([str(x) for x, _ in
                    logging.getLogger().manager.loggerDict.items()])


# logging 設定に従って構成する
config.dictConfig(get_logconf())
