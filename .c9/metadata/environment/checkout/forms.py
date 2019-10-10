{"filter":false,"title":"forms.py","tooltip":"/checkout/forms.py","undoManager":{"mark":1,"position":1,"stack":[[{"start":{"row":0,"column":0},"end":{"row":25,"column":0},"action":"insert","lines":["from django import forms","from .models import Order","","","class MakePaymentForm(forms.Form):","","    MONTH_CHOICES = [(i, i) for i in range(1, 12)]","    YEAR_CHOICES = [(i, i) for i in range(2019, 2036)]","","    credit_card_number = forms.CharField(label='Credit card number', required=False)","    cvv = forms.CharField(label='Security code (CVV)', required=False)","    expiry_month = forms.ChoiceField(label='Month', choices=MONTH_CHOICES, required=False)","    expiry_year = forms.ChoiceField(label='Year', choices=YEAR_CHOICES, required=False)","    stripe_id = forms.CharField(widget=forms.HiddenInput)","","","class OrderForm(forms.ModelForm):","","    class Meta:","        model = Order","        fields = (","            'full_name', 'phone_number', 'country', 'postcode',","            'town_or_city', 'street_address1', 'street_address2',","            'county'","        )",""],"id":1}],[{"start":{"row":21,"column":8},"end":{"row":21,"column":12},"action":"remove","lines":["    "],"id":2}]]},"ace":{"folds":[],"scrolltop":73,"scrollleft":0,"selection":{"start":{"row":25,"column":0},"end":{"row":25,"column":0},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":3,"state":"start","mode":"ace/mode/python"}},"timestamp":1570479388736,"hash":"f4877798a11bd28f03422218cae8310af1157b9d"}