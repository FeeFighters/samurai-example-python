from django import forms

class OrderForm(forms.Form):
    YEARS = (('2011','2011'),('2012','2012'))
    MONTHS = (('1','1'),('2','2'),('3','3'))
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zipcode = forms.CharField()
    card_number = forms.CharField()
    cvv = forms.CharField()
    expiry_month = forms.ChoiceField(choices=MONTHS)
    expiry_year = forms.ChoiceField(choices=YEARS)

class ServerToServerForm(forms.Form):
    card_number = forms.CharField()
    cvv = forms.CharField()

