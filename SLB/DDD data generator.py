from re import X
import pandas as pd
import numpy as np
import random
import multiprocessing as mp
import datetime 
import schedule



def TimeLog_CSV(Start_time):
    #Generate channel name and unit
    ChannelName_List = ['Time',"DrillBoreHole.TDREF.Projected"]
    Unit_List = ['s',"m"]
    for i in range(300):                                                                                                          #Variable
        Channel = 'Channel'+'-'+ str(i+1) +".Projected"
        ChannelName_List.append(Channel)

    for i in range(300):                                                                                                          #Variable
        Unit = 'Unit'+'-'+str(i+1)
        Unit_List.append(Unit)
    First_two_rows = pd.DataFrame(list(zip(ChannelName_List,Unit_List))).T

    #Generate Data Frame(Timedelta determines the time shift)
    Date_Time = pd.date_range(start=pd.Timestamp(Start_time), end=pd.Timestamp(Start_time) + pd.Timedelta(4,'d'), freq='1s')      #Variable
    Date_Depth = np.arange(0,len(Date_Time)*0.15,0.15)
    Data_Matrix = np.empty([len(Date_Time),302])                                                                                  #Variable
    Data = pd.DataFrame(Data_Matrix)
    Data.iloc[:,0] = Date_Time
    Data.iloc[:,1] = Date_Depth
    Data.iloc[:,1] = Date_Depth.astype("str")
    #Add value every 1s(100 Channels)
    Data.iloc[:,2:] = random.randint(1,10)                                                                                     #Variable
    #Concat two Data Frame    
    Data_Frame = pd.concat([First_two_rows,Data]) 
    Data_Frame = Data_Frame.mask(Data_Frame.eq(0), '')
    Data_Frame = Data_Frame[:-1]
    #Export CSV
    file = Data_Frame.to_csv('TimeLog From '+ Start_time[:10] + 'To '+ str(pd.Timestamp(Start_time) + pd.Timedelta(4,'d'))[:10]+'.csv',
           encoding='utf-8', index=False,header=False,sep=',')                                                                    #Variable
    return file 



if __name__ == '__main__':
    print('-----------------------------------------------------------------------------------------------------------------------------------------')
    print('SOP For Time Log at ' + datetime.datetime.now().strftime("%H:%M:%S"))
    # N = mp.cpu_count()
    # print(N)
    # pool = mp.Pool(N)
    time_list = ['2022-08-01 00:00:00+00:00']
    #Files are created by range
    # for i in range(1):                                                                                                            #Variable
    #     time_list.append(str(pd.Timestamp(time_list[i]) + pd.Timedelta(4,'d')))                                                   #Variable
    # results = pool.map(TimeLog_CSV,time_list)
    TimeLog_CSV(time_list[0])
    print('Created '+ str(len(time_list)) + ' TimeLog CSV files')
    print('EOP For TimeLog at ' + datetime.datetime.now().strftime("%H:%M:%S"))