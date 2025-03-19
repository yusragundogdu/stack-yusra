# point-package Project

This project aims to demonstrate the basic usage of Git and GitHub for version control and collaboration, while also showcasing how to handle data files and organize a simple project structure.

## Setup

1.  Install Git: [Git Installation Guide](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
2.  Create a GitHub account: [GitHub Sign Up](https://github.com/signup)
3.  Clone the repository: `git clone https://github.com/yusragundogdu/point-package.git`

## Usage

To use this project and understand the Git/GitHub workflow, follow these steps:

1.  **Navigate to the project directory:** Open your cmd and use the `cd` command to navigate to the "point-package" directory on your pc.

2.  **Add files to the staging area:** Use the `git add .` command to add all files (coordinates.csv and point.py) to the staging area.

3.  **Commit changes:** Use the `git commit -m "Eklendi"` command to commit the staged changes with a descriptive message. For example: `git commit -m "Added coordinates.csv and point.py files"`.

4.  **Connect to the remote repository:** Use the `git remote add origin https://github.com/yusragundogdu/point-package.git` command to connect your local repository to the remote repository on GitHub.

5.  **Push changes to GitHub:** Use the `git push -u origin master` command to push your local commits to the "master" branch of the remote repository.

## File Organization

* **coordinates.csv:** Contains geographical coordinates data.
* **point.py:** A Python script (currently empty).
* **tests:** An initially empty folder for potential future tests.

## Difficulties Encountered

* **Incorrect Remote URL:** Initially, there were issues with the remote repository URL, resulting in errors like "fatal: 'origin' does not appear to be a git repository". This was resolved by using the correct URL: `https://github.com/yusragundogdu/point-package.git`.
* **Adding and Committing Files:** There was a misunderstanding of the order of commands. The `git add` command must be used before `git commit` to stage the files for commit.
* **Pushing Changes:** After correctly setting the remote URL, the `git push -u origin master` command successfully pushed the local commits to GitHub.

## Git Commands Used

* `git init`: Initializes a new Git repository.
* `git add .`: Adds all files to the staging area.
* `git commit -m "Your commit message"`: Commits the staged changes with a message.
* `git remote add origin https://github.com/yusragundogdu/point-package.git`: Adds a remote repository named "origin".
* `git push -u origin master`: Pushes the local commits to the remote repository.
* `git remote set-url origin https://github.com/yusragundogdu/point-package.git`: Sets the URL for the remote repository.
* `git remote -v`: Lists the remote repositories and their URLs.

## Local Git Workflow vs. GitHub Workflow

* **Local Git Workflow:** Involves working with Git on your local machine, creating commits, and managing branches locally.
* **GitHub Workflow:** Extends the local workflow by using GitHub as a remote repository, enabling collaboration, pull requests, and issue tracking.

## Commit Decisions

* Commits were made after each significant change to the project, such as adding files, modifying code, or fixing bugs. This ensures that changes are tracked and can be reverted if necessary.

## AI Usage (If Applicable)

* During this project, I utilized a large language model to assist with understanding Git and GitHub commands, troubleshooting errors, and structuring the README file. This interaction helped me.

  
