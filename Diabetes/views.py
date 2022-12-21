from django.shortcuts import render
import numpy as np
import pandas as pd
# our home page view
def home(request):    
    return render(request, 'index.html')


# custom method for generating predictions
def getPredictions(age,preg,glu,bp,st,ins,bmi,dpf):
    import pickle
    n1 = pickle.load(open("C:\\Users\\Arshan\\Desktop\\diabetes\\Diabetes\\Diabetes\\Age_Encode.sav", "rb"))
    age=n1.transform(np.array(age).reshape(1,-1))
    n2 = pickle.load(open("C:\\Users\\Arshan\\Desktop\\diabetes\\Diabetes\\Diabetes\\Pregancies_Encode.sav", "rb"))
    preg=n1.transform(np.array(preg).reshape(1,-1))
    n3 = pickle.load(open("C:\\Users\\Arshan\\Desktop\\diabetes\\Diabetes\\Diabetes\\Glucose_Encode.sav", "rb"))
    glu=n3.transform(np.array(glu).reshape(1,-1))
    n4 = pickle.load(open("C:\\Users\\Arshan\\Desktop\\diabetes\\Diabetes\\Diabetes\\BP_Encode.sav", "rb"))
    bp=n4.transform(np.array(bp).reshape(1,-1))
    n5 = pickle.load(open("C:\\Users\\Arshan\\Desktop\\diabetes\\Diabetes\\Diabetes\\ST_Encode.sav", "rb"))
    st=n5.transform(np.array(st).reshape(1,-1))
    n6 = pickle.load(open("C:\\Users\\Arshan\\Desktop\\diabetes\\Diabetes\\Diabetes\\Insulin_Encode.sav", "rb"))
    ins=n6.transform(np.array(ins).reshape(1,-1))
    n7 = pickle.load(open("C:\\Users\\Arshan\\Desktop\\diabetes\\Diabetes\\Diabetes\\BMI_Encode.sav", "rb"))
    bmi=n7.transform(np.array(bmi).reshape(1,-1))
    n8 = pickle.load(open("C:\\Users\\Arshan\\Desktop\\diabetes\\Diabetes\\Diabetes\\DPF_Encode.sav", "rb"))
    dpf=n8.transform(np.array(dpf).reshape(1,-1))
    l1=[age,preg,glu,bp,st,ins,bmi,dpf]
    l1=np.array(l1)
    model=pickle.load(open("C:\\Users\\Arshan\\Desktop\\diabetes\\Diabetes\\Diabetes\\RandFmodel.pkl", "rb"))
    l1=l1.reshape(1,-1)
    prediction=model.predict(l1)
    if prediction == 0:
        return "Not Diabetic"
    elif prediction == 1:
        return "Diabetic"
    else:
        return "error"
        

# our result page view
def result(request):
    age=int(request.GET['age'])
    preg=int(request.GET['preg'])
    glu=int(request.GET['glu'])
    bp=int(request.GET['bp'])
    st=int(request.GET['st'])
    ins=int(request.GET['ins'])
    bmi=float(request.GET['bmi'])
    dpf=float(request.GET['dpf'])
    result = getPredictions(age,preg,glu,bp,st,ins,bmi,dpf)

    return render(request, 'index.html', {'result':result})

