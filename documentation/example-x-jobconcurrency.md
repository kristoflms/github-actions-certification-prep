# example-x-jobconcurrency.yml

## Purpose
This workflow shows how to use workflow-level `concurrency` to ensure only one run is active per branch.
It also demonstrates job dependencies and conditional deployment.

## Trigger
- `push` on branches `main` and `develop`.

## Concurrency setup
- `group: ${{ github.workflow }}-${{ github.ref }}`
  - Groups runs by workflow and branch.
  - Different branches get separate concurrency groups.
- `cancel-in-progress: true`
  - Cancels any in-progress run in the same concurrency group when a new run starts.

## Jobs and flow
- `build`
  - Runs on `ubuntu-latest`.
  - Checks out the repository and builds the application.
- `lint`
  - Runs in parallel with `build` because it has no `needs` dependency.
- `test`
  - Depends on `build` with `needs: build`.
  - Runs unit tests after the build completes.
- `deploy`
  - Depends on `build`, `lint`, and `test`.
  - Runs only on `refs/heads/main`.
  - Deploys to production after all required jobs succeed.

## Key concepts
- Workflow-level concurrency prevents duplicate runs for the same branch.
- `needs` controls job ordering and ensures dependent jobs wait for completion.
- `if: github.ref == 'refs/heads/main'` restricts deployment to the main branch.

## Use cases
- Preventing redundant CI builds when multiple commits arrive quickly.
- Running lint in parallel with build to shorten overall workflow time.
- Deploying only from the main branch after all checks pass.
