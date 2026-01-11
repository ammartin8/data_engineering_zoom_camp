FROM python:3.13.11-slim

# Adding uv dependecies in order to run uv and install packages using uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/ 

WORKDIR /code

# uv will be installed here and create a virtual environment
ENV PATH="/code/.venv/bin:$PATH"

COPY pyproject.toml .python-version uv.lock ./

# Install dependecies from the uv.lock file
RUN uv sync --locked

COPY pipeline/pipeline.py pipeline.py

ENTRYPOINT ["python", "pipeline.py"]
