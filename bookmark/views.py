# from django.shortcuts import render
from django.views.generic.list import ListView								# 클래스형 제네릭 뷰를 사용하기 위해 필요한 클래스를 import (cf. 제네릭 뷰 : RedBook 203~204페이지 참고)
from django.views.generic.detail import DetailView							# 클래스형 제네릭 뷰를 사용하기 위해 필요한 클래스를 import
from django.views.generic.edit import CreateView, UpdateView, DeleteView	# 클래스형 제네릭 뷰를 사용하기 위해 필요한 클래스를 import
from django.urls import reverse_lazy
from .models import Bookmark 						# 동일 디렉토리에 있는 models.py 모듈에서 정의한 Bookmark 클래스를 import. 

### ListView 제네릭 뷰
#   ListView를 상속받는 경우에는 DB객체가 들어있는 리스트를 context변수로 템플릿 시스템에 넘겨주면 된다.
#   만일 이런 리스트를 테이블에 들어있는 모든 레코드를 가져와 구성하는 경우에는, model클래스명[DB테이블명]만 지정해주면 된다.
#   그렇지 않은 경우에는 get_queryset() 메서드를 오버라이딩으로 정의하여 원하는 리스트를 구성해주면 된다.
#   또한 명시적으로 지정하지 않아도 Django가 알아서 지정해주는 속성 2가지가 있다.
#   첫번째는 context변수로 "object_list"를 사용하는 것이고, 두번째는 템플릿 파일을 "모델명소문자_list.html" 형식의 이름으로 지정하는 것이다.
#   물론 context변수명과 템플릿 파일명을 명시적으로 지정할 수도 있다.
class BookmarkListView(ListView) :
	model = Bookmark 	# Bookmark테이블의 특정 레코드를 가져와서, context변수를 구성.
						# 여기서 context변수명은 디폴트 값을 사용하고 있으며, "object"와 모델명소문자인 "bookmark", 둘 다 가능하다.
	##################### 참고로 ListView 사용 시 디폴트 context변수명은 "object_list"와 모델명 소문자를 사용한 "bookmark_list", 둘 다 가능하다.
	#					  (디폴트) 	context변수 	:	"object_list"
	#					  	  		템플릿 파일 	:	"templates/bookmark/bookmark_list.html"
	paginate_by = 3	# 한 페이지에 몇 개씩 출력할 것인지 설정[pagination].

class BookmarkDetailView(DetailView) :
	model = Bookmark 	# Bookmark테이블의 특정 레코드를 가져와서, context변수를 구성.
	##################### 참고로 DetailView 사용 시 디폴트 context변수명은 "object"와 모델명소문자인 "bookmark", 둘 다 가능하다.
	#					  (디폴트) 	context변수 	:	"object"
	#					  	  		템플릿 파일 	:	"templates/bookmark/bookmark_detail.html"

class BookmarkCreateView(CreateView) :
	model = Bookmark 	# Bookmark테이블의 특정 레코드를 가져와서, context변수를 구성.
	fields = ['site_name', 'url']				# fields				: DB테이블[model]에서 어떤 필드들을 입력받을 것인지를 설정.
	success_url = reverse_lazy('bookmark:list')	# success_url			: 글쓰기 완료 후 이동할 페이지 설정. >>> 'URL 패턴이름'이 'list'인, 즉 url주소가 /bookmark/인 페이지로 이동.(bookmark/urls.py 참고)
	template_name_suffix = '_create' 			# template_name_suffix	: 템플릿 파일명의 접미사 설정. >>> 템플릿 파일 	: "templates/bookmark/bookmark_create.html"
												#						  참고로 CreateView와 UpdateView의 경우 디폴트 접미사는 form이어서, 디폴트 템플릿 파일명은 "bookmark_form.html"이다.
				  	  		
class BookmarkUpdateView(UpdateView) :
	model = Bookmark 	# Bookmark테이블의 특정 레코드를 가져와서, context변수를 구성.
	fields = ['site_name', 'url']				# fields				: DB테이블[model]에서 어떤 필드들을 입력받을 것인지를 설정.
#	success_url 대신에 "모델"에서 정의한 get_absolute_url()를 통해, 이동할 페이지 설정.
	template_name_suffix = '_update' 			# template_name_suffix	: 템플릿 파일명의 접미사 설정. >>> 템플릿 파일 	: "templates/bookmark/bookmark_update.html"
												#						  참고로 CreateView와 UpdateView의 경우 디폴트 접미사는 form이어서, 디폴트 템플릿 파일명은 "bookmark_form.html"이다.

class BookmarkDeleteView(DeleteView) :
	model = Bookmark 	# Bookmark테이블의 특정 레코드를 가져와서, context변수를 구성.
	success_url = reverse_lazy('bookmark:list')	# success_url			: 글쓰기 완료 후 이동할 페이지 설정. >>> 'URL 패턴이름'이 'list'인, 즉 url주소가 /bookmark/인 페이지로 이동.(bookmark/urls.py 참고)
