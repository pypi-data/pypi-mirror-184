# ioe-email-stuff

A package that allows to send emails via a number of different methods from within a python application.

## Installation

Run the following to install:

```python
pip install ioe-email-stuff
```

## Usage

```python
from ioe_email_stuff import send_email

# Send an email - outlook only (for now).
# CC, BCC, attachment and server args not required.
# recipients, cc's and bcc's should be seperated by a semicolon, all in one string.
send_email("SUBJECT", "BODY", "USERNAME", "PASSWORD", "RECIPIENTS", cc="CCs", bcc="BCCs", files=["./ATTACHMENT1.png"], server="smtp.outlook.com")

# recommended way to handle errors is a try/except block:
try:
    semd_email("SUBJECT", "BODY", "USERNAME", "PASSWORD", "RECIPIENTS")
except Exception as e:
    # do something with e
    print(e)
```