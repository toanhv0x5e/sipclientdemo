# sipclient.py -- Simple SIP Client use PJSUA Python Module (PJSIP API) 
# Edited by: Ha Van Toan 
# Email: hatoan[dot]vniss[at]gmail[dot]com 
# Last edit: 02/08/2016 

import sys
# https://trac.pjsip.org/repos/wiki/Python_SIP/Settings#InstantiatetheLibrary
import pjsua as pj

lib = pj.Lib()

current_call = None

# http://www.pjsip.org/python/pjsua.htm#LogConfig
def log_cb(level, str, len):
    print str,

# Overriding abstract classes
# https://trac.pjsip.org/repos/wiki/Python_SIP/Calls#ReceivingIncomingCalls
# http://www.pjsip.org/python/pjsua.htm#AccountCallback
class MyAccountCallback(pj.AccountCallback):
    sem = None # variable to determine register status

    def __init__(self, account):
        pj.AccountCallback.__init__(self, account)

    # Wait for register
    def wait(self):
        self.sem = threading.Semaphore(0)
        self.sem.acquire()

    def on_reg_state(self):
        if self.sem:
            if self.account.info().reg_status >= 200:
                self.sem.release()

    # Notification on incoming call
    def on_incoming_call(self, call):
        global current_call 
        if current_call:
            call.answer(486, "Busy")
            return
            
        print "Incoming call from ", call.info().remote_uri
        print "Press 'a' to answer"

        current_call = call

        call_cb = MyCallCallback(current_call)
        current_call.set_callback(call_cb)

        current_call.answer(180)

# https://trac.pjsip.org/repos/wiki/Python_SIP/Calls#HandlingCallEvents
# http://www.pjsip.org/python/pjsua.htm#CallCallback
class MyCallCallback(pj.CallCallback):
    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)

    # Notification when call state has changed
    def on_state(self):
        print "Call is ", self.call.info().state_text,
        print "last code =", self.call.info().last_code, 
        print "(" + self.call.info().last_reason + ")"

    # Notification when call's media state has changed.
    def on_media_state(self):
        if self.call.info().media_state == pjsua.MediaState.ACTIVE:
            print "Media is now active"
        else:
            print "Media is inactive"

    # Notification when call's media state has changed.
    def on_media_state(self):
        global lib
        if self.call.info().media_state == pj.MediaState.ACTIVE:
            # Connect the call to sound device
            call_slot = self.call.info().conf_slot
            lib.conf_connect(call_slot, 0)
            lib.conf_connect(0, call_slot)
            print "Hello world, I can talk!"

def
    acc_cfg = pj.AccountConfig()
    acc_cfg.id = "sip:123host01@sip2sip.info"
    acc_cfg.reg_uri = "sip:sip2sip.info"
    #acc_cfg.reg_uri = "sip:sip2sip.info;transport=tls"
    acc_cfg.proxy = [ "sip:proxy.sipthor.net;lr" ]
    acc_cfg.auth_cred = [pj.AuthCred(
        realm="sip2sip.info",
        username="123host01",
        passwd="12345678a@",
    )]

    acc_cb = MyAccountCallback(acc_cfg)
    acc = lib.create_account(acc_cfg, cb=acc_cb)
    
    acc_cb.wait()
    print "\n"
    print "Registration complete, status=", acc.info().reg_status, \
          "(" + acc.info().reg_reason + ")"


try:
    # http://www.pjsip.org/python/pjsua.htm#UAConfig
    my_ua_cfg = pj.UAConfig()
    my_ua_cfg.nameserver = ['8.8.8.8', '8.8.4.4'] # Example: Google Public DNS
    #my_ua_cfg.stun_host = "stun.pjsip.org"
    # http://www.pjsip.org/python/pjsua.htm#MediaConfig
    my_media_cfg = pj.MediaConfig()
    my_media_cfg.enable_ice = True
    
    # Procedure: Initialize > Create Transpot > Start > Handle calls > Shutdown
    # https://trac.pjsip.org/repos/wiki/Python_SIP/Settings#StartupandShutdown
    # Initialize the Library
    lib.init(ua_cfg=my_ua_cfg, media_cfg=my_media_cfg, log_cfg = pj.LogConfig(level=3, callback=log_cb))
    
    # Create One or More Transports
    lib.create_transport(pjsua.TransportType.UDP, pjsua.TransportConfig(5080))
    #transport = lib.create_transport(pj.TransportType.TLS, pj.TransportConfig(port=5060)) # SSL
    lib.set_null_snd_dev()
    #print "\nListening on", transport.info().host, 
    #print "port", transport.info().port, "\n"

    # Starting the Library
    lib.start()
    lib.handle_events()

    ############################
    # Handle calls
    # Create local/user-less account, example: "sip:127.0.0.1"
    acc_cb = MyAccountCallback()
    acc = lib.create_account_for_transport(transport, cb=acc_cb)

    # https://trac.pjsip.org/repos/wiki/Python_SIP/Calls#MakingOutgoingCalls
    dst_uri="sip:127.0.0.1:5060"
    my_cb = MyCallCallback()
    call = acc.make_call(dst_uri, cb=my_cb)

    # Wait for ENTER before quitting
    print "Press <ENTER> to quit"
    input = sys.stdin.readline().rstrip("\r\n")

    ############################

    # Menu loop
    while True:
        print "My SIP URI is", my_sip_uri
        print "Menu:  m=make call, h=hangup call, a=answer call, q=quit"

        input = sys.stdin.readline().rstrip("\r\n")
        if input == "m":
            if current_call:
                print "Already have another call"
                continue
            print "Enter destination URI to call: ", 
            input = sys.stdin.readline().rstrip("\r\n")
            if input == "":
                continue
            lck = lib.auto_lock()
            current_call = make_call(input)
            del lck

        elif input == "h":
            if not current_call:
                print "There is no call"
                continue
            current_call.hangup()

        elif input == "a":
            if not current_call:
                print "There is no call"
                continue
            current_call.answer(200)

        elif input == "q":
            break


    # Shutting Down the Library
    lib.destroy()
    lib = None

except pj.Error, err:
    print "Exception: " + str(e)
    # Handle if throw exception, will shutdown library and termination
    lib.destroy()
    lib = None
    sys.exit(1)
    #exit(0): EXIT_SUCCESS -- successful termination. This causes the program to exit with a successful termination.
    #exit(1): EXIT_FAILURE -- unsuccessful termination. This causes the program to exit with a system-specific meaning.

# Generate free.wav

# festival is a tool text-to-speech
#sudo pacman -S festival festival-us

# text2wave is a tool convert text-to-speech to wav
#text2wave -o free.wav message.txt

# Account SIP

#SIP Address    123host01@sip2sip.info
#Username       123host01
#Domain/Realm   sip2sip.info

#SIP Address    123host02@sip2sip.info
#Username       123host02
#Domain/Realm   sip2sip.info

#Password       12345678a@

# Source code uploaded to VPS: 103.255.236.99
