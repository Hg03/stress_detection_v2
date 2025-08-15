FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim

WORKDIR /backend

COPY backend/pyproject.toml /backend/

COPY backend/ /backend/

# Install uv and sync dependencies
ENV UV_LINK_MODE=copy
ENV UV_NO_CACHE=1

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
RUN uv sync --no-cache

# Expose fastapi default port
EXPOSE 8080

# Use uv run to execute fastapi server
CMD ["uv", "run", "uvicorn", "app:app", "--port", "8080"]