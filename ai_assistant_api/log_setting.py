"""logging の初期化
"""
from logging import config
import os
from pathlib import Path

import yaml


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

# logging 設定に従って構成する
config.dictConfig(dict_conf)
