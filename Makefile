.PHONY: install dev test lint fmt migrate seed demo types ui build-ui e2e serve

install:
	uv sync

dev:
	uv run uvicorn bluemage.main:create_app --factory --reload

test:
	uv run pytest -v

lint:
	uv run ruff check .

fmt:
	uv run ruff format .

migrate:
	uv run alembic -c server/alembic.ini upgrade head

seed: migrate
	uv run bluemage seed

demo: seed build-ui
	@echo "Now run 'make serve' and open http://localhost:8000"

types:
	uv run bluemage openapi > openapi.json
	cd frontend && npm run gen:types

ui:
	cd frontend && npm run dev

build-ui:
	cd frontend && npm ci && npm run build

e2e: build-ui
	cd frontend && npm run test:e2e

serve: build-ui migrate
	BLUEMAGE_FRONTEND_DIST=frontend/dist uv run uvicorn bluemage.main:create_app --factory --port 8000
