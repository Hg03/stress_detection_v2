FROM ghcr.io/astral-sh/uv:python3.10-bookworm-slim

WORKDIR /workspace

COPY frontend/pyproject.toml /workspace/

# Change to backend directory where pyproject.toml exists
COPY . /workspace/

# Install uv and sync dependencies
ENV UV_LINK_MODE=copy
ENV UV_NO_CACHE=1

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*
RUN uv sync --no-cache

# Expose streamlit's default port
EXPOSE 8501

# Use uv run to execute streamlit
CMD ["uv", "run", "streamlit", "run", "frontend/app.py", "--server.port", "8501"]