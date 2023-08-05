# git-sim
Visually simulate Git operations in your own repo with a single terminal command.

This generates an image (default) or video visualization depicting the command's behavior.

Command syntax is based directly on Git's command-line syntax, so using git-sim is as familiar as possible.

Example: `git-sim merge <branch>`

![git-sim-merge_11-30-22_11-50-32](https://user-images.githubusercontent.com/49353917/204894714-89d77aa7-98c9-4172-b11c-58f38672f1a7.jpg)

## Use cases
- Visualize Git commands to understand their effects on your repo before actually running them
- Prevent unexpected working directory and repository states by simulating before running
- Share visualizations (jpg image or mp4 video) of your Git commands with your team, or the world
- Save visualizations as a part of your team documentation to document workflow and prevent recurring issues
- Create static Git diagrams (jpg) or dynamic animated videos (mp4) to speed up content creation
- Help visual learners understand how Git commands work

## Features
- Run a one-liner git-sim command in the terminal to generate a custom Git command visualization (.jpg) from your repo
- Supported commands: `log`, `status`, `add`, `restore`, `commit`, `stash`, `branch`, `tag`, `reset`, `revert`, `merge`, `rebase`, `cherry-pick`
- Generate an animated video (.mp4) instead of a static image using the `--animate` flag (note: significant performance slowdown, it is recommended to use `--low-quality` to speed up testing and remove when ready to generate presentation-quality video)
- Choose between dark mode (default) and light mode
- Animation only: Add custom branded intro/outro sequences if desired
- Animation only: Speed up or slow down animation speed as desired

## Quickstart
1) Install [manim and manim dependencies for your OS](https://www.manim.community/)

2) Install `git-sim`:

```console
$ pip3 install git-sim
```

3) Browse to the Git repository you want to simulate Git commands in:

```console
$ cd path/to/git/repo
```

4) Run the program:

```console
$ git-sim [global options] <subcommand> [subcommand options]
```

5) Simulated output will be created as a `.jpg` file. Output files are named using the subcommand executed combined with a timestamp, and by default are stored in a subdirectory called `git-sim_media/`. The location of this subdirectory is customizable using the command line flag `--media-dir=path/to/output`. Note that when the `--animate` global flag is used, render times will be much longer and a `.mp4` video output file will be produced.

6) See global help for list of global options/flags and subcommands:

```console
$ git-sim -h
```

7) See subcommand help for list of options/flags for a specific subcommand:

```console
$ git-sim <subcommand> -h
```

## Requirements
* Python 3.7 or greater
* Pip (Package manager for Python)
* [Manim (Community version)](https://www.manim.community/)

## Commands
Basic usage is similar to Git itself - `git-sim` takes a familiar set of subcommands including "log", "status", "add", "restore", "commit", "stash", "branch", "tag", "reset", "revert", "merge", "rebase", "cherry-pick", along with corresponding options.

```console
$ git-sim [global options] <subcommand> [subcommand options]
```

The `[global options]` apply to the overarching `git-sim` simulation itself, including:

`--light-mode`: Use a light mode color scheme instead of default dark mode.  
`--animate`: Instead of outputting a static image, animate the Git command behavior in a .mp4 video.

Animation-only global options (to be used in conjunction with `--animate`:

`--speed=n`: Set the multiple of animation speed of the output simulation, `n` can be an integer or float, default is 1.  
`--low-quality`: Render the animation in low quality to speed up creation time, recommended for non-presentation use.  
`--show-intro`: Add an intro sequence with custom logo and title.  
`--show-outro`: Add an outro sequence with custom logo and text.  
`--title=title`: Custom title to display at the beginning of the animation.  
`--logo=logo.png`: The path to a custom logo to use in the animation intro/outro.  
`--outro-top-text`: Custom text to display above the logo during the outro.  
`--outro-bottom-text`: Custom text to display below the logo during the outro.

The `[subcommand options]` are like regular Git options specific to the specified subcommand (see below for a full list).

The following is a list of Git commands that can be simulated and their corresponding options/flags.

### git log
Usage: `git-sim log`

- Simulated output will show the most recent 5 commits on the active branch by default

![git-sim-log_11-30-22_11-40-56](https://user-images.githubusercontent.com/49353917/204893190-8be7e544-1abf-4514-98c9-391a6ef732d3.jpg)

### git status
Usage: `git-sim status`

- Simulated output will show the state of the working directory, staging area, and untracked files
- Note that simulated output will also show the most recent 5 commits on the active branch

![git-sim-status_11-11-22_22-57-49](https://user-images.githubusercontent.com/49353917/201461977-189d58fd-f796-4069-b94e-dfb5a395758a.jpg)

### git add
Usage: `git-sim add <file 1> <file 2> ... <file n>`

- Specify one or more `<file>` as a *modified* working directory file, or an untracked file
- Simulated output will show files being moved to the staging area
- Note that simulated output will also show the most recent 5 commits on the active branch

![git-sim-add_11-11-22_22-59-54](https://user-images.githubusercontent.com/49353917/201461985-2ebf7bfe-929a-4025-9049-8f2a933a237a.jpg)

### git restore
Usage: `git-sim restore <file 1> <file 2> ... <file n>`

- Specify one or more `<file>` as a *modified* working directory file, or staged file
- Simulated output will show files being moved back to the working directory or discarded changes
- Note that simulated output will also show the most recent 5 commits on the active branch

![git-sim-restore_11-21-22_20-43-45](https://user-images.githubusercontent.com/49353917/203223705-e1872376-df9f-4f11-b06e-746766b2a4ca.jpg)

### git commit
Usage: `git-sim commit -m "Commit message"`

- Simulated output will show the new commit added to the tip of the active branch
- Specify your commit message after the -m option
- HEAD and the active branch will be moved to the new commit
- Simulated output will show files in the staging area being included in the new commit

![git-sim-commit_11-21-22_20-45-11](https://user-images.githubusercontent.com/49353917/203223869-d7f37189-7a6a-4e5d-93f3-46c7f3509690.jpg)

### git stash
Usage: `git-sim stash <file>`

- Specify one or more `<file>` as a *modified* working directory file, or staged file
- If no `<file>` is specified, all available working directory and staged files will be included
- Simulated output will show files being moved to the Git stash
- Note that simulated output will also show the most recent 5 commits on the active branch

![git-sim-stash_11-21-22_20-46-21](https://user-images.githubusercontent.com/49353917/203224031-21c4a8c0-38d4-430d-b0a2-da4b320d05ab.jpg)

### git branch
Usage: `git-sim branch <new branch name>`

- Specify `<new branch name>` as the name of the new branch to simulate creation of
- Simulated output will show the newly create branch ref along with most recent 5 commits on the active branch

![git-sim-branch_11-11-22_23-00-36](https://user-images.githubusercontent.com/49353917/201461993-5f5ae510-1b04-4cb3-9002-72e969c4d73a.jpg)

### git tag
Usage: `git-sim tag <new tag name>`

- Specify `<new tag name>` as the name of the new tag to simulate creation of
- Simulated output will show the newly create tag ref along with most recent 5 commits on the active branch

![git-sim-tag_11-11-22_23-00-57](https://user-images.githubusercontent.com/49353917/201461998-86f58c5a-8fb5-4882-bb87-7e42e67d5c37.jpg)

### git reset
Usage: `git-sim reset <reset-to> [--mixed|--soft|--hard]`

- Specify `<reset-to>` as any commit id, branch name, tag, or other ref to simulate reset to from the current HEAD (default: `HEAD`)
- As with a normal git reset command, default reset mode is `--mixed`, but can be specified using `--soft`, `--hard`, or `--mixed`
- Simulated output will show branch/HEAD resets and resulting state of the working directory, staging area, and whether any file changes would be deleted by running the actual command

![git-sim-reset_11-11-22_23-02-42](https://user-images.githubusercontent.com/49353917/201462003-bf59e272-16fa-4c3d-b9f3-0fc91d2caa48.jpg)

### git revert
Usage: `git-sim revert <to-revert>`

- Specify `<to-revert>` as any commit id, branch name, tag, or other ref to simulate revert for
- Simulated output will show the new commit which reverts the changes from `<to-revert>`
- Simulated output will include the next 4 most recent commits on the active branch

![git-sim-revert_11-30-22_11-46-09](https://user-images.githubusercontent.com/49353917/204893827-c0fef360-9c39-4686-81f2-f85f51a85597.jpg)

### git merge
Usage: `git-sim merge <branch>`

- Specify `<branch>` as the branch name to merge into the active branch
- Simulated output will depict a fast-forward merge if possible
- Otherwise, a three-way merge will be depicted
- To force a merge commit when a fast-forward is possible, use `--no-ff`

![git-sim-merge_11-30-22_11-50-32](https://user-images.githubusercontent.com/49353917/204894714-89d77aa7-98c9-4172-b11c-58f38672f1a7.jpg)

### git rebase
Usage: `git-sim rebase <new-base>`

- Specify `<new-base>` as the branch name to rebase the active branch onto

![git-sim-rebase_11-30-22_11-52-26](https://user-images.githubusercontent.com/49353917/204895157-8f020afe-df63-494d-bd16-d00801f438bc.jpg)

### git cherry-pick
Usage: `git-sim cherry-pick <commit>`

- Specify `<commit>` as a ref (branch name/tag) or commit ID to cherry-pick onto the active branch

![git-sim-cherry-pick_11-21-22_21-13-23](https://user-images.githubusercontent.com/49353917/203227369-fce5edc3-00b5-4d57-95b8-318442c3984e.jpg)

## Video animation examples
```console
$ git-sim --animate reset HEAD^
```

https://user-images.githubusercontent.com/49353917/201462192-a3bc3a2e-f2c9-4166-81ce-743e53255fc2.mp4

```console
$ git checkout feature9
$ git-sim --animate merge feature6
```

https://user-images.githubusercontent.com/49353917/204897010-3aa2a0e6-c8ba-4acd-acd1-2683274afb63.mp4

```console
$ git checkout feature1
$ git-sim --animate rebase main
```

https://user-images.githubusercontent.com/49353917/204896434-48dbc15b-9718-47c7-b790-6caad5f8a367.mp4

```console
$ git checkout feature6
$ git-sim --animate cherry-pick feature9
```

https://user-images.githubusercontent.com/49353917/204899112-2c99019e-1253-4aef-a0b7-dc774d0adbe8.mp4

## Basic command examples
Simulate the output of the git log command:

```console
$ cd path/to/git/repo
$ git-sim log
```

Simulate the output of the git status command:

```console
$ git-sim status
```

Simulate adding a file to the Git staging area:

```console
$ git-sim add filename.ext
```

Simulate restoring a file from the Git staging area:

```console
$ git-sim restore filename.ext
```

Simulate creating a new commit based on currently staged changes:

```console
$ git-sim commit -m "Commit message"
```

Simulate stashing all working directory and staged changes:

```console
$ git-sim stash
```

Simulate creating a new Git branch:

```console
$ git-sim branch new-branch-name 
```

Simulate creating a new Git tag:

```console
$ git-sim tag new-tag-name
```

Simulate a hard reset of the current branch HEAD to the previous commit:

```console
$ git-sim reset HEAD^ --hard
```

Simulate reverting the changes in an older commit:

```console
$ git-sim revert HEAD~7
```

Simulate merging a branch into the active branch:

```console
$ git-sim merge feature1
```

Simulate rebasing the active branch onto a new base:

```console
$ git-sim rebase main
```

Simulate cherry-picking a commit from another branch onto the active branch:

```console
$ git-sim cherry-pick 0ae641
```

## Command examples with extra options/flags
Use light mode for white background and black text, instead of the default black background with white text:

```console
$ git-sim --light-mode status
```

Animate the simulated output as a .mp4 video file:

```console
$ git-sim --animate add filename.ext
```

Add an intro and outro with custom text and logo (must include `--animate`):

```console
$ git-sim --animate --show-intro --show-outro --outro-top-text="My Git Repo" --outro-bottom-text="Thanks for watching!" --logo=path/to/logo.png status
```

Customize the output image/video directory location:

```console
$ git-sim --media-dir=path/to/output status
```

Generate output video in low quality to speed up rendering time (useful for repeated testing, must include `--animate`):

```console
$ git-sim --animate --low-quality status
```

## Installation
See **Quickstart** section for details on installing manim and other dependencies. Then run:

```console
$ pip3 install git-sim
```

## Learn More
Learn more about this tool on the [git-sim project page](https://initialcommit.com/tools/git-sim).

## Authors
**Jacob Stopak** - on behalf of [Initial Commit](https://initialcommit.com)
