from django.forms import ModelForm, BooleanField, forms

from main.models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        exclude = ('slug', 'views')

    def clean_name(self):
        name = self.cleaned_data['name']
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']
        for word in words:
            if word in name.lower():
                raise forms.ValidationError(f'Название содержит запрещенное слово: {word}')
        return name

    def clean_description(self):
        description = self.cleaned_data['description']
        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                           'радар']
        for word in words:
            if word in description.lower():
                raise forms.ValidationError(f'Описание содержит запрещенное слово: {word}')
        return description
