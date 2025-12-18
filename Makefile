POETRY ?= poetry
ENV_FILE ?= .env
ENV_EXAMPLE ?= .env.example
APP_MODULE := src.main:app
APP_HOST ?= 0.0.0.0
APP_PORT ?= 8000

ifneq ("$(wildcard $(ENV_FILE))","")
	include $(ENV_FILE)
	export $(shell sed -n 's/^[[:space:]]*//;s/#.*//;/^[A-Za-z_][A-Za-z0-9_]*=/p' $(ENV_FILE) 2>/dev/null | cut -d= -f1)
endif

.PHONY: help env install api test lint format

help:
	@echo "Targets:"
	@echo "  env     Copia $(ENV_EXAMPLE) para $(ENV_FILE) se ainda nao existir."
	@echo "  install Instala dependencias com Poetry."
	@echo "  api     Sobe a API FastAPI com hot reload."
	@echo "  test    Roda a suite de testes."
	@echo "  lint    Roda flake8 e mypy basico."
	@echo "  format  Roda black e isort."

env:
	@if [ ! -f $(ENV_FILE) ]; then cp $(ENV_EXAMPLE) $(ENV_FILE); echo "Arquivo $(ENV_FILE) criado a partir de $(ENV_EXAMPLE)."; else echo "$(ENV_FILE) ja existe - nada a fazer."; fi

install:
	$(POETRY) install

api:
	$(POETRY) run uvicorn $(APP_MODULE) --host $(APP_HOST) --port $(APP_PORT) --reload

test:
	$(POETRY) run pytest

lint:
	$(POETRY) run flake8 src
	$(POETRY) run mypy src

format:
	$(POETRY) run black src
	$(POETRY) run isort src
