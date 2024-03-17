from django.db import models

# Create your models here.

class Info(models.Model): # models의 Model 클래스를 상속받는다
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=False) # 빈 값 안된다.
    intro = models.TextField()
    regdate = models.DateTimeField(auto_now_add=True) # 자동으로 현재시간 추가해서 진행
    
    def __str__(self):
        return f'Info[id={self.id}, name={self.name}, age={self.age}, ...]'
