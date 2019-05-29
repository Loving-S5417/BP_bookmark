from django.contrib import admin
from .models import Bookmark 	# 동일 디렉토리에 있는 models.py 모듈에서 정의한 Bookmark 클래스를 import. 

### models.py에서 정의한 테이블들이 Admin사이트에 보이도록 등록 ###
admin.site.register(Bookmark)