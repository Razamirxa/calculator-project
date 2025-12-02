# Git & GitHub Learning Path - Task by Task

Complete these tasks in order. Check them off as you go! ✅

---

## 📋 WEEK 1: Git Basics (Local Work)

### Day 1: Setup & First Commit
- [ ] **Task 1.1**: Install Git
  - Download from: https://git-scm.com/download/win
  - Verify installation: Open PowerShell and run:
  ```powershell
  git --version
  # Shows installed Git version - confirms Git is working properly
  ```

- [ ] **Task 1.2**: Configure Git
  ```powershell
  git config --global user.name "Your Name"
  # Sets your name - appears in all your commits to identify who made changes
  
  git config --global user.email "youremail@example.com"
  # Sets your email - links commits to your identity for team tracking
  
  git config --global core.editor "code --wait"
  # Sets VS Code as default editor for commit messages and merge conflicts
  ```

- [ ] **Task 1.3**: Initialize Your First Repository
  ```powershell
  cd "x:\learnings\git and github"
  # Navigate to your project folder
  
  git init
  # Creates a new Git repository - starts tracking changes in this folder
  
  git status
  # Shows current state - which files are tracked, modified, or untracked
  ```

- [ ] **Task 1.4**: Make Your First Commit
  ```powershell
  git add README.md
  # Stages README.md - prepares this file to be included in next commit
  
  git commit -m "Add README file"
  # Creates commit snapshot - saves staged changes with descriptive message
  
  git log
  # Shows commit history - lists all commits with author, date, and message
  ```

- [ ] **Task 1.5**: Commit All Project Files
  ```powershell
  git add .
  # Stages all files - dot (.) means add everything in current folder
  
  git commit -m "Add calculator project files"
  # Commits all staged files - saves complete project snapshot
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
  git status
  # Shows which files were modified - helps you see what you changed
  
  git diff
  # Shows exact line-by-line changes - red (-) for removed, green (+) for added
  ```

- [ ] **Task 2.3**: Commit the Change
  ```powershell
  git add calculator.py
  # Stages only calculator.py - selectively choose which files to commit
  
  git commit -m "Add modulo operation to calculator"
  # Commits with clear message - describes what feature was added
  ```

- [ ] **Task 2.4**: View History
  ```powershell
  git log
  # Shows detailed commit history - full information about each commit
  
  git log --oneline --graph --all
  # Shows compact visual history - one line per commit with branch diagram
  ```

- [ ] **Task 2.5**: Practice Undoing Changes
  - Make a small change to any file (add a comment)
  ```powershell
  git status
  # Check what changed - verify which file was modified
  
  git checkout -- calculator.py
  # Discards uncommitted changes - restores file to last committed version
  ```

**✅ Success Check**: You have 3 commits and understand `git status`, `git diff`, `git log`

---

### Day 3: Branching Basics

- [ ] **Task 3.1**: Create Your First Branch
  ```powershell
  git checkout -b feature-sqrt
  # Creates and switches to new branch - allows you to work on features without affecting main code
  
  git branch
  # Lists all branches - shows which branch you're currently on (marked with *)
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
  # Stages changes in your branch - changes stay separate from main
  
  git commit -m "Add square root function"
  # Commits to feature branch only - main branch remains unchanged
  ```

- [ ] **Task 3.4**: Switch Between Branches
  ```powershell
  git checkout main
  # Switches to main branch - your working files change to match main
  # Open calculator.py - notice square_root function is gone!
  
  git checkout feature-sqrt
  # Switches back to feature branch - files change to match this branch
  # Open calculator.py - square_root is back! Each branch has its own version
  ```

- [ ] **Task 3.5**: Merge Your Branch
  ```powershell
  git checkout main
  # Switch to main branch - you merge INTO the branch you're currently on
  
  git merge feature-sqrt
  # Merges feature-sqrt into main - brings square_root function into main branch
  
  git branch -d feature-sqrt
  # Deletes the branch - cleans up after successful merge (code is now in main)
  ```

**✅ Success Check**: Your main branch now has square_root function

---

### Day 4: More Branching Practice

- [ ] **Task 4.1**: Create Branch for Tests
  ```powershell
  git checkout -b add-sqrt-test
  # Creates test branch - keeps test additions separate until they're ready
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
  # Stages test file - prepares tests to be committed
  
  git commit -m "Add tests for square root"
  # Commits tests in branch - keeps test changes separate from main
  
  git checkout main
  # Switch to main branch - prepare to merge tests into main code
  
  git merge add-sqrt-test
  # Merges test branch - adds tests to main branch
  
  git branch -d add-sqrt-test
  # Deletes test branch - no longer needed after successful merge
  ```

- [ ] **Task 4.4**: Run the Tests
  ```powershell
  python test_calculator.py
  # Runs unit tests - verifies all calculator functions work correctly
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
  # Connects local repo to GitHub - "origin" is the standard name for remote repository
  
  git remote -v
  # Verifies connection - shows the URL of your remote repository
  ```

- [ ] **Task 5.4**: Push to GitHub
  ```powershell
  git branch -M main
  # Renames current branch to main - ensures branch name matches GitHub default
  
  git push -u origin main
  # Pushes code to GitHub - uploads all commits from local main to remote origin
  # -u sets upstream tracking so future pushes can just use "git push"
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
  # Creates feature branch - new features should always be in separate branches
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
  # Stages changes - prepares file for commit
  
  git commit -m "Add absolute value function"
  # Commits locally - saves changes on your computer only
  ```

- [ ] **Task 6.3**: Push Branch to GitHub
  ```powershell
  git push origin feature-absolute
  # Pushes branch to GitHub - uploads your feature branch to remote for team review
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
  # Switch to main branch - prepare to update with merged changes
  
  git pull origin main
  # Pulls from GitHub - downloads merged changes from remote to your local main
  
  git branch -d feature-absolute
  # Deletes local branch - no longer needed since merged on GitHub
  ```

**✅ Success Check**: Feature merged via PR, local and remote are in sync

---

### Day 7: Cloning & Collaborating

- [ ] **Task 7.1**: Clone a New Copy
  ```powershell
  cd x:\learnings
  # Change to parent directory
  
  git clone https://github.com/YOUR-USERNAME/calculator-project.git calculator-clone
  # Clones repository - downloads complete copy of project from GitHub to new folder
  # This simulates a teammate downloading your project
  
  cd calculator-clone
  # Enter cloned folder
  
  git log --oneline
  # View history - see all commits that were cloned
  ```

- [ ] **Task 7.2**: Make Changes in Clone
  - Edit README.md, add your name under Team Members
  ```powershell
  git add README.md
  # Stages README change
  
  git commit -m "Add my name to team members"
  # Commits in cloned repo - simulating teammate making changes
  
  git push origin main
  # Pushes to GitHub - uploads changes so others can get them
  ```

- [ ] **Task 7.3**: Pull Changes in Original
  ```powershell
  cd "x:\learnings\git and github"
  # Return to original project folder
  
  git pull origin main
  # Pulls changes - downloads updates made by "teammate" (your clone)
  # This is how teams stay synchronized
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
  # Creates branch named after issue - helps track which branch fixes which issue
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
  # Stages factorial changes
  
  git commit -m "Add factorial function - Fixes #1"
  # Commits with issue reference - "Fixes #1" links commit to Issue #1
  
  git push origin issue-1-factorial
  # Pushes branch to GitHub - makes it available for pull request
  ```

- [ ] **Task 8.5**: Create PR and Link Issue
  - Create PR on GitHub
  - In description write: "Closes #1"
    - "Closes #1" automatically closes Issue #1 when PR is merged
    - This links your code to the issue it solves
  - Merge the PR
  - Check that Issue #1 automatically closed!

**✅ Success Check**: Issue closed automatically when PR merged

---

### Day 9: Handling Conflicts

- [ ] **Task 9.1**: Create Two Branches
  ```powershell
  git checkout main
  # Switch to main branch - starting point for new branches
  
  git pull origin main
  # Get latest changes - ensures you're working with most recent code
  
  git checkout -b version-1
  # Create first branch - will make conflicting change here
  
  git checkout main
  # Return to main - need to create second branch from same starting point
  
  git checkout -b version-2
  # Create second branch - will make conflicting change here too
  ```

- [ ] **Task 9.2**: Make Conflicting Changes
  - In `version-1` branch:
    - Edit README.md, change description to "Advanced Calculator v1"
    ```powershell
    git add README.md; git commit -m "Update to v1"
    # Commits first version - changes same line that version-2 will change
    ```
  
  - Switch and edit same line:
    ```powershell
    git checkout version-2
    # Switch to second branch - going to edit same line differently
    ```
    - Edit README.md, change same description to "Advanced Calculator v2"
    ```powershell
    git add README.md; git commit -m "Update to v2"
    # Commits second version - creates conflict because same line changed differently
    ```

- [ ] **Task 9.3**: Merge First Branch
  ```powershell
  git checkout main
  # Switch to main - merging INTO main
  
  git merge version-1
  # Merges version-1 successfully - no conflicts yet because it's first merge
  ```

- [ ] **Task 9.4**: Merge Second Branch (CONFLICT!)
  ```powershell
  git merge version-2
  # Attempts merge - fails because same line was changed in both branches
  # Git doesn't know which version to keep, so it creates a conflict
  
  git status
  # Shows conflict status - lists files with conflicts that need manual resolution
  ```

- [ ] **Task 9.5**: Resolve the Conflict
  - Open README.md
  - Find lines with `<<<<<<<`, `=======`, `>>>>>>>`
  - Delete those markers and keep what you want
  - Save file

- [ ] **Task 9.6**: Complete the Merge
  ```powershell
  git add README.md
  # Stages resolved file - tells Git you fixed the conflict
  
  git commit -m "Resolve merge conflict"
  # Completes merge - creates merge commit with resolved conflicts
  
  git push origin main
  # Pushes to GitHub - uploads the resolved merge
  ```

**✅ Success Check**: You resolved your first merge conflict!

---

### Day 10: Advanced Git Commands

- [ ] **Task 10.1**: Use Git Stash
  ```powershell
  # Make some changes but don't commit
  
  git stash
  # Temporarily hides changes - useful when you need to switch branches but aren't ready to commit
  
  git stash list
  # Lists stashed changes - shows all changes you've temporarily hidden
  
  git stash pop
  # Restores stashed changes - brings back your work and removes from stash list
  ```

- [ ] **Task 10.2**: View Detailed History
  ```powershell
  git log --graph --oneline --all --decorate
  # Shows visual commit tree - displays branch structure and merge history
  
  git log --author="Your Name"
  # Filters by author - shows only commits made by specific person
  
  git log --since="1 week ago"
  # Filters by date - shows recent commits from past week
  ```

- [ ] **Task 10.3**: Use Git Blame
  ```powershell
  git blame calculator.py
  # Shows who changed each line - useful for finding who wrote specific code
  # Displays author, commit, and date for every line
  ```

- [ ] **Task 10.4**: Create and Use Tags
  ```powershell
  git tag v1.0
  # Creates tag - marks important points like releases (v1.0, v2.0, etc.)
  
  git tag
  # Lists all tags - shows version markers
  
  git push origin v1.0
  # Pushes tag to GitHub - makes release version available to others
  ```

- [ ] **Task 10.5**: View Differences
  ```powershell
  git diff HEAD~1
  # Compares with previous commit - HEAD~1 means "one commit before current"
  
  git diff main feature-name
  # Compares branches - shows differences between main and feature branch
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
