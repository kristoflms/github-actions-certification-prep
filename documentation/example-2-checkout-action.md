# example-2-checkout-action.yml

## Purpose
This workflow shows how to checkout the repository and inspect the runner workspace.
It is a good example for verifying that the repository files are available to later workflow steps.

## Trigger
- `workflow_dispatch`: workflow is started manually from the Actions tab.

## Jobs and steps
- `Checkout repository`
  - Uses `actions/checkout@v7`.
  - Clones the repository into the runner workspace so steps can access source files.
- `List repository files`
  - Runs `ls -ltra` to list all files in the working directory.
  - Shows hidden files, file permissions, size, and timestamps.

## Why checkout is important
Each GitHub Actions job starts on a fresh runner by default.
If you need repository files in a workflow step, you must checkout the repo first.

## Use cases
- Validate the repository layout inside the workflow environment.
- Debug path or environment issues before running build or test commands.
- Use as a template for workflows that need access to source files.
