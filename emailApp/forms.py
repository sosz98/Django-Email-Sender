from django import forms


class EmailForm(forms.Form):
    receiver_email = forms.EmailField(label="Receiver E-Mail")
    subject = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
