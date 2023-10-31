.PHONY: start stop


# docker でサーバーを起動
start:
	docker compose up -d api_server

# サービスの起動
start_service:
	python ai_assistant_api/__main__.py

# サーバーを止める
stop:
	docker compose down
