from mezzanine.blog.models import BlogPost
from ijctheme.models import  HomePage
from mezzanine.pages.page_processors import processor_for

@processor_for(HomePage)
def blog_list(request, Page):
    bp = BlogPost.objects.published()[:5]
    return {'bp': bp}