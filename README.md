# SIP Client Demo
> Just a SIP Client (VoIP) use pjsua python module

[![Build Status][travis-image]][travis-url]

![](header.png)

## Build & Installation

This guide is used for CentOS Linux 64bit 6.x.

**1. Requirements**

- Build tools: make, gcc, and binutils
- Python 2.7.x
- Develop tools (include python-dev)

Check version of CentOS. If gcc version 4.8+, can igorne upgrade gcc.

```
$ cat /etc/centos-release
```

**2. Upgrade gcc:**

Import CERN's GPG key:

```
$ sudo rpm --import http://ftp.scientificlinux.org/linux/scientific/5x/x86_64/RPM-GPG-KEYs/RPM-GPG-KEY-cern
```

Save repository information as `/etc/yum.repos.d/slc6-devtoolset.repo` on your system:

```
$ wget -O /etc/yum.repos.d/slc6-devtoolset.repo http://linuxsoft.cern.ch/cern/devtoolset/slc6-devtoolset.repo
```

Install develop tool:

```
$ sudo yum install devtoolset-2
```

Enable the environment: 

```
$ scl enable devtoolset-2 bash
```

**3. Building the Module**

Using Python build script:

1. Build the PJSIP libraries first with the usual `./configure && make dep && make` commands.
2. Go to pjsip-apps/src/python directory.
3. Run `sudo python ./setup.py install` or just `sudo make` 

Or simple use this script: [build.sh](build.sh)

**4. Testing the module installation**

```
$ python
> import pjsua
> ^Z

$
```

**5. Run application**

```
$ git clone https://github.com/hardw0rk/sipclientdemo.git
$ cd sipclientdemo
$ python sipclient.py
```

## Usage example

**1. Install text-to-speech tools**

```
$ yum install festival pulseaudio pulseaudio-utils -y 
```

Configure Festival:

```
$ vi ~/.festivalrc
----
(Parameter.set 'Audio_Method 'Audio_Command)
(Parameter.set 'Audio_Command "aplay -q -c 1 -t raw -f s16 -r $SR $FILE")
```

Configure Pulseaudio:

```
$ vi ~/.pulse/daemon.conf
---
resample-method = src-sinc-best-quality
default-sample-format=s24le
default-sample-rate=44100

Run pulseaudio daemon:
$ pulseaudio -D --system

Reset pulseaudio when change:
$ pulseaudio -k
```

Test:

```
echo 'hello, i am a 123host technical' | festival --tts
```

Text-to-speech to wav:

```
text2wave -o message.wav message.txt
```

**2. How to use**

- Register two SIP accounts:

```
SIP Address: 123host01@sip2sip.info
Username: 123host01
Domain/Realm: sip2sip.info

SIP Address: 123host02@sip2sip.info
Username: 123host02
Domain/Realm: sip2sip.info

Password: **********
```

- Login to Home page to view account details:

[http://sip2sip.info](http://sip2sip.info)

- Run SIP Client on 2 hosts to test:

Host 1:

```
python sipclient.py
---
sipclient.py -- Simple SIP Client use PJSUA Python Module (PJSIP API)

Your SIP URL [sip:123host01@sip2sip.info]: [enter-to-keep-default]
URL of the registrar [sip:sip2sip.info]: [enter-to-keep-default]
URL of the proxy [sip:proxy.sipthor.net;lr]: [enter-to-keep-default]
Auth Realm [sip2sip.info]: [enter-to-keep-default]
Auth Username [123host01@sip2sip.info]: [enter-to-keep-default]
Auth Password [**********]: [enter-to-keep-default]
---------------------------------------------------------------------
22:06:54.007    pjsua_acc.c !....sip:123host01@sip2sip.info: registration success, status=200 (OK), will re-register in 300 seconds

Registration complete, status= 200 (OK)

---------------------------------------------------------------------
My SIP URI:  sip:123host01@sip2sip.info:50643
Menu:  m=make call, h=hangup call, a=answer call, q=quit
```

Host 2:

```
python sipclient.py
---
sipclient.py -- Simple SIP Client use PJSUA Python Module (PJSIP API)

Your SIP URL [sip:123host01@sip2sip.info]: sip:123host02@sip2sip.info
URL of the registrar [sip:sip2sip.info]: [enter-to-keep-default]
URL of the proxy [sip:proxy.sipthor.net;lr]: [enter-to-keep-default]
Auth Realm [sip2sip.info]: [enter-to-keep-default]
Auth Username [123host01@sip2sip.info]: 123host02@sip2sip.info
Auth Password [**********]: [enter-to-keep-default]
---------------------------------------------------------------------
22:06:54.007    pjsua_acc.c !....sip:123host02@sip2sip.info: registration success, status=200 (OK), will re-register in 300 seconds

Registration complete, status= 200 (OK)

---------------------------------------------------------------------
My SIP URI:  sip:123host02@sip2sip.info:50643
Menu:  m=make call, h=hangup call, a=answer call, q=quit
```

## Release History

* 1.0.0
    * Work in progress

## Meta

Van Toan Ha - Github: [https://github.com/hardw0rk/](https://github.com/hardw0rk/)

Happy coding ! :+1:

[travis-image]: https://img.shields.io/travis/hardw0rk/sipclientdemo/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/hardw0rk/sipclientdemo

