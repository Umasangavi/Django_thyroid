from django.shortcuts import render
import numpy as np
import joblib as jb
# Create your views here.

def home(request):
    if request.method=='GET':
        return render(request,'index.html')

def predict(request):
    if request.method=='POST':
        TSH =(request.POST['TSH'])
        FTI =(request.POST['FTI'])
        TT4 =(request.POST['TT4'])
        T3 =(request.POST['T3'])
        query_hypothyroid =(request.POST['query_hypothyroid'])
        on_thyroxine =(request.POST['on_thyroxine'])
        sex =(request.POST['sex'])
        pregnant =(request.POST['pregnant'])
        psych =(request.POST['psych'])
        arr=np.array([[TSH, FTI ,TT4, T3,query_hypothyroid,on_thyroxine,sex,pregnant,psych]])
        model = jb.load(open("thyroid_project\model.pkl", 'rb'))
        result = model.predict(arr)
        
        if result ==1 :
            return render(request,'after.html',{'data' : 'Values shows that patient has Hypothyroidism'})
        else:
            return render(request,'after.html',{'data' : 'Happy to say that your values are Normal'})

