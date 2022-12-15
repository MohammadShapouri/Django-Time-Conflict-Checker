from django.db import models
# Create your models here.


# WEEK_DAYS_CHOICES = (
# 	('saturday',"شنبه"),
# 	('sunday',"یک شنبه"),
# 	('monday',"دو شنبه"),
# 	('tuesday',"سه شنبه"),
# 	('wednesday',"چهار شنبه"),
# 	('thursday',"پنج شنبه"),
# 	('friday',"جمعه"),
# 	)



class ClassTime(models.Model):
	EVEN_ODD_WEEKS_CHOICES = (
		('even', "زوج"),
		('odd', "فرد"),
		('all', "همه هفته ها"),
		)


	class_name 		= models.CharField(max_length=50, verbose_name="نام درس")
	class_time 		= models.TimeField(verbose_name="ساعت کلاس")
	class_day 		= models.ManyToManyField('WeekDay', verbose_name="روز کلاس", related_name='class_time')
	even_odd_weeks 	= models.CharField(choices=EVEN_ODD_WEEKS_CHOICES, default='all', max_length=4, verbose_name="هفته زوج یا فرد")
	professor_name 	= models.CharField(max_length=50, blank=True, null=True, verbose_name="نام استاد")
	exam_time 		= models.TimeField(blank=True, null=True,verbose_name="ساعت امتحان")
	exam_day 		= models.ForeignKey('WeekDay', blank=True, null=True, on_delete=models.CASCADE, verbose_name='روز امتحان', related_name='exam_time')

	class Meta:
		verbose_name = "برنامه کلاس"
		verbose_name_plural = "برنامه کلاس ها"

	def __str__(self):
		return str(self.class_name)







class WeekDay(models.Model):
	day = models.CharField(max_length=20, verbose_name="روز")

	class Meta:
		verbose_name = "روز هفته"
		verbose_name_plural = "روزهای هفته"

	def __str__(self):
		return str(self.day)
