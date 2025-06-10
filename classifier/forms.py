from django import forms

class NewsForm(forms.Form):
    news_text = forms.CharField(
        label='Enter News Text',
        widget=forms.Textarea(attrs={
            'placeholder': 'Paste news content here...',
            'rows': 5,
            'cols': 40
        })
    )
