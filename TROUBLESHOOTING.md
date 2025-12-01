# Common Git Problems & Solutions

## Problem 1: "git is not recognized"
**Error**: `'git' is not recognized as an internal or external command`

**Solution**:
1. Install Git from: https://git-scm.com/download/win
2. Restart PowerShell
3. Test: `git --version`

---

## Problem 2: Merge Conflicts
**Error**: `CONFLICT (content): Merge conflict in file.py`

**Solution**:
```powershell
# 1. Open the file with conflict
# 2. Look for these markers:
#    <<<<<<< HEAD
#    your changes
#    =======
#    their changes
#    >>>>>>> branch-name
# 3. Edit file to keep what you want
# 4. Remove the markers
# 5. Save and commit:
git add file.py
git commit -m "Resolve merge conflict"
```

---

## Problem 3: Committed to Wrong Branch
**Error**: Made changes on `main` instead of feature branch

**Solution**:
```powershell
# Before pushing:
git stash                        # Save changes
git checkout -b correct-branch   # Create right branch
git stash pop                    # Apply changes
git add .
git commit -m "Your message"
```

---

## Problem 4: Want to Undo Last Commit
**Error**: Need to undo the most recent commit

**Solution**:
```powershell
# Keep changes, undo commit:
git reset --soft HEAD~1

# Discard changes and commit:
git reset --hard HEAD~1
```

---

## Problem 5: Forgot to Pull Before Push
**Error**: `Updates were rejected because the remote contains work`

**Solution**:
```powershell
git pull origin main
# Resolve any conflicts
git push origin main
```

---

## Problem 6: Accidentally Deleted File
**Error**: Deleted file but didn't commit yet

**Solution**:
```powershell
git checkout -- deleted-file.py
```

---

## Problem 7: Want to See What Changed
**Error**: Don't remember what you modified

**Solution**:
```powershell
git status              # See which files changed
git diff                # See exact changes
git diff --cached       # See staged changes
```

---

## Problem 8: Push Rejected - Non-Fast-Forward
**Error**: `failed to push some refs`

**Solution**:
```powershell
# Someone else pushed changes first
git pull origin main
# Resolve conflicts if any
git push origin main
```

---

## Problem 9: Wrong Commit Message
**Error**: Typo in last commit message

**Solution**:
```powershell
# If not pushed yet:
git commit --amend -m "Correct message"

# If already pushed, just make new commit
```

---

## Problem 10: Need to Switch Branch But Have Changes
**Error**: `Your local changes would be overwritten`

**Solution**:
```powershell
# Save changes temporarily:
git stash

# Switch branch:
git checkout other-branch

# Come back and restore:
git checkout original-branch
git stash pop
```

---

## Quick Command Reference

```powershell
# Oh no, I messed up!
git status                     # See what's happening
git log --oneline             # See recent commits
git reflog                    # See everything you did

# Emergency undo
git checkout -- file.py       # Undo changes to file
git reset --hard HEAD         # Undo all uncommitted changes
git clean -fd                 # Remove untracked files

# Get help
git help                      # General help
git help commit               # Help for specific command
```

---

## Getting Unstuck

If you're completely lost:
```powershell
git status        # Always start here
git log --oneline # See where you are
git branch        # See which branch you're on
```

If nothing works:
```powershell
# Save your work first!
# Copy modified files to safe location
# Then delete and re-clone repository
```

---

**Remember**: Git saves everything! It's very hard to permanently lose work. Take a deep breath and check the solutions above. 💪
