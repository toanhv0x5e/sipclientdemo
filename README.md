# SIP Client Demo
> Just an SIP Client (VoIP) use pjsua python module

[![Build Status][travis-image]][travis-url]

![](header.png)

## Installation

Linux:

```sh
# test
```

## Usage example

- Tài khoản dùng để test:

```
SIP Address: 123host01@sip2sip.info
Username: 123host01
Domain/Realm: sip2sip.info

SIP Address: 123host02@sip2sip.info
Username: 123host02
Domain/Realm: sip2sip.info

Password: 12345678a@
```

- Xem thông tin tài khoản:

[http://sip2sip.info](http://sip2sip.info)

- Chạy phần mềm SIP Client trên 2 Host khác nhau:

Host 1: 

    python sipclient.py
    ---
    sipclient.py -- Simple SIP Client use PJSUA Python Module (PJSIP API)

    Your SIP URL [sip:123host01@sip2sip.info]: [enter-để-giữ-mặc-định]
    URL of the registrar [sip:sip2sip.info]: [enter-để-giữ-mặc-định]
    URL of the proxy [sip:proxy.sipthor.net;lr]: [enter-để-giữ-mặc-định]
    Auth Realm [sip2sip.info]: [enter-để-giữ-mặc-định]
    Auth Username [123host01@sip2sip.info]: [enter-để-giữ-mặc-định]
    Auth Password [12345678a@]: [enter-để-giữ-mặc-định]
    ---------------------------------------------------------------------
    22:06:54.007    pjsua_acc.c !....sip:123host01@sip2sip.info: registration success, status=200 (OK), will re-register in 300 seconds

    Registration complete, status= 200 (OK)

    ---------------------------------------------------------------------
    My SIP URI:  sip:123host01@sip2sip.info:50643
    Menu:  m=make call, h=hangup call, a=answer call, q=quit

Host 2: 

    python sipclient.py
    ---
    sipclient.py -- Simple SIP Client use PJSUA Python Module (PJSIP API)

    Your SIP URL [sip:123host01@sip2sip.info]: sip:123host02@sip2sip.info
    URL of the registrar [sip:sip2sip.info]: [enter-để-giữ-mặc-định]
    URL of the proxy [sip:proxy.sipthor.net;lr]: [enter-để-giữ-mặc-định]
    Auth Realm [sip2sip.info]: [enter-để-giữ-mặc-định]
    Auth Username [123host01@sip2sip.info]: 123host02@sip2sip.info
    Auth Password [12345678a@]: [enter-để-giữ-mặc-định]
    ---------------------------------------------------------------------
    22:06:54.007    pjsua_acc.c !....sip:123host02@sip2sip.info: registration success, status=200 (OK), will re-register in 300 seconds

    Registration complete, status= 200 (OK)

    ---------------------------------------------------------------------
    My SIP URI:  sip:123host02@sip2sip.info:50643
    Menu:  m=make call, h=hangup call, a=answer call, q=quit


## Development setup

Test

```sh
test
```

## Release History

* 1.0.0
    * Work in progress

## Meta

Van Toan Ha

[https://github.com/hardw0rk/](https://github.com/hardw0rk/)

[travis-image]: https://img.shields.io/travis/hardw0rk/sipclientdemo/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/hardw0rk/sipclientdemo
