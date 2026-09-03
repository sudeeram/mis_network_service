# Network Service

## Contribution workflow

Run `./scripts/setup-git-hooks.sh` once after cloning. All work must use a
`feature/*`, `hotfix/*`, or `bugfix/*` branch and reach `main` through a pull
request.

Independent Django service for network-domain features. It validates platform JWTs through the auth-service JWKS endpoint and owns its PostgreSQL database.

Real device connections and automation are intentionally outside the initial skeleton.

## Local development

```bash
uv sync --frozen
uv run python manage.py migrate
uv run python manage.py runserver
```

`uv` reads `.python-version`, creates an isolated `.venv`, and installs the exact
dependency versions recorded in `uv.lock`.
