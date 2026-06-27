# example1-simple-workflow.yml

## Purpose
This workflow demonstrates a simple GitHub Actions workflow that is triggered manually.
It is useful for one-off commands, debugging, and workflows that should not run automatically on every push.

## Trigger
- `workflow_dispatch`: the workflow is started manually from the GitHub Actions UI.

## Jobs and steps
- `hello` job runs on `ubuntu-latest`.
- The single step prints `Hello, World!` to the workflow logs.

## What this teaches
- How to define a manually triggered workflow.
- How a job runs on a runner and executes shell commands.
- How to keep a workflow simple with a single job and step.

## Extensions
- Add `inputs` under `workflow_dispatch` to accept runtime parameters.
- Add more jobs to perform build, test, or deploy tasks.
- Use `runs-on` with different runner environments if needed.
