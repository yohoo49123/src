from django import forms
from .models import NippoModel

class NippoModelForm(forms.ModelForm):
    class Meta:
        model = NippoModel
        fields = "__all__"

    #フィールド全て
    #fields = "__all__"

    #フィールドの一部
    #fields = ["フィールド1", "フィールド2"]

    #一部のフィールドを除く
    #exclude = "除きたいフィールド"

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)

class NippoFormClass(forms.Form):
    title = forms.CharField(max_length=100, label="タイトル")
    content = forms.CharField(widget=forms.Textarea(), max_length=1000, label="内容")

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs["class"] = "form-control"
        super().__init__(*args, **kwargs)