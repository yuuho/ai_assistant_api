# AI assistant API

言語、画像、音声などの AI 処理機能を提供。

- FastAPI + langchain


## HOWTO

1. OpenAI API Key を環境変数ファイルに記入 `.env`
2. Docker環境の起動 (下記いずれか)
    - `make start` or `docker compose up -d api_server`
    - VSCode "open in devcontainer"
3. (devcontainerのときのみ) サーバーの起動
    - `make start_service` or `python ai_assistant_api/__main__.py`
4. SwaggerUI でテスト [localhost:8039/docs](localhost:8039/docs)
