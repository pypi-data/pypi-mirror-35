from multiprocessing import Process
from subprocess import call
from watchgod import watch
import asyncio
from threading import Thread
import time

logo = """

 ######     ###    ########  ##     ## ##    ## ########  
##    ##   ## ##   ##     ## ##     ##  ##  ##  ##     ## 
##        ##   ##  ##     ## ##     ##   ####   ##     ## 
 ######  ##     ## ########  #########    ##    ########  
      ## ######### ##        ##     ##    ##    ##   ##   
##    ## ##     ## ##        ##     ##    ##    ##    ##  
 ######  ##     ## ##        ##     ##    ##    ##     ## 
                                                    
                                          

             ,gaaaaaaaagaaaaaaaaaaaaagaaaaaaaag,
           ,aP8b    _,dYba,       ,adPb,_    d8Ya,
         ,aP"  Yb_,dP"   "Yba, ,adP"   "Yb,_dP  "Ya,
       ,aP"    _88"         )888(         "88_    "Ya,
     ,aP"   _,dP"Yb      ,adP"8"Yba,      dP"Yb,_   "Ya,
   ,aPYb _,dP8    Yb  ,adP"   8   "Yba,  dP    8Yb,_ dPYa,
 ,aP"  YdP" dP     YbdP"      8      "YbdP     Yb "YbP  "Ya,
I8aaaaaa8aaa8baaaaaa88aaaaaaaa8aaaaaaaa88aaaaaad8aaa8aaaaaa8I
`Yb,   d8a, Ya      d8b,      8      ,d8b      aP ,a8b   ,dP'
  "Yb,dP "Ya "8,   dI "Yb,    8    ,dP" Ib   ,8" aP" Yb,dP"
    "Y8,   "YaI8, ,8'   "Yb,  8  ,dP"   `8, ,8IaP"   ,8P"
      "Yb,   `"Y8ad'      "Yb,8,dP"      `ba8P"'   ,dP"
        "Yb,    `"8,        "Y8P"        ,8"'    ,dP"
          "Yb,    `8,         8         ,8'    ,dP"
            "Yb,   `Ya        8        aP'   ,dP"
              "Yb,   "8,      8      ,8"   ,dP"
                "Yb,  `8,     8     ,8'  ,dP"   
                  "Yb, `Ya    8    aP' ,dP"
                    "Yb, "8,  8  ,8" ,dP"
                      "Yb,`8, 8 ,8',dP"
                        "Yb,Ya8aP,dP"
                          "Y88888P"
                            "Y8P"
                              "
"""


def start_watchers(watchers):
    for watcher in watchers:
        def f():
            cmd = watcher["command"]
            call(["/bin/bash", "-c", "cd " + watcher["directory"] +
                  " && "+cmd+""])
        p = Process(target=f)
        p.start()


def start_external():
    call(["python", "manage.py", 'start', "--server-only", '1'])


def stop_external(port):
    call([
        "/bin/bash",
        "-c", "kill -9 $(lsof  -i:" + port+" | grep python | cut -d ' ' -f2)"
    ])


def start_dev_server(path, port):
    p = Process(target=start_external)
    p.daemon = True
    p.start()

    for changes in watch(path):
        for change in changes:
            (change, file) = change
            if file.endswith(('.py', '.pyx', '.pyd')):
                stop_external(str(port))
                time.sleep(1)
                p.terminate()
                while p.is_alive():
                    time.sleep(1)
                p = Process(target=start_external)
                p.daemon = True
                p.start()

                break
