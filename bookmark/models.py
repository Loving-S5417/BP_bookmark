# Django에서 model 클래스 정의는, 곧 데이터베이스 테이블을 생성하는 것이다. 
# 
# Django에서는 "테이블"은 '클래스'로, "테이블의 칼럼"은 '클래스의 변수[속성]'로 매핑한다.
# 이때 테이블 클래스는 django.db.models.Model 클래스를 상속받아 정의하고,
# 각 클래스 변수의 타입도 Django에서 미리 정의된 필드 클래스를 사용한다.
# 
# 칼럼을 정의할 때에는 Django에서 제공하는 다양한 필드 타입을 알아야 한다.
# cf. https://docs.djangoproject.com/en/2.1/ref/models/fields/
from django.db import models
from django.urls import reverse

class Bookmark(models.Model) : 	# DB에 "application명_model명" 방식으로 테이블이 생성된다. >>> "bookmark_bookmark"
	site_name 	= models.CharField('사이트 이름', max_length=100)
	url 		= models.URLField('URL 주소')	

	def __str__(self) : # __str__() : 인스턴스 자체를 출력할 때의 형식을 지정해주는 함수. 자바에서 Obejct 객체의 toString() 메서드와 유사. 즉 객체를 string으로 표현해주는 메서드.
		return "사이트 : [" + self.site_name + "], 주소 : " + self.url

	def get_absolute_url(self) : # get_absolute_url()는 Django에서 사용하는 메서드. 보통 객체의 상세화면 주소를 반환하게 만든다.
		return reverse('bookmark:dtl', args=[str(self.id)])	# reverse() : URL패턴이름과 추가 인자를 전달받아서, URL을 생성하는 메서드.