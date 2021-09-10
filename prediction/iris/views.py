from django.shortcuts import render
import pandas as pd
from .models import PredictResults
from django.http import JsonResponse

def index(request):
    return render(request, 'index.html')

def predict_chances(request):
    if request.POST.get('action') == 'post':
        # Receive data from the user
        sepal_length = float(request.POST.get('sepal_length'))
        sepal_width = float(request.POST.get('sepal_width'))
        petal_length = float(request.POST.get('petal_length'))
        petal_width = float(request.POST.get('petal_width'))
        # Unpickle model
        model = pd.read_pickle(r"C:\Users\admin\Downloads\iris.pickle")
        # Make prediction
        result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
        classification = result[0]
        PredictResults.objects.create(sepal_length=sepal_length, sepal_width=sepal_width, petal_length=petal_length, petal_width=petal_width, classification=classification)
        return JsonResponse({'result': classification,
                                'sepal_length': sepal_length,
                                'sepal_width': sepal_width,
                                'petal_length': petal_length,
                                'petal_width': petal_width},
                            safe=False)

def view_results(request):
    # Submit prediction and show results
    data = { "dataset": PredictResults.objects.all() }
    return render(request, "results.html", data)