from django import forms


class BootStrap:
    bootstrap_exclude_fields = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环找到所有的插件,添加了class="form-control"
        for name, field in self.fields.items():
            if name in self.bootstrap_exclude_fields:
                continue
            # 字段中有属性，保留原来的属性，每有属性，才增加
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"]: field.label
            else:
                field.widget.attrs = {"class": "form-control", "placeholder": field.label}


class BootStrapModelForm(BootStrap, forms.ModelForm):

   pass


class BootStrapForm(BootStrap, forms.Form):
    pass

