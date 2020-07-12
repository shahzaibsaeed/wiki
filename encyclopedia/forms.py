from django import forms

class NewPageForm(forms.Form):
    title = forms.CharField(label="Entry Title*", required= True, widget=forms.TextInput(attrs={
        'placeholder': 'New Entry Title'
        }))
    content = forms.CharField(label="Main Content*", required= True, widget=forms.Textarea(attrs={
        'placeholder': 'Content as Markdown'
        }))