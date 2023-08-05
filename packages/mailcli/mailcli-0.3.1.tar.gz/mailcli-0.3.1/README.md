# Mail CLI

Encapsulation for email senders, include mailgun service and SMTP mailer.

## Install

To install mail helper, run this command in your terminal:

```bash
$ pip install -U git+https://github.com/debugtalk/mail-cli.git#egg=mail-cli
```

## Usage

```text
$ python mailcli.py -h
usage: mailcli.py [-h] [-V] [-u MAILGUN_SMTP_USERNAME]
                  [-p MAILGUN_SMTP_PASSWORD] [--mail-sender MAIL_SENDER]
                  [--mail-recepients [MAIL_RECEPIENTS [MAIL_RECEPIENTS ...]]]
                  [--mail-subject MAIL_SUBJECT] [--mail-content MAIL_CONTENT]
                  [--mail-content-path MAIL_CONTENT_PATH]

Mail-CLI, send mail with mailgun service.

optional arguments:
  -h, --help            show this help message and exit
  -V, --version         show version
  -u MAILGUN_SMTP_USERNAME, --mailgun-smtp-username MAILGUN_SMTP_USERNAME
                        Specify mailgun smtp username.
  -p MAILGUN_SMTP_PASSWORD, --mailgun-smtp-password MAILGUN_SMTP_PASSWORD
                        Specify mailgun smtp password.
  --mail-sender MAIL_SENDER
                        Specify email sender.
  --mail-recepients [MAIL_RECEPIENTS [MAIL_RECEPIENTS ...]]
                        Specify email recepients.
  --mail-subject MAIL_SUBJECT
                        Specify email subject.
  --mail-content MAIL_CONTENT
                        Specify email content.
  --mail-content-path MAIL_CONTENT_PATH
                        Load file content as mail content.
```

## Examples

### send mail with content

```bash
$ python mailcli.py \
    -u "user@mail.com" \
    -p "pwd123" \
    --mail-sender "sender@mail.com" \
    --mail-recepients test1@mail.com test2@mail.com \
    --mail-subject subject-test \
    --mail-content hello-world
```

### send mail with file content

```bash
$ python mailcli.py \
    -u "user@mail.com" \
    -p "pwd123" \
    --mail-sender "sender@mail.com" \
    --mail-recepients test1@mail.com test2@mail.com \
    --mail-subject subject-test \
    --mail-content-path 1534006836.html
```
