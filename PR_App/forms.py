from django import forms
from django.forms import inlineformset_factory
from .models import PR_Document, PR_Document_Detail

class PRDocumentForm(forms.ModelForm):
    class Meta:
        model = PR_Document
        fields = ['nomor_pr', 'created_by']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Tambahkan class CSS ke field nomor_pr
        self.fields['nomor_pr'].widget.attrs.update({
            'class': 'form-control',  # Class Bootstrap untuk input
            'placeholder': 'Enter PR Number',  # Placeholder opsional
        })
        
        self.fields['created_by'].widget.attrs.update({
            'class': 'form-control',
            'disabled': True,  # Membuat field read-only
        })

class PRDocumentDetailForm(forms.ModelForm):
    class Meta:
        model = PR_Document_Detail
        fields = ['line_number', 'part_number', 'qty', 'usage', 'due']

# Membuat formset untuk PR_Document_Detail
PRDocumentDetailFormSet = inlineformset_factory(
    PR_Document,  # Model induk
    PR_Document_Detail,  # Model anak
    form=PRDocumentDetailForm,  # Form untuk model anak
    extra=5,  # Jumlah form kosong yang ditampilkan
    can_delete=True,  # Memungkinkan penghapusan detail
)