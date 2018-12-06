from django.shortcuts import render
from django.http import HttpResponse
#from ipynb
import pandas as pd
import numpy as np
from string import Template
import math

def home(request) :
    return render(request, 'diagnose/index.html')

def about(request) :
    return HttpResponse("Made by Kelompok 24: 13515020, 13515022, 135100, 13515101, 13515148, 13515601")

def result(request) :
    data = pd.read_csv('./tubes2_HeartDisease_train.csv')
    dataMean = pd.read_csv('./tubes2_HeartDisease_train.csv')
    dataMode = pd.read_csv('./tubes2_HeartDisease_train.csv')
    dataDropped = pd.read_csv('./tubes2_HeartDisease_train.csv')
    dataMeanDropped = pd.read_csv('./tubes2_HeartDisease_train.csv')
    dataModeDropped = pd.read_csv('./tubes2_HeartDisease_train.csv')

    # panjang kolom dan baris data                
    col = data.shape[1]
    row = data.shape[0]

    # Mengubah data kosong menjadi missing value , data kosong di dataDropped di drop
    for i in range(col):
        for j in range(row):
            if (data.iat[j,i] != '?'):
                if (math.isnan(float(data.iat[j,i]))):
                    data.iat[j,i] = '?'
                    dataMean.iat[j,i] = '?'
                    dataMode.iat[j,i] = '?'
                    dataDropped = dataDropped.drop(j)
                    dataMeanDropped = dataMeanDropped.drop(j)
                    dataModeDropped = dataModeDropped.drop(j)


    # metadata data
    collumns = []
    modes = []
    means = []
    numberOfDefinedData = []
    sums = []

    #Array of collumn name
    s = Template('Column$a')
    for i in range(col): 
        collumns.append(s.substitute(a=i+1))
                
    #Dapet modus tiap kolom. Kalau modusnya '?', ambil modus kedua
    for i in collumns:
        if (data[i].value_counts().keys()[0] == '?'):        
            modes.append(data[i].value_counts().keys()[1])
        else:
            modes.append(data[i].value_counts().keys()[0])

    # Dapet Rataan tiap kolom data non drop
    for i in range(col):    
        sum = 0
        count = 0
        for j in range(row):
            if (data.iat[j,i] != '?'):            
                count += 1
                sum += float(data.iat[j,i])
        numberOfDefinedData.append(count)
        sums.append(sum)
        if (i in [3,4,7,9]):
            means.append(float(sum / count))
        elif (i == 1):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 2):
            legalValues = [1,2,3,4]
            modifiedLegalValues = [1,2,3,4]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 5):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 6):
            legalValues = [2,1,0]
            modifiedLegalValues = [2,1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 8):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 10):
            legalValues = [1,2,3]
            modifiedLegalValues = [1,2,3]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 11):
            legalValues = [0,1,2,3]
            modifiedLegalValues = [0,1,2,3]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 12):
            legalValues = [3,6,7]
            modifiedLegalValues = [3,6,7]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 13):
            legalValues = [0,1,2,3,4]
            modifiedLegalValues = [0,1,2,3,4]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        else:        
            means.append(int(sum / count))

    # mengubah data mean
    for i in range(col):
        for j in range(row):
            if (data.iat[j,i] == '?'):
                dataMean.iat[j,i] = means[i]
                
    # mengubah data modus
    for i in range(col):
        for j in range(row):
            if (data.iat[j,i] == '?'):
                dataMode.iat[j,i] = modes[i]            
            
    # panjang kolom dan baris dataDropped
    colDropped = dataDropped.shape[1]
    rowDropped = dataDropped.shape[0]

    # metadata dataDropped
    collumnsDropped = []
    modesDropped = []
    meansDropped = []
    numberOfDefinedDataDropped = []
    sumsDropped = []

    #Array of collumn name
    s = Template('Column$a')
    for i in range(colDropped): 
        collumnsDropped.append(s.substitute(a=i+1))
                
    #Dapet modus tiap kolom. Kalau modusnya '?', ambil modus kedua
    for i in collumnsDropped:
        if (dataDropped[i].value_counts().keys()[0] == '?'):        
            modesDropped.append(dataDropped[i].value_counts().keys()[1])
        else:
            modesDropped.append(dataDropped[i].value_counts().keys()[0])

    # Dapet Rataan tiap kolom data non drop
    for i in range(colDropped):    
        sum = 0
        count = 0
        for j in range(rowDropped):
            if (dataDropped.iat[j,i] != '?'):            
                count += 1
                sum += float(dataDropped.iat[j,i])
        numberOfDefinedDataDropped.append(count)
        sumsDropped.append(sum)
        if (i in [3,4,7,9]):
            meansDropped.append(float(sum / count))
        elif (i == 1):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 2):
            legalValues = [1,2,3,4]
            modifiedLegalValues = [1,2,3,4]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 5):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 6):
            legalValues = [2,1,0]
            modifiedLegalValues = [2,1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 8):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 10):
            legalValues = [1,2,3]
            modifiedLegalValues = [1,2,3]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 11):
            legalValues = [0,1,2,3]
            modifiedLegalValues = [0,1,2,3]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 12):
            legalValues = [3,6,7]
            modifiedLegalValues = [3,6,7]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 13):
            legalValues = [0,1,2,3,4]
            modifiedLegalValues = [0,1,2,3,4]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        else:        
            meansDropped.append(int(sum / count))

    # mengubah data mean
    for i in range(colDropped):
        for j in range(rowDropped):
            if (dataDropped.iat[j,i] == '?'):
                dataMeanDropped.iat[j,i] = meansDropped[i]
                
    # mengubah data modus
    for i in range(colDropped):
        for j in range(rowDropped):
            if (dataDropped.iat[j,i] == '?'):
                dataModeDropped.iat[j,i] = modesDropped[i]

    # bagian data test
    col1 = request.GET.get('col1')
    col2 = request.GET.get('col2')
    col3 = request.GET.get('col3')
    col4 = request.GET.get('col4')
    col5 = request.GET.get('col5')
    col6 = request.GET.get('col6')
    col7 = request.GET.get('col7')
    col8 = request.GET.get('col8')
    col9 = request.GET.get('col9')
    col10 = request.GET.get('col10')
    col11 = request.GET.get('col11')
    col12 = request.GET.get('col12')
    col13 = request.GET.get('col13')

    data1 = int("{}".format(col1))
    data2 = int("{}".format(col2))
    data3 = int("{}".format(col3))
    data4 = int("{}".format(col4))
    data5 = int("{}".format(col5))
    data6 = int("{}".format(col6))
    data7 = int("{}".format(col7))
    data8 = int("{}".format(col8))
    data9 = int("{}".format(col9))
    data10 = int("{}".format(col10))
    data11 = int("{}".format(col11))
    data12 = int("{}".format(col12))
    data13 = int("{}".format(col13))

    datax = {
        'Coloumn1' : pd.Series([data1],index=[0]),
        'Coloumn2' : pd.Series([data2],index=[0]),
        'Coloumn3' : pd.Series([data3],index=[0]),
        'Coloumn4' : pd.Series([data4],index=[0]),
        'Coloumn5' : pd.Series([data5],index=[0]),
        'Coloumn6' : pd.Series([data6],index=[0]),
        'Coloumn7' : pd.Series([data7],index=[0]),
        'Coloumn8' : pd.Series([data8],index=[0]),
        'Coloumn9' : pd.Series([data9],index=[0]),
        'Coloumn10' : pd.Series([data10],index=[0]),
        'Coloumn11' : pd.Series([data11],index=[0]),
        'Coloumn12' : pd.Series([data12],index=[0]),
        'Coloumn13' : pd.Series([data13],index=[0]),
    }

    data_test = pd.DataFrame(datax)
    dataMean_test = pd.DataFrame(datax)
    dataMode_test = pd.DataFrame(datax)
    dataDropped_test = pd.DataFrame(datax)
    dataMeanDropped_test = pd.DataFrame(datax)
    dataModeDropped_test = pd.DataFrame(datax)

    # panjang kolom dan baris data                
    col = data_test.shape[1]
    row = data_test.shape[0]

    # Mengubah data kosong menjadi missing value , data kosong di dataDropped di drop
    for i in range(col):
        for j in range(row):
            if (data_test.iat[j,i] != '?'):
                if (math.isnan(float(data_test.iat[j,i]))):
                    data_test.iat[j,i] = '?'
                    dataMean_test.iat[j,i] = '?'
                    dataMode_test.iat[j,i] = '?'
                    dataDropped_test = dataDropped_test.drop(j)
                    dataMeanDropped_test = dataMeanDropped_test.drop(j)
                    dataModeDropped_test = dataModeDropped_test.drop(j)

    # metadata data
    collumns = []
    modes = []
    means = []
    numberOfDefinedData = []
    sums = []

    #Array of collumn name
    s = Template('Column$a')
    for i in range(col): 
        collumns.append(s.substitute(a=i+1))
                
    #Dapet modus tiap kolom. Kalau modusnya '?', ambil modus kedua
    for i in range(len(collumns)):
        modes.append(data_test.iat[0,i])

    # Dapet Rataan tiap kolom data non drop
    for i in range(col):    
        sum = 0
        count = 0
        for j in range(row):
            if (data_test.iat[j,i] != '?'):            
                count += 1
                sum += float(data_test.iat[j,i])
        numberOfDefinedData.append(count)
        sums.append(sum)
        if (i in [3,4,7,9]):
            means.append(float(sum / count))
        elif (i == 1):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 2):
            legalValues = [1,2,3,4]
            modifiedLegalValues = [1,2,3,4]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 5):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 6):
            legalValues = [2,1,0]
            modifiedLegalValues = [2,1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 8):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 10):
            legalValues = [1,2,3]
            modifiedLegalValues = [1,2,3]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 11):
            legalValues = [0,1,2,3]
            modifiedLegalValues = [0,1,2,3]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 12):
            legalValues = [3,6,7]
            modifiedLegalValues = [3,6,7]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 13):
            legalValues = [0,1,2,3,4]
            modifiedLegalValues = [0,1,2,3,4]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            means.append(legalValues[legalValues.index(min(legalValues))])
        else:        
            means.append(int(sum / count))

    # mengubah data mean
    for i in range(col):
        for j in range(row):
            if (data_test.iat[j,i] == '?'):
                dataMean_test.iat[j,i] = means[i]
                
    # mengubah data modus
    for i in range(col):
        for j in range(row):
            if (data_test.iat[j,i] == '?'):
                dataMode_test.iat[j,i] = modes[i]            
            
    # panjang kolom dan baris dataDropped
    colDropped = dataDropped_test.shape[1]
    rowDropped = dataDropped_test.shape[0]

    # metadata dataDropped
    collumnsDropped = []
    modesDropped = []
    meansDropped = []
    numberOfDefinedDataDropped = []
    sumsDropped = []

    #Array of collumn name
    s = Template('Column$a')
    for i in range(colDropped): 
        collumnsDropped.append(s.substitute(a=i+1))
                
    #Dapet modus tiap kolom. Kalau modusnya '?', ambil modus kedua
    for i in range(len(collumnsDropped)):
        modesDropped.append(dataDropped_test.iat[0,i])

    # Dapet Rataan tiap kolom data non drop
    for i in range(colDropped):    
        sum = 0
        count = 0
        for j in range(rowDropped):
            if (dataDropped_test.iat[j,i] != '?'):            
                count += 1
                sum += float(dataDropped_test.iat[j,i])
        numberOfDefinedDataDropped.append(count)
        sumsDropped.append(sum)
        if (i in [3,4,7,9]):
            meansDropped.append(float(sum / count))
        elif (i == 1):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 2):
            legalValues = [1,2,3,4]
            modifiedLegalValues = [1,2,3,4]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 5):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 6):
            legalValues = [2,1,0]
            modifiedLegalValues = [2,1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 8):
            legalValues = [1,0]
            modifiedLegalValues = [1,0]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 10):
            legalValues = [1,2,3]
            modifiedLegalValues = [1,2,3]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 11):
            legalValues = [0,1,2,3]
            modifiedLegalValues = [0,1,2,3]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 12):
            legalValues = [3,6,7]
            modifiedLegalValues = [3,6,7]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        elif (i == 13):
            legalValues = [0,1,2,3,4]
            modifiedLegalValues = [0,1,2,3,4]
            modifiedLegalValues[:] = [abs(x - int(sum/count)) for x in modifiedLegalValues]
            meansDropped.append(legalValues[legalValues.index(min(legalValues))])
        else:        
            meansDropped.append(int(sum / count))

    # mengubah data mean
    for i in range(colDropped):
        for j in range(rowDropped):
            if (dataDropped_test.iat[j,i] == '?'):
                dataMeanDropped_test.iat[j,i] = meansDropped[i]
                
    # mengubah data modus
    for i in range(colDropped):
        for j in range(rowDropped):
            if (dataDropped_test.iat[j,i] == '?'):
                dataModeDropped_test.iat[j,i] = modesDropped[i]

    #predict test data
    target = data['Column14']
    from sklearn.naive_bayes import GaussianNB
    dataModeNb = dataMode.drop(columns=['Column14'] , axis=1)
    dataMeanNb = dataMean.drop(columns=['Column14'] , axis=1)

    NB = GaussianNB()
    NBMode = NB.fit(dataModeNb, target)
    NBMean = NB.fit(dataMeanNb, target)
    targetModeNb = NB.predict(dataMode_test)
    targetMeanNb = NB.predict(dataMean_test)

    if (targetModeNb > 0) :
        return render(request, 'diagnose/result2.html')
    else :
        return render(request, 'diagnose/result1.html')
    