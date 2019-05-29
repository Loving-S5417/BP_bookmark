from django.urls import path
from .views import BookmarkListView, BookmarkCreateView, BookmarkDetailView, BookmarkUpdateView, BookmarkDeleteView	# 동일 디렉터리 안에 views.py에서 정의한 클래스들을 import.

app_name = 'bookmark'	# app_name 변수는 URL 패턴의 이름이 충돌나는 것을 방지하기 위한 name space 역할을 한다. ( reverse()나 {% url %} 탬플릿 태그에서 자주 사용된다. )
						# 예컨대 애플리케이션 aaa의 URL 패턴이름과 애플리케이션 bbb의 URL 패턴이름이 모두 detail일 경우, 각각 aaa:detail, bbb:detail로 표기해서 구분할 수 있다.
 
urlpatterns = [
	path('', 					BookmarkListView.as_view(), 	name='list'),	# ex) /bookmark/
	path('add/', 				BookmarkCreateView.as_view(), 	name='add'), 	# ex) /bookmark/add/
	path('detail/<int:pk>/', 	BookmarkDetailView.as_view(), 	name='dtl'), 	# ex) /bookmark/detail/99/
	path('update/<int:pk>/', 	BookmarkUpdateView.as_view(), 	name='mod'), 	# ex) /bookmark/update/99/
	path('delete/<int:pk>/', 	BookmarkDeleteView.as_view(), 	name='del'), 	# ex) /bookmark/delete/99/
]
###### <int:pk>
#		int : 컨버터.
#			  컨버터 종류 : 	1. str	: 컨버터를 설정하지 않을 경우 적용되는 기본 컨버터로서, 비어있지 않은 모든 문자와 매칭. (단 '/'는 제외.)
#			  				2. int	: 0을 포함한 양의 정수와 매칭.
#			  				3. slug	: ASCII 문자, 숫자, 하이픈, 언더스코어를 포함한 슬러그 문자열과 매칭.
#			  				4. uuid	: UUID와 매칭. (같은 페이지에 여러 URL이 연결되는 것을 막기 위해 사용.)
#			  				5. path	: 기본적으로 str와 같은 기능을 하나, '/'도 포함. (URL의 부분이 아닌 전체에 대한 매칭을 하고 싶을 때 사용.)
#		pk	: 컨버터를 통해 반환받은 값 OR 패턴에 일치하는 값의 변수명.

# 1. ######################################################################################################################
# as_view()  : 	클래스형 뷰는 클래스로 진입하기 위한 as_view() 클래스 매서드를 제공한다.
# 				이 메서드를 "진입 메서드"라고 부르기도 하는데,
# 				그 역할은 클래스의 인스턴스를 생성하고, 그 인스턴스의 dispatch() 메서드를 호출한다.
# dispatch() :	요청을 검사해서 GET, POST 등의 어떤 HTTP 메서드로 요청되었는지를 알아낸 다음,
#				인스턴스 내에서 해당 이름을 갖는 메서드로 요청을 중계해준다.
#				만일 해당 메서드가 정의되어 있지 않으면 HttpResponseNotAllowed 예외처리를 발생시킨다.
#				
#	cf.	클래스형 View 코딩 시
#		[각 애플리케이션 폴더 안에 있는 "views.py" 코딩 시]
#		
#		"	from django.views.generic import View 	"
#		
#		와 같은 방식으로 필요한 제네릭 뷰를 상속하면서 시작하게 되는데,
#		Django가 기본적으로 제공하는 제네릭 뷰에는
#		as_view() 메서드와 dispatch() 메서드가 정의되어 있기 때문에,
#		개발자가 별도로 정의하지 않아도 as_view()와 dispatch()를 사용할 수 있다.
#		
#		
#		
# 2. ######################################################################################################################
# URL/View 매핑을 정의하는 방식은 항상 동일한데, URL패턴 매칭은 위에서 아래로 진행하므로, 정의하는 순서에 유의해야 한다.
# 위에서는 bookmark 애플리케이션에 대한 URL/View 매핑을 정의하고 있다.
# path()는 route, view 2개의 필수인자와, kwarges, name 2개의 선택인자를 받는다.
# 		route 	: URL 주소.
# 				  URL 패턴을 표현하는 문자열[URL 스트링].
# 				  참고로 DetailView 제네릭 뷰를 이용하여 DB테이블에서 특정 레코드를 조회하는 경우 Primary Key로 검색하는데,
# 				  이때 Primary Key는 "pk"라는 변수에 담겨 제네릭 뷰로 전달되고, 이에 대한 처리는 DetailView 제네릭 뷰가 알아서 처리해 준다.
# 		view  	: route에 해당하는 URL 주소로 접근했을 때 호출할 view함수.
# 				  URL 스트링이 매칭되면 호출되는 (애플리케이션[books] 디렉토리 안에 있는 views.py파일에 정의된) view함수.
#				  HttpRequest 객체와 URL 스트링에서 추출된 항목이 이 view함수의 인자로 전달된다.
# 		kwarges	: view함수에 전달할 값들.
# 				  URL 스트링에서 추출된 항목 외에 추가적인 인자를 view함수에 전달할 때, 딕셔너리 형식으로 인자를 정의한다. (우리 예제에는 사용안함.)
# 		name    : route의 이름.
# 				  각 URL 패턴에 이름을 지정한다. 해당 이름은 Template 파일에서 많이 사용한다.
#		
#		
#		
# 3. URL-뷰-템플릿 매핑 ####################################################################################################
# <URL패턴>				<뷰 클래스명>		<템플릿 파일명>														<템플릿 설명>
# /bookmark/			BookmarkListView	프로젝트디렉토리/bookmark/templates/bookmark/bookmark_list.html		
# /bookmark/add/		BookmarkCreateView 	프로젝트디렉토리/bookmark/templates/bookmark/bookmark_create.html		