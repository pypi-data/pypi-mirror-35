from libaloha.markdown import MarkdownFileReader
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

import os
import logging

logger = logging.getLogger(__name__)


class AlohaView(TemplateView):
    title = ''

    def get_context_data(self, **kwargs):
        """
        Récupère le contexte et ajoute une clé {{ view_title }}
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['view_title'] = self.title
        return context

    def redirect_to_error(self, message=None):
        self.template_name = 'error-page.html'
        return self.render_to_response({'message': message})

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Exception as e:
            logger.error("AlohaView.dispatch: {} {}".format(e.__class__.__name__, str(e)))
            message = None
            if settings.DEBUG:
                message = str(e)
            return self.redirect_to_error(message)


@method_decorator(login_required, name='dispatch')
class AlohaProtectedView(AlohaView):
    pass


class AlohaMarkdownView(AlohaView):
    markdown_file = None
    template_name = 'markdown-view.html'

    def get_markdown_file(self, filename):

        if not filename.endswith('.md'):
            filename += '.md'
        filename = os.path.join(settings.STATIC_MARKDOWN_FOLDER, filename)
        if not os.path.isfile(filename):
            raise FileNotFoundError(filename)

        md = MarkdownFileReader(filename).get()
        return md

    def get(self, request, *args, **kwargs):

        logger.debug("Get markdown view: {}".format(self.markdown_file))

        if not self.markdown_file:
            raise AttributeError("MarkdownView.markdown_file doit être défini")

        self.markdown_file = os.path.join(settings.STATIC_MARKDOWN_FOLDER, self.markdown_file)
        md = self.get_markdown_file(self.markdown_file)

        context = super().get_context_data()
        context['view_title'] = md.get_metadata('title', self.title)
        context['content'] = md.html

        return self.render_to_response(context)