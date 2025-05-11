DIR         := $(shell pwd)
CONTAINERS  := $(shell docker ps -aq)

compose: ## Building and Running apps with docker-compose
	@echo "Run application with docker"
	docker stop $(CONTAINERS) 2>/dev/null || true
	docker rm $(CONTAINERS) 2>/dev/null || true
	docker compose down --remove-orphans || true
	docker compose -f "docker-compose.yml" up --build
	@echo "Application is running"

test: ## Running a test
	@echo "Test application with docker"
	docker-compose run app pytest
