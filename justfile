_default:
  just --list

test:
  uv run pytest tests/ -v

test-coverage:
  uv run pytest tests/ -v --cov=render_engine_theme_kjaymiller --cov-report=term-out

lint:
  uv run ruff check src tests

typecheck:
  uv run ruff check src tests

check:
  just lint
  just test

merge:
    gh pr merge --squash -d

release version:
    gh release create {{version}} --generate-notes
