import damv1airtableprojectk8salert as airtblk8salert
from .mytime7 import currentTime7 as cT7, difference_datetimezone7_by_seconds_from_between as diff_btwnsecT7

from enum import Enum

class const_thread(Enum):
    number_1 = 1
    number_2 = 2
    number_3 = 3

aCls = airtblk8salert.sandbox()

dThreadMark = {}
silentLogger = {}

def diffRange_logger(_time=cT7(), **kwargs):
    diffMark = 0
    if '_argThreadNumber' in kwargs:
        threadNumber = kwargs.get("_argThreadNumber")
        key = str(threadNumber).strip()
        if not key in dThreadMark:
            dThreadMark[key] = str(_time).strip()
        else:
            origin_mark = str(dThreadMark[key]).strip()
            # print('  - origin :',origin_mark)
            update_mark = str(_time).strip()
            # print('  - update :',update_mark)
            diffMark = diff_btwnsecT7(origin_mark,update_mark)
            dThreadMark[key] = str(_time).strip()
            # print('    [ Diff :',str(diffMark),'s ]')
    return diffMark

# # Depricated 01 Jan 2023
# def logger(_time=cT7(), *args, **kwargs):   
    
#     print(_time,' '.join(args))

#     try:
#         threadNumber = const_thread.number_1.value
#         if '_argThreadNumber' in kwargs:
#             threadNumber = kwargs.get("_argThreadNumber") 
#             if "'int'" in str(type(threadNumber)):
#                 idAirtable = None
#                 if '_argIdAirtable' in kwargs:
#                     idAirtable = kwargs.get("_argIdAirtable") 
#                     if str(idAirtable).strip()!='':
#                         aCls.pyairtable_updateDateTime_CurrentNumberLastOfLog(threadNumber,idAirtable)
#                         # pass
#     except ValueError:
#         pass


def logger(_time=cT7(), *args, **kwargs):   
    
    messages = ' '.join(args)
    bShow = True
    try:
        threadNumber = const_thread.number_1.value
        if '_argThreadNumber' in kwargs:
            threadNumber = kwargs.get("_argThreadNumber") 
            if "'int'" in str(type(threadNumber)):
                idAirtable = None
                if '_argIdAirtable' in kwargs:
                    idAirtable = kwargs.get("_argIdAirtable") 
                    if not '_argMarkSilentLogger' in kwargs and not '_argDiffMinSecondsSilentLogger_forUpdate':
                        if str(idAirtable).strip()!='':
                            aCls.pyairtable_updateDateTime_CurrentNumberLastOfLog(threadNumber,idAirtable)
                            # pass
                    else:
                        MarkSilentLogger = kwargs.get("_argMarkSilentLogger")
                        DiffMinSecondsSilentLogger_forUpdate = kwargs.get("_argDiffMinSecondsSilentLogger_forUpdate")
                        if "'bool'" in str(type(MarkSilentLogger)):
                            bShow = False
                            silentLogger[str(threadNumber)] = messages
                            if MarkSilentLogger==True:
                                diffRlogger = diffRange_logger(cT7(),_argThreadNumber = threadNumber)
                                if diffRlogger >= int(DiffMinSecondsSilentLogger_forUpdate):
                                    # print('    [ Ready for update airtable ]')
                                    aCls.pyairtable_updateDateTime_CurrentNumberLastOfLog(threadNumber,idAirtable)
                                    # pass


        if bShow == True: print(_time,messages)
    except ValueError:
        pass


# ##Only for testing
# import time
# import random

# # for i in range(1,5):
# #     diffRange_logger(cT7(),_argThreadNumber=1)
# #     time.sleep(2)

# for i in range(1,55):
#     THREADNUMBER = 1
#     random_decimal = random.randint(155, 580)/100

#     msgSilentLogger = ''
#     if str(THREADNUMBER)in silentLogger:
#         msgSilentLogger = silentLogger[str(THREADNUMBER)]
#     print("---> check message from silentLogger :",msgSilentLogger )

#     loggerV2(cT7(),'Hello World!', _argMarkSilentLogger=True, _argDiffMinSecondsSilentLogger_forUpdate = 5, _argThreadNumber=THREADNUMBER, _argIdAirtable='recdObiUDW8KsxW2w')
#     # Q.loggerV2(time7.currentTime7(),'Hello World!', _argMarkSilentLogger=True, _argDiffMinSecondsSilentLogger_forUpdate = 5, _argThreadNumber=THREADNUMBER, _argIdAirtable='recdObiUDW8KsxW2w')

#     time.sleep(random_decimal)
#     # time.sleep(4)
#     print('')