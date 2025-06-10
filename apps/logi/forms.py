from django import forms
from .models import Route


class RouteCreateForm(forms.ModelForm):
    """
    Форма добавления
    """

    class Meta:
        model = Route
        fields = ('title', 'slug', 'category', 'description', 'text', 'thumbnail', 'status')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class RouteUpdateForm(RouteCreateForm):
    class Meta:
        model = Route
        fields = RouteCreateForm.Meta.fields + ('updater', 'fixed')

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы под Bootstrap
        """
        super().__init__(*args, **kwargs)

        self.fields['fixed'].widget.attrs.update({
            'class': 'form-check-input'
        })
