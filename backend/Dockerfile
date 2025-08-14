FROM python:3.10-slim

WORKDIR /workspace

# Copy the entire backend directory (including its pyproject.toml)
COPY backend ./backend

# Change to backend directory where pyproject.toml exists
WORKDIR /workspace/backend

# Install uv and sync dependencies
ENV UV_LINK_MODE=copy
ENV UV_NO_CACHE=1

RUN pip install --no-cache-dir uv && \
    uv sync --no-cache

# Expose streamlit's default port
EXPOSE 8501

# Use uv run to execute fastapi server
CMD ["uv", "run", "uvicorn", "app:app", "--port", "8000"]