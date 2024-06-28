from django import forms


class ArrayForm(forms.Form):
    array = forms.CharField(
        label='Enter a sequence of numbers (e.g., 1234)',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '1234'})
    )

    def clean_array(self):
        data = self.cleaned_data['array']
        try:
            data = list(map(int, data))
        except ValueError:
            raise forms.ValidationError('Please enter a valid sequence of numbers.')
        return data
