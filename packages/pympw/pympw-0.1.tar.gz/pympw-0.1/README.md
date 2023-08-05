# pympw: Master Password --- An Algorithm for Freedom

Master Password is a determnistic password generator.
This is a Python implementation of the Master Password algorithm v3 based on 
[mpw-js](https://github.com/tmthrgd/mpw-js).

I faithfully implemented the [algorithm](http://www.masterpasswordapp.com/masterpassword-algorithm.pdf) for a cool password manager in a few dozen lines of Python. Please note **this code is for demonstration purposes only.** If you want to use a reliable deterministic password manager, get one at [masterpassword.app](http://masterpassword.app).

## **Features**

- ✔ Faithful and concise implementation of Master Password v3 using standard Python crypto libraries **scrypt, hmac, and digest.sha256**.
- ✔ *Quick password generation* for a single site.
- ✔ Generate long passwords, PINs, or even memorable phrases 
- ✔ Intuitive interactive session. *Type your master password once and request site passwords as you go!*
- ✔ Copy passwords to your clipboard --- *never print passwords out at all!*
- ✔ Interactive session can timeout after a few minutes to *protect your privacy*
- ✔ Support for counter and *all* MPv3 password template classes (maximum, long, medium, basic, short, PIN, name, and phrase)

## Installation

```
git clone --depth=1 https://github.com/roguh/pympw
cd pympw 
pip install .
```

### Dependencies

If you don't want pip to install dependencies, make sure to install the Python packages `scrypt` and `pyperclip`.

## CLI Usage

### Single site password with one command

Generate a password with a single command

```
$ python3 bin/pympw -n USER --type long -s google.com -c 20000
please type your master password >
site=google.com, type=long, counter=20000
Vode7.QojfDeqa
```

### Interactive mode

Enter interactive mode by omitting the `--site` argument. Type `CTRL-D` or `quit` to quit.

```
 $ pympw -n USER
please type your master password >
please type site name > google.com
please type counter or ENTER for default=1 > 20000
please type type or ENTER for default=long >
Vode7.QojfDeqa
please type site name > quit
bye
```

### More concise interactive mode

Enter alternative interactive mode

```
 $ python3 pympw -n USER -b/
please type your master password >
please type site name[/type[/counter]] > google.com
Kasi2/FipsHonm
please type site name[/type[/counter]] > google.com/pin
7002
please type site name[/type[/counter]] > google.com/medium/3
Wap4/Voy
please type site name[/type[/counter]] > google.com/x
i%&yc(sRV7VJqOQK%G0~
please type site name[/type[/counter]] > quit
bye
```

### Complete examples 

Use `--copy` to copy password to clipboard.

```
$ pympw -n USER --copy --type x
please type your master password >
please type site name > github.com
please type counter or ENTER for default=1 >
please type type or ENTER for default=x >
password copied to clipboard
E(%MMCBruYhaPEV6bM7^
```

Use `--exit-after` to shutdown interactive mode after some number of seconds.
Use `--quiet` to print less output.
Use `--keepalive` to reschedule timeout if you're still using the program.

```
$ pympw --name USER --type maximum --quiet --copy --splitby / \
    --keepalive --exit-after "$((60 * 5))" \
    --exit-command 'notify-send "MasterPassword is now closed"'
master password >
site name[/type[/counter]] > google.com/l/20000
Vode7.QojfDeqa
site name[/type[/counter]] > google.com
i%&yc(sRV7VJqOQK%G0~
site name[/type[/counter]] > 300 second timeout reached
bye
```

### All options 

```
$ pympw -h
usage: pympw [-h] [--name NAME] [--site SITE] [--counter COUNTER] [--quiet]
                  [--copy] [--hide-pw] [--splitby SPLITBY] [--keepalive]
                  [--exit-after EXIT_AFTER] [--exit-command EXIT_COMMAND]
                  [--type {maximum,x,long,l,medium,m,basic,b,short,s,longbasic,lb,pin,#,name,n,phrase,ph}]

CLI to Master Password algorithm v3. Passwords are generated locally, your
master password is not sent to any server. http://masterpassword.app

optional arguments:
 -h, --help            show this help message and exit
 --name NAME, -n NAME  your full name
 --site SITE, -s SITE  site name (e.g. linux.org). omit this argument to
                       start an interactive session.
 --counter COUNTER, -c COUNTER
                       positive integer less than 2**31=4294967296
 --type {maximum,x,long,l,medium,m,basic,b,short,s,longbasic,lb,pin,#,name,n,phrase,ph}
                       password type
 --copy, -y            copy password to clipboard instead of printing it
 --hide-pw, -d         never print passwords
 --splitby SPLITBY, -b SPLITBY
                       more efficient interactive session. suggested values:
                       tab, space, or '/'
 --exit-after EXIT_AFTER, -e EXIT_AFTER
                       script will timeout and close after this many seconds
 --exit-command EXIT_COMMAND
                       run this command if the script times out
 --keepalive, -k       keep program from timing out by pressing ENTER
 --quiet, -q           less output
```


## Library Usage

```
> from pympw import site_password, master_key, template_class_names 
```

See all template classes available 

```
> template_class_names 
['maximum',
 'x',
 'long',
 'l',
 'medium',
 'm',
 'basic',
 'b',
 'short',
 's',
 'longbasic',
 'lb',
 'pin',
 '#',
 'name',
 'n',
 'phrase',
 'ph']
```

Generate a master key (>1sec)

```
> master_key = master_key(b'USER', b'PASSWORD')
b'\xc8\xf2\xc7\xd3<(\x05\xaf\xf8ng\xfb\xb2\x06\xab6\x83\xfc\x85m\xcb\xa3$c\xb7\xc6I\x93\x01\xc7\xeb+\x810\xb2\xf2\x84\xa3f\xb7\xf0R\x9c_\xf1\xb3b\xa2\x99\xcb\xd3\x97`\xab_\xef\x89\xe6S\xe7\x84LM\xee'
```

Generate a password

```
> site_password(master_key=master_key, site_name='google.com', template_class='long', counter=20000)
'Vode7.QojfDeqa'
```

## Running tests

```
$ python3 setup.py test
============================== test session starts ===============================
platform linux -- Python 3.7.0, pytest-3.6.4, py-1.5.4, pluggy-0.7.1
collected 3 items                                                                

pympw/tests/test_master_password_v3.py ...                       [100%]

============================ 3 passed in 0.62 seconds ============================
```

## Authors

Master Password is a security product and algorithm by [Maarten Billemont](http://lhunath.com/), [Lyndir](http://www.lyndir.com/).

This Python implementation was created by Hugo Rivera.
