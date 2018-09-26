import os 
import signal 

#向24051进程发送SIGKILL信号
os.kill(24051,signal.SIGKILL)