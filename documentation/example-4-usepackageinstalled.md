# example-4-usepackageinstalled.yml

## Purpose
This workflow demonstrates installing a package on the runner and using conditional steps based on success or failure.
It shows how to dynamically install a tool before using it in the same job.

## Trigger
- `workflow_dispatch`: workflow is started manually.

## Jobs and steps
- `Install cowsay`
  - Runs `sudo apt-get update && sudo apt-get install -y cowsay`.
  - Updates the package cache and installs the `cowsay` package on the Ubuntu runner.
  - This step may fail if network or package installation issues occur.
- `Run cowsay`
  - Runs only if all previous steps in the job succeeded (`if: ${{ success() }}`).
  - Prints a message using the installed `cowsay` tool.
- `Installation failed message`
  - Runs only if a previous step in the job failed (`if: ${{ failure() }}`).
  - Prints a fallback message when the install step fails.

## Important details
- Each job runs on a fresh runner, so installing a package is necessary when the package is not available by default.
- The `success()` and `failure()` conditionals allow you to branch workflow behavior.
- `sudo apt-get install` can increase workflow runtime; consider caching or using prebuilt runner tools when available.

## Use cases
- Install CLI tools required only for certain workflows.
- Run a fallback or cleanup step when installation fails.
- Demonstrate conditional execution based on step outcome.
