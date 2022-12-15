from django import forms
from .models import ClassTime, WeekDay



class ClassTimeForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		# self.fields['class_name'].required = False
		# self.fields['class_time'].required = False
		self.fields['class_time'].widget = forms.TimeInput(attrs= {'class': 'time_class'})
		self.fields['exam_time'].widget = forms.TimeInput(attrs= {'class': 'time_class'})
		self.fields['class_time'].widget 


	class_day = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple, queryset=WeekDay.objects.all(), label="روز کلاس")

	class Meta:
		model = ClassTime
		fields = ['class_name', 'class_time', 'class_day', 'even_odd_weeks', 'professor_name', 'exam_time', 'exam_day']


