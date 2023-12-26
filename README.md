# AI assistant API

言語、画像、音声などの AI 処理機能を提供。

- FastAPI + langchain


## HOWTO

### サーバーの起動とAPIの確認

1. OpenAI API Key を環境変数ファイルに記入 `.env`
2. Docker環境の起動 (下記いずれか)
    - `make start` or `docker compose up -d api_server`
    - VSCode "open in devcontainer"
3. (devcontainerのときのみ) サーバーの起動
    - `make start_service` or `python ai_assistant_api/__main__.py`
4. SwaggerUI でテスト
    - dockerを直接起動している場合 [localhost:8039/docs](localhost:8039/docs)
    - devcontainer の中でサーバーを起動している場合 [localhost:8038/docs](localhost:8038/docs)


### チャットの始め方

1. SwaggerUI に入る
2. `/users` の `Try it out` でユーザーを登録。
3. SwaggerUI 右上の `Authorize` でログイン。
    - `/users/me` でログインできているか確認ができる。
4. `/chat` の `Try it out` からチャットができることを確認。

