# Thread batch with timeout - return values in dict 


1) import threadingbatch
2) add the decorator @threadingbatch.thread_capture to your function
3) add \*args, \*\*kwargs to your function
4) create a list of lists with all function calls 
5) call threadingbatch.start_all_threads
6) get the results from threadingbatch.results

```python
$ pip install threadingbatch
from kthread_sleep import sleep  # killing might not work with time.sleep ( pip install kthread-sleep )
import threadingbatch
import random


@threadingbatch.thread_capture  # The threaded function must be decorated
def test(
    testnumber, *args, **kwargs
):  # a threaded function must have *args, **kwargs and can't have the keyword argument _starttime

    print(f"start {testnumber}")
    sleep(1)
    v = random.randrange(1, 30)
    print(f"end {testnumber}")
    return v


flist = []
for ini, k in enumerate(range(20)):  # creating 20 function calls

    flist.append(
        [
            test,  # function
            (),  # args
            {"testnumber": ini},  # kwargs
            f"function_{str(ini)}",  # key in threadingbatch.results (must be unique and type str), the key can't have the name "done"
        ]
    )
flistt = threadingbatch.start_all_threads(
    flist,
    threadtlimit=5,  # number of simultaneously executed threads
    timeout=4,  # call Kthread.kill after n seconds
    sleepafterkill=0.02,  # sleep time after calling Kthread.kill
    sleepafterstart=0.02,  # sleep time after starting a thread
    ignore_exceptions=False,
    verbose=False,
)

while not threadingbatch.results[
    "done"
]:  # when all threads are done, threadingbatch.results['done'] changes to True

    pass
    sleep(0.1)

# output:
# start 0
# start 1
# start 2
# start 3
# start 4
# start 5
# end 0
# start 6
# end 1
# start 7
# end 2
# start 8
# end 3
# ....

print(threadingbatch.results)
# defaultdict(<function threadingbatch.<lambda>()>,
#             {'done': True,
#              'function_19': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 11, 'realstart': 1673158006.740858}),
#              'function_18': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 23, 'realstart': 1673158006.4810376}),
#              'function_17': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 14, 'realstart': 1673158005.2808566}),
#              'function_16': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 1, 'realstart': 1673158005.1208546}),
#              'function_15': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 4, 'realstart': 1673158005.0807495}),
#              'function_14': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 23, 'realstart': 1673158004.7609262}),
#              'function_13': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 15, 'realstart': 1673158004.7207859}),
#              'function_12': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 4, 'realstart': 1673158004.5210721}),
#              'function_11': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 15, 'realstart': 1673158002.9808593}),
#              'function_10': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 4, 'realstart': 1673158002.941067}),
#              'function_9': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 20, 'realstart': 1673158002.9007895}),
#              'function_8': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 29, 'realstart': 1673158002.420729}),
#              'function_7': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 6, 'realstart': 1673158002.3609126}),
#              'function_6': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 16, 'realstart': 1673158002.3207767}),
#              'function_5': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 1, 'realstart': 1673158000.5775528}),
#              'function_4': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 18, 'realstart': 1673158000.5409462}),
#              'function_3': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 23, 'realstart': 1673158000.5010219}),
#              'function_2': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 14, 'realstart': 1673158000.4609187}),
#              'function_1': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 10, 'realstart': 1673158000.420832}),
#              'function_0': defaultdict(<function threadingbatch.<lambda>()>,
#                          {'results': 12, 'realstart': 1673158000.370694})})



```



