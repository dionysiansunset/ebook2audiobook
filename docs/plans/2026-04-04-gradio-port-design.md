# Gradio Port Configuration Design

## Goal

Make Windows launches use a fixed, configurable Gradio port so the app can be reopened reliably on the expected local URL.

## Recommended Approach

Use the existing `GRADIO_SERVER_PORT` environment variable as the single source of truth for the Gradio port, and set it in `ebook2audiobook.cmd` for Windows launches.

## Why This Approach

- It keeps the Windows launcher behavior simple and explicit.
- It matches Gradio's documented environment variable behavior.
- It avoids hardcoding a second unrelated port value in the Python app.
- It keeps the browser helper and the Gradio server on the same port.

## Required Changes

- Update `lib/conf.py` so `interface_port` reads from `GRADIO_SERVER_PORT`, defaulting to `7860`.
- Update `ebook2audiobook.cmd` to set `GRADIO_SERVER_PORT=8085` and reuse that value for `TEST_PORT`.

## Validation

- Launch `ebook2audiobook.cmd`.
- Confirm Gradio starts on `http://127.0.0.1:8085`.
- Confirm restarts reuse the same port.
