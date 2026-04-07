# Repository Guidelines

## Project Structure & Module Organization
`app.py` is the main CLI and Gradio entrypoint. Core application logic lives in `lib/`, with engine integrations under `lib/classes/tts_engines/` and shared configuration in `lib/conf*.py`. Utility and maintenance scripts are in `tools/`. Container-specific pieces live in `components/` and `dockerfiles/`. Treat `ext/py/` as vendored upstream code, and avoid editing `models/`, `voices/`, `run/`, `tmp/`, and `audiobooks/` unless your change is explicitly about generated assets or runtime data.

## Build, Test, and Development Commands
Install dependencies with `pip install -r requirements.txt` for local development, or `pip install -e .` to register the `ebook2audiobook` console script. Use `python app.py --help` to inspect supported flags and `python app.py --share` to launch the web UI. For headless conversion, use `python app.py --headless --ebook ebooks/tests/<file> --language eng`. Build the container with `docker build -f Dockerfile -t ebook2audiobook .` when validating Docker changes.

## Coding Style & Naming Conventions
Follow existing Python conventions: 4-space indentation, `snake_case` for functions and variables, `PascalCase` for classes, and concise module-level helpers. Keep configuration changes centralized in `lib/conf.py` or the relevant `conf_*` module instead of scattering constants. Match the surrounding style in legacy files before refactoring. There is no enforced formatter in this repo, so keep imports tidy and favor small, reviewable changes.

## Testing Guidelines
Automated coverage is limited, so contributors should verify the exact path they changed. Use sample inputs from `ebooks/tests/` for manual conversion checks. Run targeted helper scripts directly, for example `python tools/gpu_test.py` or `python tools/m4b_chapter_extractor.py --help`, when touching those areas. If you add tests, place them near the relevant tool or under a dedicated `tests/` package and name them `test_<feature>.py`.

## Commit & Pull Request Guidelines
Recent history is heavily release-oriented (`v26.4.4`, date-based tags), so for normal development prefer short imperative commit subjects such as `Fix XTTS language fallback`. Keep commits scoped to one concern. Pull requests should include a concise summary, manual test notes, platform details when relevant (`Linux`, `macOS`, `Windows`, `Docker`), and screenshots for GUI changes. Link the related issue when one exists.

## Security & Configuration Tips
Do not commit private ebooks, cloned voices, API secrets, or generated audiobooks. Large model and voice assets should stay out of git unless the repository already tracks them intentionally. Preserve the README’s legal constraint: this project is for non-DRM, legally acquired ebooks only.
