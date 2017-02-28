from django import forms


from course.models.file_upload import Document
from course.models.topic import Topic

class DocumentForm(forms.ModelForm):
    class Meta:
        
        model = Document
        fields = ('topic', 'description', 'document', )
