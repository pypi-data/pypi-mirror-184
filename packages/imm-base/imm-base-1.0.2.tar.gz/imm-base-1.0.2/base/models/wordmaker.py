from docxtpl import DocxTemplate


class WordMaker:
    """This class makes word file based on template and filling in the data of context"""

    def __init__(self, template, context, output):
        self.document = DocxTemplate(template)
        self.context = context
        self.output = output

    def make(self):
        self.document.render(self.context)
        self.document.save(self.output)
        return f"{self.output} has been saved..."
