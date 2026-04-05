# Gradio Port Configuration Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Make Windows launches use a stable non-default Gradio port via `GRADIO_SERVER_PORT`.

**Architecture:** The Windows launcher sets the desired port in the environment, and Python reads that environment variable into the existing Gradio launch configuration. The browser helper reuses the same port value so both entry points stay aligned.

**Tech Stack:** Windows batch, Python, Gradio

---

### Task 1: Read Gradio port from environment

**Files:**
- Modify: `lib/conf.py`

**Step 1: Write the failing test**

Use manual verification for this config-only change.

**Step 2: Run test to verify it fails**

Run: launch without any code changes and observe Gradio still binds to `7860` even if the launcher sets a different desired port.

**Step 3: Write minimal implementation**

Change `interface_port` to use `int(os.environ.get("GRADIO_SERVER_PORT", "7860"))`.

**Step 4: Run test to verify it passes**

Run the app with `GRADIO_SERVER_PORT=8085` and verify the server binds to `8085`.

### Task 2: Keep Windows launcher and browser helper aligned

**Files:**
- Modify: `ebook2audiobook.cmd`

**Step 1: Write the failing test**

Use manual verification for this launcher change.

**Step 2: Run test to verify it fails**

Run: inspect current launcher values and observe the helper still targets `7860`.

**Step 3: Write minimal implementation**

Set `GRADIO_SERVER_PORT=8085` in the launcher and define `TEST_PORT=%GRADIO_SERVER_PORT%`.

**Step 4: Run test to verify it passes**

Launch with `ebook2audiobook.cmd` and confirm both Gradio and the helper use `8085`.
