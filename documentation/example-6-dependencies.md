# example-6-dependencies.yml

## Purpose
This workflow illustrates job dependencies using `needs` to enforce ordered execution.
It is a simple example of a common build-test-deploy pipeline.

## Trigger
- `workflow_dispatch`: workflow is started manually.

## Jobs and flow
- `build`
  - Runs first on `ubuntu-latest`.
  - Checks out the repository and echoes a build message.
- `test`
  - Depends on `build` with `needs: build`.
  - Checks out the repository and echoes a test message.
- `deploy`
  - Depends on `test` with `needs: test`.
  - Checks out the repository and echoes a deploy message.

## Key concepts
- `needs` creates dependencies between jobs.
- Jobs with `needs` wait for required jobs to finish successfully before starting.
- Each job has its own runner, so checkout is repeated in this example to access repository files.

## Notes
- Use `needs` to prevent downstream jobs from running if upstream jobs fail.
- This example repeats `actions/checkout@v4` in each job, which is common when each job needs repo files.
- For real workflows, replace the echo commands with actual build, test, and deployment tasks.
