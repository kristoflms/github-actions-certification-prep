# example-3-multiple-commands.yml

## Purpose
This workflow demonstrates running multiple shell commands inside a single workflow step.
It is useful when you want to execute a short script without splitting each command into separate steps.

## Trigger
- `workflow_dispatch`: workflow is started manually.

## Jobs and steps
- `Checkout repository`
  - Uses `actions/checkout@v3` to clone the repo.
  - Required if any of the commands need repository files.
- `Run multiple commands`
  - Uses YAML pipe syntax (`|`) to run multiple commands in one shell session.
  - Commands run sequentially in the same step.
  - Shows how to print text, list directory contents, print current path, and check the installed Node.js version.

## Key concepts
- Multiline `run` blocks are useful for small scripts.
- All commands in the block share the same shell environment.
- If one command fails, the entire step fails unless `continue-on-error` is used.

## Notes
- Use separate steps when you want each command to appear as its own workflow step.
- This example uses `node --version` to show the installed Node.js version on the runner.
- `ls -la` displays file details and can help confirm the checkout succeeded.
