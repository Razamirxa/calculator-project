# Quick Start Guide - Do This First!

## 🎯 Your First 30 Minutes with Git

Follow these steps RIGHT NOW to get started:

### Step 1: Install Git (5 minutes)
1. Download Git: https://git-scm.com/download/win
2. Run installer (use default settings)
3. Open PowerShell and verify:
   ```powershell
   git --version
   ```
   You should see something like: `git version 2.43.0`

### Step 2: Configure Git (2 minutes)
```powershell
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Step 3: Initialize Your Repository (3 minutes)
```powershell
cd "x:\learnings\git and github"
git init
git status
```

### Step 4: Make Your First Commit (5 minutes)
```powershell
git add .
git commit -m "Initial commit: Learning Git and GitHub"
git log
```

### Step 5: Test the Calculator (2 minutes)
```powershell
python calculator.py
```

### Step 6: Make a Change (10 minutes)
1. Open `calculator.py` in VS Code
2. Add a new method to the Calculator class:
   ```python
   def modulo(self, a, b):
       """Return remainder of a divided by b"""
       return a % b
   ```
3. Save the file
4. See what changed:
   ```powershell
   git status
   git diff
   ```
5. Commit your change:
   ```powershell
   git add calculator.py
   git commit -m "Add modulo operation"
   ```

### Step 7: Create Your First Branch (3 minutes)
```powershell
git checkout -b my-first-branch
git branch
git checkout main
```

---

## ✅ Success! You just learned:
- ✅ How to install and configure Git
- ✅ How to initialize a repository
- ✅ How to make commits
- ✅ How to check status and see changes
- ✅ How to create branches

---

## 🎓 What's Next?

Now open `LEARNING_PATH.md` and continue with **Day 2**!

The complete learning path covers:
- Week 1: Git basics (local work)
- Week 2: GitHub and remote repositories
- Week 3: Team collaboration
- Week 4: Professional workflows

**You're ready! Keep going! 🚀**
