from django import forms
from django.forms import inlineformset_factory
from .models import PR_Document, PR_Document_Detail

class PRDocumentForm(forms.ModelForm):
    class Meta:
        model = PR_Document
        fields = ['nomor_pr', 'acknowledged_by', 'approved_by', 'director_apprv_by', 'received_by']

class PRDocumentDetailForm(forms.ModelForm):
    class Meta:
        model = PR_Document_Detail
        fields = ['line_number', 'part_number', 'qty', 'usage', 'due']

# Membuat formset untuk PR_Document_Detail
PRDocumentDetailFormSet = inlineformset_factory(
    PR_Document,  # Model induk
    PR_Document_Detail,  # Model anak
    form=PRDocumentDetailForm,  # Form untuk model anak
    extra=1,  # Jumlah form kosong yang ditampilkan
    can_delete=True,  # Memungkinkan penghapusan detail
)