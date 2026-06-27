# Advanced Git Commands

## `git rebase -i`
Interactive rebase lets you rewrite commit history.

Example:
```bash
git rebase -i HEAD~4
```

- Use `pick`, `squash`, `fixup`, or `reword` to change commit history.
- Useful for cleaning up a branch before merging.

## `git cherry-pick`
Apply a single commit from another branch.

Example:
```bash
git cherry-pick abc1234
```

- Copies one commit onto the current branch.
- Useful for backporting specific fixes.

## `git reflog`
View the history of HEAD and branch movements.

Example:
```bash
git reflog
```

- Shows changes to HEAD even after rebases or resets.
- Useful for recovering lost commits.

## `git reset --mixed`
Reset the branch and keep working tree changes unstaged.

Example:
```bash
git reset --mixed HEAD~1
```

- Keeps your files but un-stages them.
- Good for undoing a commit while preserving changes.

## `git push --force-with-lease`
Force push safely by checking remote state first.

Example:
```bash
git push --force-with-lease origin development
```

- Safer than `--force`.
- Fails if the remote branch has new commits you don’t have locally.

## `git bisect`
Find the commit that introduced a bug using binary search.

Example:
```bash
git bisect start
git bisect bad
git bisect good v1.0
```

- Git checks out commits between the good and bad points.
- Helps find the exact commit that introduced a regression.

## `git filter-repo` / `git filter-branch`
Rewrite history across many commits.

Example:
```bash
git filter-repo --path filename --invert-paths
```

- Use for removing files or sensitive data from history.
- `git filter-repo` is preferred over `git filter-branch`.

## `git worktree`
Check out multiple branches at once.

Example:
```bash
git worktree add ../branch-worktree development
```

- Useful when you need separate working directories for different branches.
- Keeps each branch isolated in its own folder.
