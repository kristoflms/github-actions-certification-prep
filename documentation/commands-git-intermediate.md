# Intermediate Git Commands

## `git diff`
Show changes between commits, branches, or the working tree.

Examples:
```bash
git diff
git diff --staged
git diff main..development
```

- `git diff` shows unstaged changes.
- `git diff --staged` shows staged changes.
- Compare branches with `git diff branchA..branchB`.

## `git merge`
Merge another branch into the current branch.

Example:
```bash
git checkout development
git merge feature/login-form
```

- Creates a merge commit if there are new commits on both branches.
- Use it to bring changes from one branch into another.

## `git rebase`
Reapply commits on top of another base branch.

Example:
```bash
git checkout development
git rebase main
```

- Rewrites branch history.
- Keeps history linear by placing your commits after the latest base branch commits.

## `git reset --soft`
Move branch to another commit without changing working tree.

Example:
```bash
git reset --soft HEAD~1
```

- Keeps your changes staged.
- Useful when you want to undo a commit but keep the edits.

## `git reset --hard`
Reset branch and working tree to a specific commit.

Example:
```bash
git reset --hard origin/main
```

- WARNING: discards unstaged and staged changes.
- Use when you want to revert completely to a known commit.

## `git pull --rebase`
Update current branch by rebasing onto the remote branch.

Example:
```bash
git pull --rebase origin main
```

- Fetches remote changes and reapplies your commits on top.
- Avoids extra merge commits.

## `git stash`
Save uncommitted changes temporarily.

Example:
```bash
git stash
git stash pop
```

- Use when you need to switch branches but keep your work.
- `git stash pop` re-applies the saved changes.
