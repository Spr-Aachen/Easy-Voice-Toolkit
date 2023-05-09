import os
#import time
from typing import Optional
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from threading import currentThread


def TaskAccelerating(
    TargetList: list,
    ArgsList: list = [(), ],
    TypeList: list = ['MultiProcessing', ],
    Workers: Optional[int] = None,
    Asynchronous: bool = False,
    ShowMessages: bool = True
):
    '''
    Function to create pool for multiprocessing/multithreading to accelerate tasks
    '''
    #StartTime = int(time.time())

    ProcessPool = ProcessPoolExecutor(max_workers = Workers)
    ThreadPool = ThreadPoolExecutor(max_workers = Workers)

    for Target in TargetList:
        Args = ArgsList[TargetList.index(Target)]
        Type = TypeList[TargetList.index(Target)]

        if Type == None:
            pass
        
        elif Type == 'MultiProcessing':
            Process = ProcessPool.submit(Target, *Args)
            print(
                "Task start\n" if Asynchronous == True else f"Task start ({TargetList.index(Target) + 1}/{len(TargetList)})\n"
                f"Name : {Target.__name__}\n"
                f"PID  : {os.getpid()}\n"
                "Please wait...\n"
            ) if ShowMessages == True else print('')
            Process.result() if Asynchronous == False else None
        
        elif Type == 'MultiThreading':
            Thread = ThreadPool.submit(Target, *Args)
            print(
                "Task start\n" if Asynchronous == True else f"Task start ({TargetList.index(Target) + 1}/{len(TargetList)})\n"
                f"Name : {Target.__name__}\n"
                f"TID  : {currentThread().ident}\n"
                "Please wait...\n"
            ) if ShowMessages == True else print('')
            Thread.result() if Asynchronous == False else None

        else:
            raise Exception(f"{Type} not found! Use 'MultiProcessing' or 'MultiThreading' instead.")
        
        print(
            f"Task done ({TargetList.index(Target) + 1}/{len(TargetList)})\n"
        ) if ShowMessages == True and Asynchronous == False else print('')
    
    ProcessPool.shutdown(
        wait = False,
        cancel_futures = True
    )
    ThreadPool.shutdown(
        wait = False,
        cancel_futures = True
    )

    print(
        "All done\n"
        "全部完成\n"
    ) if ShowMessages == True else print('')

    #Endtime = int(time.time())