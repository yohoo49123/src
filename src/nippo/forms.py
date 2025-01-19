from django import forms
from .models import NippoModel
from bootstrap_datepicker_plus.widgets import DatePickerInput

    #フィールド全て
    #fields = "__all__"

    #フィールドの一部
    #fields = ["フィールド1", "フィールド2"]

    #一部のフィールドを除く
    #exclude = "除きたいフィールド"

class NippoModelForm(forms.ModelForm):
    date = forms.DateField(
        label="作成日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )
    class Meta:
        model = NippoModel
        exclude = ["user"]

    def __init__(self, user=None, *args, **kwargs):
        for key, field in self.base_fields.items():
            if key != "public":
                field.widget.attrs["class"] = "form-control"
            else:
                field.widget.attrs["class"] = "form-check-input"

        self.user = user
        super().__init__(*args, **kwargs)
        
    def save(self, commit=True):
        nippo_obj = super().save(commit=False)
        if self.user:
            nippo_obj.user = self.user
        if commit:
            nippo_obj.save()
        return nippo_obj



class NippoFormClass(forms.Form):
    title = forms.CharField(max_length=100, label="タイトル")
    content = forms.CharField(widget=forms.Textarea(), max_length=1000, label="内容")

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)