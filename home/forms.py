# make sure this is at the top if it isn't already
from django import forms


# our new form
class ContactForm(forms.Form):
    fields = ['contact_name', 'contact_email', 'content']
    contact_name = forms.CharField(required=True,  widget=forms.TextInput(attrs={'class': 'form-control'})) 
    contact_email = forms.EmailField(required=True,  widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class': 'form-control special'})
    )
    
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Name:"
        self.fields['contact_email'].label = "Email:"
        self.fields['content'].label = "Message:"
