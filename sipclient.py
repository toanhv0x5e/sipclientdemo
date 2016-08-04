# sipclient.py -- Simple SIP Client use PJSUA Python Module (PJSIP API) 
# Edited by: Ha Van Toan 
# Email: hatoan[dot]vniss[at]gmail[dot]com 
# Last edit: 04/08/2016 

import sys
import os
import threading
import wave
from time import sleep
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

    def __init__(self, account=None):
        pj.AccountCallback.__init__(self, account)

    # Wait for register
    def wait(self):
        self.sem = threading.Semaphore(0)
        self.sem.acquire()

    def on_reg_state(self):
        if self.sem:
            if self.account.info().reg_status >= 200:
                self.sem.release()
    '''
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
    '''
# https://trac.pjsip.org/repos/wiki/Python_SIP/Calls#HandlingCallEvents
# http://www.pjsip.org/python/pjsua.htm#CallCallback
class MyCallCallback(pj.CallCallback):
    def __init__(self, call=None):
        pj.CallCallback.__init__(self, call)

    # Notification when call state has changed
    def on_state(self):
        global current_call
        global in_call
        print "Call with", self.call.info().remote_uri,
        print "is", self.call.info().state_text,
        print "last code =", self.call.info().last_code, 
        print "(" + self.call.info().last_reason + ")"
        
        if self.call.info().state == pj.CallState.DISCONNECTED:
            current_call = None
            print 'Current call is', current_call
            in_call = False
        elif self.call.info().state == pj.CallState.CONFIRMED:
            # Call is Answered
            print "Call Answered"
            wfile = wave.open("free.wav")
            time = (1.0 * wfile.getnframes ()) / wfile.getframerate ()
            print str(time) + "ms"
            wfile.close()
            call_slot = self.call.info().conf_slot
            self.wav_player_id=pj.Lib.instance().create_player('free.wav',loop=False)
            self.wav_slot=pj.Lib.instance().player_get_slot(self.wav_player_id)
            pj.Lib.instance().conf_connect(self.wav_slot, call_slot)
            sleep(time)
            pj.Lib.instance().player_destroy(self.wav_player_id)
            self.call.hangup()
            in_call = False

    # Notification when call's media state has changed.
    def on_media_state(self):
        if self.call.info().media_state == pj.MediaState.ACTIVE:
            print "Media is now active"
        else:
            print "Media is inactive"

# Function to make call
def make_call(uri):
    try:
        print "Making call to", uri
        return acc.make_call(uri, cb=MyCallCallback())
    except pj.Error, e:
        print "Exception: " + str(e)
        return None

def cb_func(pid) :
    print '%s playback is done' % pid
    current_call.hangup()


try:
    # http://www.pjsip.org/python/pjsua.htm#UAConfig
    my_ua_cfg = pj.UAConfig()
    my_ua_cfg.nameserver = ['8.8.8.8', '8.8.4.4']
    my_ua_cfg.user_agent = "123Host SIP Client"
    # http://www.pjsip.org/python/pjsua.htm#MediaConfig
    my_media_cfg = pj.MediaConfig()
    my_media_cfg.enable_ice = True
    
    #
    # Procedure: Initialize > Create Transpot > Start > Handle calls > Shutdown
    #

    # https://trac.pjsip.org/repos/wiki/Python_SIP/Settings#StartupandShutdown
    # Initialize the Library
    lib.init(ua_cfg=my_ua_cfg, media_cfg=my_media_cfg, log_cfg = pj.LogConfig(level=3, callback=log_cb))
    
    # Create One or More Transports
    transport = lib.create_transport(pj.TransportType.UDP, pj.TransportConfig(0))
    #transport = lib.create_transport(pj.TransportType.TLS, pj.TransportConfig(port=5060)) # SSL
    lib.set_null_snd_dev()

    # Starting the Library
    lib.start()
    lib.handle_events()

    #
    # Registration
    #
    acc_cfg = pj.AccountConfig()
    os.system('clear')
    print "sipclient.py -- Simple SIP Client use PJSUA Python Module (PJSIP API)"
    print ""
    #
    acc_cfg.id = raw_input("Your SIP URL [sip:123host01@sip2sip.info]: ")
    if ((acc_cfg.id) and len(acc_cfg.id) > 0):
        pass
    else:
        acc_cfg.id = "sip:123host01@sip2sip.info"
    #
    acc_cfg.reg_uri  = raw_input("URL of the registrar [sip:sip2sip.info]: ")
    if ((acc_cfg.reg_uri) and len(acc_cfg.reg_uri) > 0):
        pass
    else:
        acc_cfg.reg_uri  = "sip:sip2sip.info"
    #
    acc_cfg.proxy = [] 
    proxy = raw_input("URL of the proxy [sip:proxy.sipthor.net;lr]: ")
    acc_cfg.proxy.append(proxy)
    if ((proxy) and len(proxy) > 0):
        pass
    else:
        acc_cfg.proxy = [ "sip:proxy.sipthor.net;lr" ]
    #
    realm = raw_input("Auth Realm [sip2sip.info]: ")
    if ((realm) and len(realm) > 0):
        pass
    else:
        realm = "sip2sip.info"
    #
    username = raw_input("Auth Username [123host01@sip2sip.info]: ")
    if ((username) and len(username) > 0):
        pass
    else:
        username = "123host01@sip2sip.info"
    #
    passwd = raw_input("Auth Password [12345678a@]: ")
    if ((passwd) and len(passwd) > 0):
        pass
    else:
        passwd = "12345678a@"
    print "---------------------------------------------------------------------"

    acc_cfg.auth_cred = [pj.AuthCred(realm, username ,passwd)]
    
    acc_cb = MyAccountCallback(acc_cfg)
    acc = lib.create_account(acc_cfg, cb=acc_cb)
    
    acc_cb.wait()
    print ""
    print "Registration complete, status=", acc.info().reg_status, \
          "(" + acc.info().reg_reason + ")"

    my_sip_uri = acc_cfg.id + ":" + str(transport.info().port)

    # Menu loop
    while True:
        print ""
        print "---------------------------------------------------------------------"
        print "My SIP URI: ", my_sip_uri
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
            in_call = True
            lck = lib.auto_lock()
            current_call = make_call(input)
            print 'Current call is', current_call
            del lck
            # Wait for the call to end before shuting down
            while in_call:
                pass
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
    transport = None
    acc_cb.delete()
    acc_cb = None


except pj.Error, e:
    print "Exception: " + str(e)
    # Handle if throw exception, will shutdown library and termination
    lib.destroy()
    lib = None
    sys.exit(1)

