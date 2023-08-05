from django.http import HttpResponse

from .views import AlohaView, AlohaProtectedView, AlohaMarkdownView

def teapot(request):
    return HttpResponse("""
<html>
    <h1>418 I'm a teapot</h1>
    <p>The HTCPCP Server is a teapot. The responding entity MAY be short and stout.</p>
</html>
""", status=418)


__all__ = ['AlohaView', 'AlohaProtectedView', 'AlohaMarkdownView']