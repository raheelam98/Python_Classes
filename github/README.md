# Git  Commands


## Push a Project to GitHub

Follow these steps to upload your local project to GitHub for the first time.

### Install Git (if not already installed)

```bash
git --version
```

### Open Terminal (Mac/Linux) or Git Bash (Windows)
Navigate to your project folder on your laptop:
```bash
cd path/to/your/project
```

### Status

```bash
git status
```

### Safe Fix (recommended)
First, fetch updates from GitHub:
```bash
git fetch origin
```

### Initialize Git
This makes folder a Git repository.
```bash
git init
```
This creates a hidden .git folder to track changes.

### Add Remote GitHub Repo
Connect your local project with your GitHub repository:
```bash
git remote add origin https://github.com/username/my-project.git
```
Replace username/my-project.git with your actual GitHub repo URL.

### Stage Files
Add all files to Git tracking:

```bash
git add .
```

### Commit Changes
Save your changes with a message:

```bash
git commit -m "Initial commit"
```

### Push to GitHub
Rename the default branch to main (if needed) and push to GitHub:

```bash
git branch -M main
git push -u origin main
```

Note:
- git branch -M main → rename your branch to main.
- git push -u origin main → push it to GitHub and remember the connection for next time.
- ***-u ** sets the upstream branch so future pushes can just be git push.

## Fix repository if it is not push

### Option 1: If you don’t care about the existing files on GitHub (overwrite everything)

This will replace the repo on GitHub with your local project.
```bash
git push -u origin main --force
```

### Option 2: If you want to keep both (merge GitHub + your local project)

* First, pull the GitHub repo into your local project:

   ```bash
    git pull origin main --rebase
     ```
     This brings down the GitHub commits (like README.md) and applies your changes on top.

* Then push again:
      ```bash
       git push -u origin main
      ```

Recommended: 
- Use Option 2 if you want to keep everything in sync.
- Use Option 1 only if you’re sure you want to overwrite GitHub with your laptop files.


#### If you make more changes later:

```bash
git add .
git commit -m "Updated project"
git push
```

