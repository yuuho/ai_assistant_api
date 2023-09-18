.PHONY: start stop


# docker でサーバーを起動
start:
	docker compose up -d api_server

# サーバーを止める
stop:
	docker compose down
