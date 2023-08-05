import re
import markdown

from markdown import Extension
from markdown.preprocessors import Preprocessor


def makeExtension(config=None):
    return TogglerExtension(config)


class TogglerExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        self.heading_processor = TogglerProcessor(md)
        md.preprocessors.add('togglers', self.heading_processor, '>html_block')


class TogglerProcessor(Preprocessor):

    def __init__(self, md):
        Preprocessor.__init__(self, md)

    def run(self, lines):
        content = ""
        lineLen = len(lines)
        count = 0

        for line in lines:
            content += line
            if count < lineLen - 1:
                content += "\n"
            count += 1

        # Get togglers from document
        toggler_p = r'[ \t]*\|{3}[\s\S]*?\|{3}(?=\n)'
        togglers = re.compile(toggler_p).findall(content)

        for toggler in togglers:
            indent = re.compile(r'^\s*').findall(toggler)
            without_indents = self.remove_indents(toggler)

            tabs_p = r'(\|{3}[ ]*".*"(?=\n))'
            without_indents = self.getMainDiv(without_indents, tabs_p)

            indent = indent[0]
            if indent:
                with_indents = self.add_indents(without_indents, indent)
                content = content.replace(toggler, with_indents)
            else:
                content = content.replace(toggler, without_indents)

        new_lines = []
        for line in content.split("\n"):
            new_lines.append(line)

        return new_lines

    def getMainDiv(self, toggler, tabs_p):
        """
        Get the HTML syntax from the toggler markdown.
        :param toggler: The toggler markdown
        :param tabs_p: Regex to get the tab names.
        :return:
            string: The HTML syntax from the toggler markdown.
        """

        # Get main tab names
        main_tabs = re.compile(tabs_p).findall(toggler)

        # If no tabs then return empty list
        if not main_tabs:
            return toggler

        toggler = toggler[:len(toggler)-3]

        number_of_tabs = len(main_tabs)
        data_names = ""
        tab_contents = []

        i = 0
        for tab in main_tabs:
            # Extract tab name
            t = re.search(r'"(.*?)"', tab).group(1)

            data_names += t + ","
            start_index = toggler.index(tab) + len(tab) + 1

            if i < number_of_tabs - 1:
                last_index = toggler.index(main_tabs[i + 1])
            else:
                last_index = len(toggler)

            # Tab contents
            tab_content = toggler[start_index:last_index]
            tab_contents.append(tab_content)
            i += 1

        data_names = data_names[:-1]
        tab_names = data_names.split(",")
        content = ""

        for i in range(len(tab_names)):
            content += self.getSubDiv(tab_names[i], tab_contents[i])

        return "<div class=\"toro-toggler\" data-names=\"{}\">\n\n{}\n\n</div>\n".format(data_names, content)

    def getSubDiv(self, tab_name, tab_content):
        """
        Get tab's HTML syntax from the tab markdown.
        :param tab_name: Name of the tab.
        :param tab_content: Contents fo the tab.
        :return:
            string: The HTML syntax from the tab's markdown.
        """

        tab_content = self.remove_indents(tab_content) + "\n"
        nested_togglers = re.compile(r'[ \t]*/{3}[\s\S]*?/{3}(?=\n)').findall(tab_content)

        # If contains nested togglers
        if nested_togglers:
            for nested_toggler in nested_togglers:
                nested_html = self.getNestedTogglerDiv(nested_toggler)
                tab_content = tab_content.replace(nested_toggler, nested_html)

        return "\n\n<div data=related-divider=\"{}\">\n\n{}\n\n</div>".format(tab_name, tab_content)

    def getNestedTogglerDiv(self, nestedToggler):
        """
        Get nested toggler's HTML syntax from the nested toggler markdown.
        :param nestedToggler: Nested toggler markdown.
        :return:
            string: The HTML syntax from nested toggler's markfown.
        """

        tabs_p = r'(/{3}[ ]*".*"(?=\n))'
        return self.getMainDiv(nestedToggler, tabs_p)

    def remove_indents(self, content):
        """
        Removes indentations in content.
        :param content: Then content to be removed with indentations.
        :return:
            string: Content with removed indentations.
        """

        indent = re.compile(r'^\s*').findall(content)
        if indent:
            indent = indent[0]
            without_indents = ""

            for c in content.split("\n"):
                if c[:len(indent)] == indent:
                    without_indents += c[len(indent):] + "\n"
                else:
                    without_indents += c + "\n"

            without_indents = without_indents[:-1]
            return without_indents
        else:
            return content

    def add_indents(self, content, indent):
        """
        Append indentations to content.
        :param content: The content to be appended with an indent.
        :param indent: The indentation.
        :return:
            string: Content appended with indentation.
        """

        with_indent = ""
        for c in content.split("\n"):
            with_indent += indent + c + "\n"

        return with_indent


# md = markdown.Markdown(extensions=["toro-mkdocs-togglers"])
# text = """
# ||| "Coder Studio"
#     foo
#
#     bar
#
# ||| "Coder Cloud"
#     /// "Tab1"
#         tab1
#     /// "Tab2"
#         tab2
#     ///
# |||
# """
# print(md.convert(text))