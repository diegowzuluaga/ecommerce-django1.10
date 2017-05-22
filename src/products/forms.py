
from django.forms.models import modelformset_factory
from django import forms
from .models import *

class VariationInventoryForm(forms.ModelForm):
	class Meta:
		model = Variation
		fields = (
			"title",
			"price",
			"sale_price",
			"inventory",
			"active",
		)
VariationInventoryFormSet = modelformset_factory(Variation, form = VariationInventoryForm, extra = 0)
