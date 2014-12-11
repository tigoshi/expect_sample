import os
import pexpect
import fdpexpect
import time

fd = os.open("/dev/ttyUSB0", os.O_RDWR|os.O_NONBLOCK|os.O_NOCTTY )
print fd
m = fdpexpect.fdspawn(fd)

send_str = "info"
print "##########"
print "sending " + send_str
m.sendline(send_str) # Escape sequence
print "wait response....."
time.sleep(1)
m.expect("hermit>")
#m.expect("hermit> \r\nhermit>")
string = m.before
string_a = m.after
print "before " + string
print "after " + string_a
print "########## done..... ##########"

send_str = "memmap"
print "##########"
print "sending " + send_str
m.sendline(send_str) # Escape sequence
print "wait response....."
m.expect("hermit>")
string = m.before
string_a = m.after
print "before " + string
print "after " + string_a
print "########## done..... ##########"

send_str = "memmap"
print "##########"
print "sending " + send_str
m.sendline(send_str) # Escape sequence
print "wait response....."
m.expect("hermit>")
string = m.before
string_a = m.after
print "before " + string
print "after " + string_a
print "########## done..... ##########"

