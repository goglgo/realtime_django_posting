from django.db import models



class ScreenShot(models.Model):
    # upload_to "" >> MEDIA ROOT save
    image = models.ImageField(verbose_name="이미지 파일", upload_to="")
    uploaded_date = models.DateTimeField(auto_now_add=True)
    context = models.TextField(verbose_name='본문')

class Information(models.Model):
    ram_usage = models.CharField(verbose_name="램 사용량", max_length=200)

class Computer(models.Model):
    computer_name = models.CharField(verbose_name="컴퓨터 이름", max_length=50)
    screenshots = models.ManyToManyField(ScreenShot)
    information = models.ForeignKey(Information, on_delete=models.CASCADE)