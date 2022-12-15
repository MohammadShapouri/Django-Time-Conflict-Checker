from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView, View
from django.urls import reverse_lazy
from .models import ClassTime
from .forms import ClassTimeForm
from django.shortcuts import redirect
# Create your views here.




# class CreateClassTime(View):

# 	form_instance_num = 3

# 	def get(self, request):
# 		forms = list()
# 		for i in range(self.form_instance_num):
# 			forms.append(ClassTimeForm(prefix=i))
# 		context = {
# 			'forms' : forms
# 		}
# 		return render(request, 'schedule/create-class-time.html', context)


# 	def post(self, request):
# 		have_error = False
# 		ready_for_saving = False
# 		forms = list()
# 		validated_forms = list()

# 		for i in range(self.form_instance_num):
# 			forms.append(ClassTimeForm(request.POST, prefix=i))

# 		for form in forms:
# 			if form.is_valid():
# 				# form.cleaned_data.get('class_day') returns a queryset list; so, django orm methods can be used for it like form.cleaned_data.get('class_day').count()
# 				if form.cleaned_data.get('class_name') and form.cleaned_data.get('class_time') and form.cleaned_data.get('class_day').count() > 0:
# 					validated_forms.append(form)
# 					ready_for_saving = True
# 				elif form.cleaned_data.get('class_name') == None and form.cleaned_data.get('class_time') == None and form.cleaned_data.get('class_day').count() == 0:
# 					pass
# 				else:
# 					if form.cleaned_data.get('class_name') == None:
# 						have_error = True
# 						form.add_error('class_name', "نام کلاس الزامیست.")
# 					if form.cleaned_data.get('class_time') == None:
# 						have_error = True
# 						form.add_error('class_time', "ساعت کلاس الزامیست.")
# 					if form.cleaned_data.get('class_day').count() == 0:
# 						have_error = True
# 						form.add_error('class_day', "روز(های) کلاس الزامیست.")

# 		if have_error == False and ready_for_saving:
# 			# ClassTime.objects.bulk_create([
# 			# 		ClassTime(class_name=form.cleaned_data.get('class_name'),
# 			# 				class_time=form.cleaned_data.get('class_time'),
# 			# 				class_day=form.cleaned_data.get('class_day'),
# 			# 				even_odd_weeks=form.cleaned_data.get('even_odd_weeks'),
# 			# 				professor_name=form.cleaned_data.get('professor_name'),
# 			# 				) for form in validated_forms
# 			# 	])
# 			[form.save() for form in validated_forms]
# 			reverse_lazy('')

# 		context = {
# 			'forms' : forms
# 		}
# 		return render(request, 'schedule/create-class-time.html', context)







# class CreateClassTime(View):
# 	def get(self, request):
# 		classTimeForm = ClassTimeForm(prefix='classTimeForm')
# 		examTimeForm = ExamTimeForm(prefix='examTimeForm')

# 		context = {
# 			'classTimeForm': classTimeForm,
# 			'examTimeForm': examTimeForm,
# 		}
# 		return render(request, 'schedule/create-class-time.html', context)


# 	def post(self, request):
# 		classTimeForm = ClassTimeForm(request.POST, prefix='classTimeForm')
# 		examTimeForm = ExamTimeForm(request.POST, prefix='examTimeForm')
# 		if classTimeForm.is_valid() and examTimeForm.is_valid():
# 			examTime = examTimeForm.save()
# 			classTimeForm.instance.exam_time = examTime
# 			classTimeForm.save()
# 			return redirect('CreateClassTime')


# 		context = {
# 			'classTimeForm': classTimeForm,
# 			'examTimeForm': examTimeForm,
# 		}

# 		return render(request, 'schedule/create-class-time.html', context)









class CreateClassTime(CreateView):
	model = ClassTime
	form_class = ClassTimeForm
	template_name = 'schedule/create-class-time.html'
	success_url = reverse_lazy('CreateClassTime')





class UpdateClassTime(UpdateView):
	model = ClassTime
	form_class = ClassTimeForm
	template_name = 'schedule/create-class-time.html'
	success_url = reverse_lazy('ClassTimeList')


	def get_object(self):
		pk = self.kwargs.get('pk')
		return get_object_or_404(ClassTime, pk=pk)



class ClassTimeList(ListView):
	model = ClassTime
	template_name = 'schedule/class-time-list.html'

	def get_queryset(self):
		return ClassTime.objects.all()

