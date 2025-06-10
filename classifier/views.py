from django.shortcuts import render
from .forms import NewsForm
import pickle
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'classifier', 'classifier_model.pkl')

with open(MODEL_PATH, 'rb') as f:
    vectorizer, model = pickle.load(f)

def home(request):
    prediction = None
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news_text = form.cleaned_data['news_text']
            transformed_text = vectorizer.transform([news_text])
    
            prediction_result = model.predict(transformed_text)
            prediction_proba = model.predict_proba(transformed_text)
    
            prediction = prediction_result[0]
            proba_0 = prediction_proba[0][0]  
            proba_1 = prediction_proba[0][1]  
    
            print("Prediction:", prediction)
            print("Probability 0:", proba_0)
            print("Probability 1:", proba_1)

    else:
        form = NewsForm()

    return render(request, 'classifier/index.html', {'form': form, 'prediction': prediction})
