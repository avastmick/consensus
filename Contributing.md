# Contributing

The best way to contribute is to use [Gitbook](https://www.gitbook.com/book/avastmick/consensus). Go to [avastmick.io](avastmick.io/contact/) and drop me a note. I'll add you as collaborator.

## TL;DR;

- Using `Gitbook.com`:
  - Sign-up, using whichever method you prefer
  - Download the `Gitbook` editor
  - Send me a request to add you as a collaborator
  - Make changes then push up you changes and I will review.
- `Technical` - see below!

## Step-by-step for `Gitbook.com`

First, you need to know that the book is held in three versions: `master`, `draft` and `edit`.

- This README is on the `master` branch and is for information only.
- All changes should be made on the `edit` branch - can be experimental
- The `draft` branch, is the publishable version of the book - so must of high quality.

- Go to [gitbook.com](https://gitbook.com)
- Sign-up, using whichever method you prefer
- Send me your username or sign-up email on [avastmick.io](http://avastmick.io/contact/) and I will add you as a `collaborator`.

Once I've added you as a collaborator, sign-in to `Gitbook.com`, you should now see `Consensus` as a book.

- Click "Edit"...
- Now select the working version - `edit`

![Gitbook change version 1](images/gitbook-change-version-1.png)
![Gitbook change version 2](images/gitbook-change-version-2.png)

- Enter Enter "https://github.com/avastmick/consensus" in box (again)
- Wait... until the version is `edit`

![Gitbook change version 3](images/gitbook-change-version-3.png)

You will now be able to see all of the current chapters and can edit any that you like.

_Note:_ Please only make edits on the `edit` version.

If you have downloaded the `Gitbook.com` desktop editor, the above should also be the same.

### Technical Folks

If you are more technical, please use a typical git workflow. Only do this if you _are_ technical and know what `git` is _and_ know how to use it, otherwise go with the easier option above ;)

```bash
# Fork the https://github.com/avastmick/consensus repo
git clone https://github.com/[your_username]/consensus.git
cd consensus
git checkout edit
# make changes
git commit -am 'Made some changes'
git push
# Create pull request [your_username]/consensus/edit -> avastmick/consensus/edit
# Rinse and repeat
```