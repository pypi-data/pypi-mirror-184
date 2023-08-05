"""
Short summary

Basic module to do things.
"""


class Converter():
    """ A simple converter for converting PDFs to text. """

    def convert(self, path):
        """
        Convert the given pdf to text

        Parameters:
        path(str): The path to a PDF file

        Returns:
        str: The content of the PDF file as text
        """
        print('pdf2text', path)
