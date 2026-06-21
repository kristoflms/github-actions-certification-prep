# example-4-usepackagenotinstalled.yml

## Purpose
This workflow illustrates a failure scenario when a workflow assumes a tool is installed but it is not available on the runner.
It is useful for learning why package installation is important in GitHub Actions.

## Trigger
- `push` to the `main` branch.

## Jobs and steps
- `Run cowsay without installing`
  - Executes `cowsay` directly.
  - On a standard `ubuntu-latest` runner, `cowsay` is not guaranteed to be installed.
  - The step is expected to fail unless a previous step or workflow setup installs the package.

## Lessons
- GitHub Actions runners provide a base image with common tools, but not every package is present.
- If your workflow depends on a tool, install it explicitly or use a runner image that includes it.
- A failed step stops the job by default unless `continue-on-error: true` is used.

## Notes
- This workflow does not include `actions/checkout` because the command does not depend on repository files.
- Use this pattern to test and debug missing dependencies before adding package installation steps.
