from django import forms
from DocumentUpload.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('file_name', 'description', 'document',)
