from django import forms
from . import models, kivano_kg, faberlic_com

class ParserProductForm(forms.Form):
    MEDIA_CHOISCES = (
        ('olx.uz', 'olx.uz'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)

    class Meta:
        filds = [
            'media_type',
        ]
    def parser_data(self):
        if self.data['media_type'] == 'olx.uz':
            olx_parser = pars.parser()
            for i in olx_parser:
                models.KivanoProducts.objects.create(**i)

