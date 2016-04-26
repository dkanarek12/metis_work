# Branches and Pull Requests


### Objectives:

 * Use branches to organize work on a repository.
 * Use pull requests to submit challenges.
 * Get feedback and discuss work on GitHub.
 * Improve work and re-submit as needed.


### Ideas:

 * Git history is like a tree of commits, and you can work on different named "growth points" called branches.
 * On GitHub, you can submit changes by asking that they be pulled in by someone else - this is called a pull request.


### Process:

 * Which branch are you on ?
```
git branch
```

 * Create a branch and switch to it:

```
git checkout -b experiment
```

 * Check your branch situation:

```
git branch
```

 * Change branches:

```
git checkout master
git checkout experiment
```

 * Work on your branch as usual, and then push to your `origin`.

```
git push origin experiment
```

 * Make a pull request on GitHub.

 * When you sync up, sync up `master`!

```
git checkout master
git pull upstream master
```

It's possible to do pull requests from your `master` branch, but this puts you in an awkward position where you're waiting for the pull request to get merged before it's safe for you to sync up again. Topic branches are highly recommended.


 * (BTW) Note that you have a `~/.gitconfig` file, which you can customize. I never type this, for example:

```
git log --graph --decorate --pretty=oneline --abbrev-commit --all
```
