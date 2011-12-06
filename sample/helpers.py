from django import forms

# Form helpers
# -------------------------------------
#

class ServerToServerForm(forms.Form):
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

class TransparentRedirectForm(forms.Form):
    card_number = forms.CharField()
    cvv = forms.CharField()


# Error parser
# -------------------------------------
# 
# * Samurai returns both dictionaries as well as
# * simple strings in error list. This helper parses
# * the error list returned by samurai python client
# * and prepares a list of only error messagesi
#
def parse_error(errors):
    error_list = []
    for err in errors:
        if isinstance(err, dict) and  err.get('key'):
            error_list.append(err.get('key'))
        else:
            error_list.append(err)
    return error_list



