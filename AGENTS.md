# Repository Guidelines

## Project Structure & Module Organization
`app.py` is the main CLI and Gradio entrypoint. Core application logic lives in `lib/`, with engine implementations under `lib/classes/tts_engines/` and shared runtime/config modules such as `lib/conf.py`, `lib/conf_lang.py`, and `lib/conf_models.py`. Docker assets are in the repository root plus `components/audiocraft/`. Test fixtures and sample inputs live in `tools/workflow-testing/` and `ebooks/tests/`. Generated outputs should stay in `audiobooks/`, while reusable voice and model assets belong in `voices/` and `models/`. Planning notes go in `docs/plans/`.

## Build, Test, and Development Commands
Use the project launchers for normal local development:

- `./ebook2audiobook.command` launches the Gradio UI on Unix-like systems.
- `python app.py --help` prints the full CLI surface when your environment is already set up.
- `./ebook2audiobook.command --headless --ebook tools/workflow-testing/test1.txt --language eng` runs a simple headless conversion smoke test.
- `docker compose --profile gpu up --no-log-prefix` starts the containerized app for GPU workflows.
- `docker compose --profile gpu run --rm ebook2audiobook --headless --ebook "/app/ebooks/myfile.pdf"` runs headless conversion in Compose.

## Coding Style & Naming Conventions
Follow the existing Python style in `app.py` and `lib/`: 4-space indentation, snake_case for functions and variables, PascalCase for classes, and uppercase constants for config values. Keep modules focused and place engine-specific behavior under `lib/classes/tts_engines/` instead of expanding `app.py`. No formatter or linter is configured in `pyproject.toml`, so match nearby code and keep imports and argument handling readable.

## Testing Guidelines
This repo relies primarily on smoke testing rather than a small unit-test suite. Reuse inputs from `tools/workflow-testing/` and `ebooks/tests/` when validating changes. At minimum, run `python app.py --help` and one headless conversion that exercises the code you touched. GitHub Actions in `.github/workflows/E2A-Test.yml` run broader end-to-end checks across supported engines; avoid merging changes that only work in the GUI path.

## Commit & Pull Request Guidelines
Recent history mixes short hotfix subjects such as `kilo-fix` with release tags like `v26.4.4`. Prefer short, imperative commit subjects that describe the functional change clearly. For pull requests, include the user-visible impact, the commands you ran to validate it, and any environment assumptions such as CPU/GPU or Docker mode. Add screenshots only when changing the Gradio UI.

## Security & Configuration Tips
Do not commit generated audiobooks, downloaded models, or local virtual environments such as `python_env/`. Treat `ebooks/` content as test data only, and use legally acquired, non-DRM inputs as noted in `README.md`.
