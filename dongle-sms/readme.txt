send-mail.py 
============

Originally created to be used with FreePBX(asterisk)+mod_dongle to forward SMS and USSD messages to mailbox.


Configuration:
--------------

1. 
chown asterisk:asterisk /etc/asterisk/send_mail.py
chmod 750 /etc/asterisk/send_mail.py

2. edit /etc/asterisk/send_mail.py, set mailbox credentials.
   (make sure asterisk user has write access to the log file)

3. add to /etc/asterisk/extensions_custom.conf
```
[from-pstn-custom]
include => dongle-incoming-sms
include => dongle-incoming-ussd

[dongle-incoming-sms]
exten => sms,1,Noop(Incoming SMS from ${CALLERID(num)} ${BASE64_DECODE(${SMS_BASE64})})
exten => sms,n,System(echo '${STRFTIME(${EPOCH},,%Y-%m-%d %H:%M:%S)} - ${DONGLENAME}(${DONGLENUMBER}) - ${CALLERID(num)}: ${BASE64_DECODE(${SMS_BASE64})}' |/etc/asterisk/send_mail.py)
exten => sms,n,Hangup()

[dongle-incoming-ussd]
exten => ussd,1,Noop(Incoming USSD for ${DONGLENAME}: ${BASE64_DECODE(${USSD_BASE64})})
exten => ussd,n,System(echo '${STRFTIME(${EPOCH},,%Y-%m-%d %H:%M:%S)} - ${DONGLENAME}(${DONGLENUMBER}): ${BASE64_DECODE(${USSD_BASE64})}' |/etc/asterisk/send_mail.py)
exten => ussd,n,Hangup()
```
