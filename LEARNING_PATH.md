# Git & GitHub Learning Path - Task by Task

Complete these tasks in order. Check them off as you go! ✅

---

## 📋 WEEK 1: Git Basics (Local Work)

### Day 1: Setup & First Commit
- [ ] **Task 1.1**: Install Git
  - Download from: https://git-scm.com/download/win
  - Verify installation: Open PowerShell and run `git --version`

- [ ] **Task 1.2**: Configure Git
  ```powershell
  git config --global user.name "Your Name"
  git config --global user.email "youremail@example.com"
  git config --global core.editor "code --wait"  # Use VS Code as editor
  ```

- [ ] **Task 1.3**: Initialize Your First Repository
  ```powershell
  cd "x:\learnings\git and github"
  git init
  git status  # See what Git sees
  ```

- [ ] **Task 1.4**: Make Your First Commit
  ```powershell
  git add README.md
  git commit -m "Add README file"
  git log  # View your commit
  ```

- [ ] **Task 1.5**: Commit All Project Files
  ```powershell
  git add .
  git commit -m "Add calculator project files"
  ```

**✅ Success Check**: Run `git log --oneline` and see 2 commits

---

### Day 2: Making Changes & Tracking History

- [ ] **Task 2.1**: Modify the Calculator
  - Open `calculator.py`
  - Add this new method inside the Calculator class:
  ```python
  def modulo(self, a, b):
      """Return remainder of a divided by b"""
      if b == 0:
          raise ValueError("Cannot modulo by zero")
      return a % b
  ```

- [ ] **Task 2.2**: See What Changed
  ```powershell
  git status        # See which files changed
  git diff          # See exact changes
  ```

- [ ] **Task 2.3**: Commit the Change
  ```powershell
  git add calculator.py
  git commit -m "Add modulo operation to calculator"
  ```

- [ ] **Task 2.4**: View History
  ```powershell
  git log
  git log --oneline --graph --all
  ```

- [ ] **Task 2.5**: Practice Undoing Changes
  - Make a small change to any file (add a comment)
  - Check status: `git status`
  - Undo it: `git checkout -- calculator.py`

**✅ Success Check**: You have 3 commits and understand `git status`, `git diff`, `git log`

---

### Day 3: Branching Basics

- [ ] **Task 3.1**: Create Your First Branch
  ```powershell
  git checkout -b feature-sqrt
  git branch  # See all branches
  ```

- [ ] **Task 3.2**: Add Feature in Branch
  - Add this method to Calculator class:
  ```python
  def square_root(self, a):
      """Calculate square root"""
      if a < 0:
          raise ValueError("Cannot calculate square root of negative number")
      return a ** 0.5
  ```

- [ ] **Task 3.3**: Commit in Branch
  ```powershell
  git add calculator.py
  git commit -m "Add square root function"
  ```

- [ ] **Task 3.4**: Switch Between Branches
  ```powershell
  git checkout main           # Switch to main
  # Open calculator.py - notice square_root is gone!
  git checkout feature-sqrt   # Switch back
  # Open calculator.py - square_root is back!
  ```

- [ ] **Task 3.5**: Merge Your Branch
  ```powershell
  git checkout main
  git merge feature-sqrt
  git branch -d feature-sqrt  # Delete the branch
  ```

**✅ Success Check**: Your main branch now has square_root function

---

### Day 4: More Branching Practice

- [ ] **Task 4.1**: Create Branch for Tests
  ```powershell
  git checkout -b add-sqrt-test
  ```

- [ ] **Task 4.2**: Add Test
  - Open `test_calculator.py`
  - Add this test method in TestCalculator class:
  ```python
  def test_square_root(self):
      """Test square root operation"""
      self.assertEqual(self.calc.square_root(16), 4)
      self.assertEqual(self.calc.square_root(9), 3)
  
  def test_square_root_negative(self):
      """Test square root of negative raises error"""
      with self.assertRaises(ValueError):
          self.calc.square_root(-4)
  ```

- [ ] **Task 4.3**: Commit and Merge
  ```powershell
  git add test_calculator.py
  git commit -m "Add tests for square root"
  git checkout main
  git merge add-sqrt-test
  git branch -d add-sqrt-test
  ```

- [ ] **Task 4.4**: Run the Tests
  ```powershell
  python test_calculator.py
  ```

**✅ Success Check**: Tests pass, branch merged and deleted

---

## 📋 WEEK 2: GitHub & Remote Work

### Day 5: GitHub Setup

- [ ] **Task 5.1**: Create GitHub Account
  - Go to: https://github.com
  - Sign up for free account
  - Verify your email

- [ ] **Task 5.2**: Create New Repository on GitHub
  - Click "+" icon → "New repository"
  - Name: `calculator-project`
  - Description: "Learning Git and GitHub"
  - Choose: Public
  - DON'T initialize with README (we already have one)
  - Click "Create repository"

- [ ] **Task 5.3**: Connect Local to GitHub
  ```powershell
  git remote add origin https://github.com/YOUR-USERNAME/calculator-project.git
  git remote -v  # Verify it's connected
  ```

- [ ] **Task 5.4**: Push to GitHub
  ```powershell
  git branch -M main  # Rename master to main if needed
  git push -u origin main
  ```

- [ ] **Task 5.5**: View on GitHub
  - Refresh your GitHub repository page
  - See your code online!
  - Explore: commits, branches, files

**✅ Success Check**: Your code is visible on GitHub

---

### Day 6: GitHub Workflow

- [ ] **Task 6.1**: Make Changes Locally
  ```powershell
  git checkout -b feature-absolute
  ```
  - Add to Calculator class:
  ```python
  def absolute(self, a):
      """Return absolute value"""
      return abs(a)
  ```

- [ ] **Task 6.2**: Commit Locally
  ```powershell
  git add calculator.py
  git commit -m "Add absolute value function"
  ```

- [ ] **Task 6.3**: Push Branch to GitHub
  ```powershell
  git push origin feature-absolute
  ```

- [ ] **Task 6.4**: Create Pull Request
  - Go to your GitHub repository
  - Click "Compare & pull request" button
  - Title: "Add absolute value function"
  - Description: "This PR adds absolute value calculation"
  - Click "Create pull request"

- [ ] **Task 6.5**: Merge Pull Request
  - Review your changes on GitHub
  - Click "Merge pull request"
  - Click "Confirm merge"
  - Delete the branch on GitHub

- [ ] **Task 6.6**: Update Local Repository
  ```powershell
  git checkout main
  git pull origin main
  git branch -d feature-absolute
  ```

**✅ Success Check**: Feature merged via PR, local and remote are in sync

---

### Day 7: Cloning & Collaborating

- [ ] **Task 7.1**: Clone a New Copy
  ```powershell
  cd x:\learnings
  git clone https://github.com/YOUR-USERNAME/calculator-project.git calculator-clone
  cd calculator-clone
  git log --oneline
  ```

- [ ] **Task 7.2**: Make Changes in Clone
  - Edit README.md, add your name under Team Members
  ```powershell
  git add README.md
  git commit -m "Add my name to team members"
  git push origin main
  ```

- [ ] **Task 7.3**: Pull Changes in Original
  ```powershell
  cd "x:\learnings\git and github"
  git pull origin main
  ```

**✅ Success Check**: Changes sync between two local copies via GitHub

---

## 📋 WEEK 3: Team Collaboration

### Day 8: Simulating Team Work

- [ ] **Task 8.1**: Create Issue on GitHub
  - Go to your repo → "Issues" tab
  - Click "New issue"
  - Title: "Add factorial function"
  - Description: "We need a factorial calculator function"
  - Click "Submit new issue"

- [ ] **Task 8.2**: Create Branch from Issue
  ```powershell
  git checkout -b issue-1-factorial
  ```

- [ ] **Task 8.3**: Implement the Feature
  - Add to Calculator:
  ```python
  def factorial(self, n):
      """Calculate factorial of n"""
      if n < 0:
          raise ValueError("Factorial not defined for negative numbers")
      if n == 0 or n == 1:
          return 1
      result = 1
      for i in range(2, n + 1):
          result *= i
      return result
  ```

- [ ] **Task 8.4**: Commit and Push
  ```powershell
  git add calculator.py
  git commit -m "Add factorial function - Fixes #1"
  git push origin issue-1-factorial
  ```

- [ ] **Task 8.5**: Create PR and Link Issue
  - Create PR on GitHub
  - In description write: "Closes #1"
  - Merge the PR
  - Check that Issue #1 automatically closed!

**✅ Success Check**: Issue closed automatically when PR merged

---

### Day 9: Handling Conflicts

- [ ] **Task 9.1**: Create Two Branches
  ```powershell
  git checkout main
  git pull origin main
  git checkout -b version-1
  git checkout main
  git checkout -b version-2
  ```

- [ ] **Task 9.2**: Make Conflicting Changes
  - In `version-1` branch:
    - Edit README.md, change description to "Advanced Calculator v1"
    - Commit: `git add README.md; git commit -m "Update to v1"`
  
  - Switch and edit same line:
    ```powershell
    git checkout version-2
    ```
    - Edit README.md, change same description to "Advanced Calculator v2"
    - Commit: `git add README.md; git commit -m "Update to v2"`

- [ ] **Task 9.3**: Merge First Branch
  ```powershell
  git checkout main
  git merge version-1  # This works fine
  ```

- [ ] **Task 9.4**: Merge Second Branch (CONFLICT!)
  ```powershell
  git merge version-2  # CONFLICT!
  git status           # See the conflict
  ```

- [ ] **Task 9.5**: Resolve the Conflict
  - Open README.md
  - Find lines with `<<<<<<<`, `=======`, `>>>>>>>`
  - Delete those markers and keep what you want
  - Save file

- [ ] **Task 9.6**: Complete the Merge
  ```powershell
  git add README.md
  git commit -m "Resolve merge conflict"
  git push origin main
  ```

**✅ Success Check**: You resolved your first merge conflict!

---

### Day 10: Advanced Git Commands

- [ ] **Task 10.1**: Use Git Stash
  ```powershell
  # Make some changes but don't commit
  # Then:
  git stash                    # Hide changes
  git stash list               # See stashed changes
  git stash pop                # Bring changes back
  ```

- [ ] **Task 10.2**: View Detailed History
  ```powershell
  git log --graph --oneline --all --decorate
  git log --author="Your Name"
  git log --since="1 week ago"
  ```

- [ ] **Task 10.3**: Use Git Blame
  ```powershell
  git blame calculator.py      # See who changed each line
  ```

- [ ] **Task 10.4**: Create and Use Tags
  ```powershell
  git tag v1.0                 # Create tag
  git tag                      # List tags
  git push origin v1.0         # Push tag to GitHub
  ```

- [ ] **Task 10.5**: View Differences
  ```powershell
  git diff HEAD~1              # Compare with previous commit
  git diff main feature-name   # Compare branches
  ```

**✅ Success Check**: You know advanced Git commands

---

## 📋 WEEK 4: Professional Workflows

### Day 11-12: Fork & Contribute

- [ ] **Task 11.1**: Find Public Repository
  - Search GitHub for beginner-friendly projects
  - Look for repos with "good first issue" label

- [ ] **Task 11.2**: Fork a Repository
  - Click "Fork" button on GitHub
  - Clone YOUR fork locally

- [ ] **Task 11.3**: Make a Contribution
  - Create branch
  - Fix typo or add small feature
  - Commit and push to your fork

- [ ] **Task 11.4**: Create PR to Original
  - Submit Pull Request from your fork
  - Write good description
  - Wait for review

**✅ Success Check**: You made your first open source contribution!

---

### Day 13-14: Team Best Practices

- [ ] **Task 13.1**: Write Good Commit Messages
  - Format: `Type: Brief description`
  - Examples:
    - `feat: Add new calculator function`
    - `fix: Resolve division by zero bug`
    - `docs: Update README with examples`
    - `test: Add unit tests for modulo`

- [ ] **Task 13.2**: Create .github Folder
  ```powershell
  mkdir .github
  ```
  - Create Pull Request template
  - Create Issue template

- [ ] **Task 13.3**: Set Up Branch Protection
  - GitHub repo → Settings → Branches
  - Add rule for `main`
  - Require PR reviews before merge

- [ ] **Task 13.4**: Use GitHub Projects
  - Create project board
  - Add cards for tasks
  - Move cards through workflow

**✅ Success Check**: Your repo follows professional standards

---

## 🎓 FINAL PROJECT

### Complete Team Simulation

- [ ] **Final Task**: Enhance Calculator with Team Workflow
  1. Create 3 issues on GitHub for new features:
     - Issue #1: Add logarithm function
     - Issue #2: Add percentage calculation
     - Issue #3: Add documentation strings
  
  2. For EACH issue:
     - Create branch from main
     - Implement feature
     - Write test
     - Commit with good message
     - Push branch
     - Create Pull Request
     - Review your own code
     - Merge PR
     - Pull to local main
  
  3. Create a release (v2.0) on GitHub
  
  4. Update README with all new features

**✅ Final Success**: You completed a full professional Git/GitHub workflow!

---

## 📚 Quick Reference Commands

```powershell
# Daily workflow
git status                          # Check status
git add .                          # Stage all changes
git commit -m "message"            # Commit
git push origin branch-name        # Push to GitHub
git pull origin main               # Get latest changes

# Branching
git checkout -b new-branch         # Create and switch
git checkout main                  # Switch branch
git merge branch-name              # Merge branch
git branch -d branch-name          # Delete branch

# Viewing
git log --oneline                  # See commits
git diff                           # See changes
git remote -v                      # See remote URLs

# Undo
git checkout -- file.py            # Undo file changes
git reset --soft HEAD~1            # Undo last commit
git stash                          # Temporarily hide changes
```

---

## 🎯 Learning Resources

- Git Documentation: https://git-scm.com/doc
- GitHub Guides: https://guides.github.com
- Interactive Learning: https://learngitbranching.js.org
- GitHub Skills: https://skills.github.com

---

**🚀 START WITH DAY 1, TASK 1.1 NOW!**
