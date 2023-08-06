# Getting started for developers

## Interactions with other developers

[**Gitter chat**](https://gitter.im/mindfulness-at-the-computer/community) - real-time text based chat about anything related to the project.

### Open conversation policy

Unless conversations are clearly of a private nature, we can choose to share them with other team members. The reasons for this policy is so that it does not take too long to relay information to others, and also it may be that other people have valuable ideas or input in the conversation.

### Reassigning issues

If there hasn't been an update for the progress on an issue in about 1-2 weeks we may reassign the issue to someone else. One reason for this is that we want new volunteers to be able to take on these issues.

### Conversations about issues in the Gitter chat

Please use [the Gitter chat](https://gitter.im/mindfulness-at-the-computer/community) rather than issue comments for conversations about issues. The goal is that the issue has almost no comments and that a person new to an issue is easily able to grasp what the issue is about. If new information is gained it may be better to update the first issue comment.

If you use comments to discuss issues please be aware that comments are removed now and then, and the description (first comment) is updated with information relevant to the issue.

## How to report bugs

Please report bugs or issues [in our issue list](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/-/issues)

## Decision process

Overall design and architecture is determined by SunyataZero (Tord). In other words the project uses a so-called "benevolent dictatorship" structure. (Of course since this is free and open source software, anyone can - and are encouraged - to create a fork and create their own Mindfulness application which meets their needs❣).

## Contributor responsibility, money and license

No responsibility for any financial or other damages.

People contributing to the project are unpaid, it's entirely a volunteer effort. No money is made from this application at the time of writing (and there are no plans for this to change).

This application is Free Libre Open Source Software. The software license is GPLv3.

## How do I get an overview of the project?

* Read about the [tech architecture](docs/tech-architecture.md) for the application.
* If things are unclear, please ask in the [Gitter chat](https://gitter.im/mindfulness-at-the-computer/community).

<!-- * Read the [advertisement for new people at code4socialgood](https://app.code4socialgood.org/project/view/932). -->

## What can I do right now?

* Code reviews.
* Write automated tests to increase code coverage.
* Check [the issue list](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/issues) to see if there are any issues marked with [help wanted](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/issues?label_name%5B%5D=help+wanted)
  * If you need to add new dependencies please bring this up in the chat before implementing (we are careful about adding more dependencies).

<!--
* This project is newbie-friendly and has [these issues](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/issues?label_name%5B%5D=first-timers-only) specifically for new people.
-->

## Merge Requests

1. Fork the repo (if you haven't already done so).
2. Clone it to your computer. You can do it using `git clone {url_name}`. (You can clone using https or ssh)
3. When you're ready to work on an issue, be sure you're on the **master** [branch](https://docs.gitlab.com/ee/gitlab-basics/create-branch.html)(Check using `git branch`). From there, create a separate branch. You can do this using `git checkout -b branch_name` where branch_name (e.g. issue_32) is the name of a new branch that you create.
4. Make your changes. Save the file. Go to the command line and do `git add file_name` to add it to the staging area.
5. Test the changes you've made manually to check that they are working okay
6. Run auto-tests to see if the changes you've made have impacted other parts of the application: `python -m unittest discover -s test` (on Ubuntu use `python3` instead of `python`).
5. Commit your changes. Do this using `git commit -m "comment about the changes made"`.
6. Push the working branch (e.g. issue_32) to your remote fork. This is done using `git push origin branch_name`.
7. Make the [merge request](https://docs.gitlab.com/ee/gitlab-basics/add-merge-request.html) (on the [upstream **master** branch](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/tree/master)).
    * Do not merge it with the master branch on your fork. That would result in multiple, or unrelated patches being included in a single PR.
8. If any further changes need to be made, comments will be made on the pull request.

If you're unsure of some details while you're making edits, you can discuss them in the [Gitter chat room](https://gitter.im/mindfulness-at-the-computer/community).

It's possible to work on two or more different patches (and therefore multiple branches) at one time, but it's recommended that beginners only work on one patch at a time.

### Syncing

Periodically, you'll need the sync your repo with the "upstream" repo (the original repo).

This file shows the relationship between the different copies: https://gitlab.com/mindfulness-at-the-computer/git-info/-/blob/master/repositories-in-our-workflow.png

<!--
GitLab has instructions for doing this:

1. [Configuring a remote for a fork](https://gitlab.com/help/gitlab-basics/fork-project.md)
    * Use https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer for the URL.
2. [Syncing a Fork](https://docs.gitlab.com/ee/gitlab-basics/start-using-git.html#go-to-the-master-branch-to-pull-the-latest-changes-from-there)
    * Use `git@gitlab.com:mindfulness-at-the-computer/mindfulness-at-the-computer.git` for the branch name.
-->

### Workflow overview

![workflow](docs/git-workflow.png)

<!--
## Translations

We need help localizing the application. Helping with translations is easy:
* You can add your name to our list of translators on [this wiki page](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer/wikis/Translators).
* You can [**join us on Crowdin**](https://crwd.in/mindfulness-at-the-computer) which is the system we use for adding translations and enter your translations there.
-->

## Website

The website has [a separate GitLab repo](https://gitlab.com/mindfulness-at-the-computer/mindfulness-at-the-computer.gitlab.io). The website itself is available [here](https://sunyatazero.gitlab.io/)

***

### References
* Book "Producing open-source software".
  * http://producingoss.com/en/getting-started.html#developer-guidelines.
  * http://producingoss.com/en/social-infrastructure.html.
* [Advertisement for new people](docs/varia/advertisement-for-devs.md).
