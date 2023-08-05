import os
import logging
import markdown

logger = logging.getLogger(__name__)
markdown.logger.setLevel(logging.INFO)


class MarkdownFile:
    """
    Representation of a Markdown file parsed by the
    MarkdownFileReader class
    """

    EXTENSION = '.md'

    def __init__(self, path: str, html=None, metadata=None):
        """
        Initialise un fichier Markdown
        :param path:        Chemin absolu du fichier
        :param html:        Contenu au format HTML du fichier
        :param metadata:    Métadonnées du fichier
        """
        self.path = path
        self.html = html or ""
        self.metadata = metadata or {}

    def get_metadata(self, key: str, default=None, is_list=False):
        """
        Retourne une valeur de métadonnées
        :param key:
        :param default:
        :param is_list:
        :return:
        """

        if not key in self.metadata:
            return default

        if not is_list:
            return self.metadata[key][0]
        else:
            return self.metadata[key]


class MarkdownFileReader:
    """
    Markdown reader
    Classe permettant de lire un fichier Markdown passé en entrée

    Métadonnées acceptées :
        title: contient le titre du document, on utilise le titre par défaut sinon
    """

    extensions = [
        'markdown.extensions.meta',
        'markdown.extensions.nl2br',
        'markdown.extensions.tables',
    ]

    def __init__(self, path):

        if not path.endswith(MarkdownFile.EXTENSION):
            path += MarkdownFile.EXTENSION

        if not os.path.isfile(path):
            logger.error("MarkdownFileReader: le fichier n'existe pas: {}".format(path))
            raise FileNotFoundError(path)

        self.path = path
        self._file = None
        self._parser = markdown.Markdown(extensions=self.extensions)

    def get(self):
        """
        Retourne le fichier Markdown lu
        :return:
        """

        if self._file:
            return self._file

        logger.debug("Lecture du fichier Markdown: {}".format(self.path))

        # Lecture du fichier et stockage du contenu
        with open(self.path, encoding='utf-8') as f:
            text = f.read()

        html = self._parser.convert(text)
        metadata = self._get_metadata()

        self._file = MarkdownFile(self.path, html, metadata)
        return self._file

    def _get_metadata(self):
        """
        Récupère les métadonnées du fichier parsé
        :return:
        """

        try:
            return self._parser.Meta
        except AttributeError:
            return {}
