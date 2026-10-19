---
name: visual-tester
description: Capture visual screenshots with Playwright, inspect rendered DOM/UI, and validate visual appearance of frontend changes
argument-hint: "[URL] [SELECTOR]"
---

# Visual Tester Skill

Use this skill to visually verify UI changes in a browser using Playwright headless screenshots.

## Instructions
1. Verify dev server is up: `curl -sI http://localhost:3000`
2. Take a screenshot with `snap-page`:
   ```bash
   # Full page
   snap-page http://localhost:3000 /tmp/screenshot.png

   # Specific component or selector
   snap-page http://localhost:3000 /tmp/component.png .finding-panel-card
   ```
3. Inspect screenshot path, confirm layout/styles, and report visual evidence.
4. Format output (Caveman): `[target] OK file:///tmp/screenshot.png. [observations].`
