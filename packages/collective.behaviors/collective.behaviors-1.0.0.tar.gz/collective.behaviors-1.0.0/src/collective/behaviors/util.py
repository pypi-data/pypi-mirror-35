from plone.formwidget.namedfile.converter import b64decode_file
from plone.namedfile.file import NamedImage


def convert_datagrid_iamge(picture):
    filename, data = b64decode_file(picture)
    data = NamedImage(data=data, filename=filename)
    return data
