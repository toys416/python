from re import X
import pandas as pd
import numpy as np
import random
import multiprocessing as mp
import datetime 

def TimeLog_CSV(Start_time):
    #Generate channel name and unit
    ChannelName_List = ['Time']
    Unit_List = ['s']
    for i in range(300):                                                                                                          #Variable
        Channel = 'Channel'+'-'+ str(i+1)
        ChannelName_List.append(Channel)

    for i in range(300):                                                                                                          #Variable
        Unit = 'Unit'+'-'+str(i+1)
        Unit_List.append(Unit)
    First_two_rows = pd.DataFrame(list(zip(ChannelName_List,Unit_List))).T

    #Generate Data Frame(Timedelta determines the time shift)
    Date_Time = pd.date_range(start=pd.Timestamp(Start_time), end=pd.Timestamp(Start_time) + pd.Timedelta(4,'d'), freq='1s')      #Variable
    Data_Matrix = np.empty([len(Date_Time),301])                                                                                  #Variable
    Data = pd.DataFrame(Data_Matrix)
    Data.iloc[:,[0]] = Date_Time
    #Add value every 1s(100 Channels)
    Data.iloc[:,1:101] = random.randint(1,10)                                                                                     #Variable
    #Add value every 3s(50 Channels)/5s(120 Channels)/10s(30 Channels)
    row3 = 0
    row5 = 0
    row10 = 0
    for i in range(len(Data.index)):
        Data.iloc[row3,101:151] =random.randint(1,10)                                                                             #Variable
        if row3 <= len(Data.index)-3:
           row3 += 3
        else:
           break
        Data.iloc[row5,151:271] =random.randint(1,10)                                                                             #Variable
        if row5 <= len(Data.index)-5:
           row5 += 5
        Data.iloc[row10,271:] = random.randint(1,10)                                                                              #Variable
        if row10 <= len(Data.index)-10:
           row10 += 10

    #Concat two Data Frame    
    Data_Frame = pd.concat([First_two_rows,Data]) 
    Data_Frame = Data_Frame.mask(Data_Frame.eq(0), '')
    Data_Frame = Data_Frame[:-1]
    #Export CSV
    file = Data_Frame.to_csv('TimeLog From '+ Start_time[:10] + 'To '+ str(pd.Timestamp(Start_time) + pd.Timedelta(4,'d'))[:10]+'.csv',
           encoding='utf-8', index=False,header=False,sep=',')                                                                    #Variable
    return file 

def DepthLog_CSV(Depth):
    totalChannel = 100
    totalDepth = 1000
    
    #Generate channel name and unit
    ChannelName_List = ['Depth']
    Unit_List = ['ft']

    for i in range(totalChannel):                                                                                                          #Variable
        Channel = 'Channel'+'-'+ str(i+1)
        ChannelName_List.append(Channel)

    for i in range(totalChannel):                                                                                                          #Variable
        Unit = 'Unit'+'-'+str(i+1)
        Unit_List.append(Unit)

    First_two_rows = pd.DataFrame(list(zip(ChannelName_List,Unit_List))).T
    #Generate Data Frame(Starting Depth to End Depth)
    Data_Matrix = np.empty([Depth*2+1,101])                                                                                       #Variable
    Data = pd.DataFrame(Data_Matrix)
    Data_Depth = pd.DataFrame(np.arange(2000, Depth + 2000.5, 0.5))                                                               #Variable
    Data.iloc[:,[0]] = Data_Depth
    #Add value every 0.5ft(50 Channels)
    Data.iloc[:,1:51] = random.randint(1,10)                                                                                      #Variable
    #Add value every 1ft(50 Channels)
    row2 = 0
    for i in range(len(Data.index)):
        Data.iloc[row2,51:101] =random.randint(1,10)                                                                              #Variable
        if row2 <= len(Data.index)-2:
           row2 += 2

    #Concat two Data Frame 
    Data_Frame = pd.concat([First_two_rows,Data]) 
    Data_Frame = Data_Frame.mask(Data_Frame.eq(0), '')
    #Export CSV
    file = Data_Frame.to_csv('DepthLog_From_'+ '2000' + '_To_'+ str(Depth+2000)+'_ft.csv',
           encoding='utf-8', index=False,header=False,sep=',')                                                                    #Variable
    return file
 

if __name__ == '__main__':
    print('-----------------------------------------------------------------------------------------------------------------------------------------')
    print('SOP For Time Log at ' + datetime.datetime.now().strftime("%H:%M:%S"))
    N = mp.cpu_count()
    pool = mp.Pool(N)
    time_list = ['2022-08-02 00:00:00+00:00']
    #Files are created by range
    # for i in range(1):                                                                                                            #Variable
    #     time_list.append(str(pd.Timestamp(time_list[i]) + pd.Timedelta(4,'d')))                                                   #Variable
    print(time_list)
    results = pool.map(TimeLog_CSV,time_list)   
    print('Created '+ str(len(time_list)) + ' TimeLog CSV files')
    print('EOP For TimeLog at ' + datetime.datetime.now().strftime("%H:%M:%S"))
    print('-----------------------------------------------------------------------------------------------------------------------------------------')
    # depth = 1000                                                                                                               #Variable
    # DepthLog_CSV(depth)                                                                                                           #Variable
    # print('EOP For DepthLog at ' + datetime.datetime.now().strftime("%H:%M:%S"))
    # print('-----------------------------------------------------------------------------------------------------------------------------------------')







