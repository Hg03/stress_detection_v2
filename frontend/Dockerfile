FROM python:3.10-slim

WORKDIR /workspace

COPY frontend/pyproject.toml /workspace/

# Change to backend directory where pyproject.toml exists
COPY . /workspace/

# Install uv and sync dependencies
ENV UV_LINK_MODE=copy
ENV UV_NO_CACHE=1

RUN pip install --no-cache-dir uv && \
    uv sync --no-cache

# Expose streamlit's default port
EXPOSE 8501

# Use uv run to execute streamlit
CMD ["uv", "run", "streamlit", "run", "frontend/app.py", "--server.port", "8501"]