import re
import markdown

from markdown import Extension
from markdown.preprocessors import Preprocessor


def makeExtension(config=None):
    return TogglerExtension(config)


class TogglerExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        self.heading_processor = TogglerProcessor(md)
        md.preprocessors.add('toggler', self.heading_processor, '>html_block')


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

        toggler_p = r'([ \t]*\|{3}[\s\S]*\|{3}[\s\S]*?[ ]{4}[\S].*(?=\n\n+.*(?!\|)^[\S]))|' \
                    r'([ \t]*\|{3}[\s\S]*\|{3}[\s\S]*?[ ]{4}[\S].*(?=\n\n+.*(?!\|)[\S]))|' \
                    r'([ \t]*\|{3}[\s\S]*\|{3}[\s\S]*?[ ]{4}[\S].*(?=(\n\n+)|($)))'
        togglers = re.compile(toggler_p).findall(content)

        for toggler in togglers:
            temp = ""
            for l in toggler:
                temp += l
            toggler = temp

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

        # Get main tab names
        main_tabs = re.compile(tabs_p).findall(toggler)

        # If no tabs then return empty list
        if not main_tabs:
            return toggler

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

        return "<div class=\"toro-toggler\" data-names=\"{}\">\n\n{}\n\n</div>\n\n".format(data_names, content)

    def getSubDiv(self, tab_name, tab_content):
        tab_content = self.remove_indents(tab_content) + "\n\n"
        nested_togglers = re.compile(r'[ \t]*/{3}[\s\S]*?/{3}[\s\S]*?[ ]{4}.*[\S](?=\n\n)').findall(tab_content)

        if nested_togglers:
            for nested_toggler in nested_togglers:
                nested_html = self.getNestedTogglerDiv(nested_toggler)
                tab_content = tab_content.replace(nested_toggler, nested_html)

        return "\n\n<div data=related-divider=\"{}\">\n\n{}\n\n</div>".format(tab_name, tab_content)

    def getNestedTogglerDiv(self, nestedToggler):
        tabs_p = r'/{3}[ ]+".*"(?=\n)'
        return self.getMainDiv(nestedToggler, tabs_p)

    def remove_indents(self, content):
        content_lines = content.split("\n")

        for line in content_lines:
            if line and line != "\n":
                indent = re.compile(r'^\s*').findall(content)
                if indent:
                    indent = indent[0]
                    indent = indent.replace("\n", "")
                    without_indents = ""

                    for c in content.split("\n"):
                        if c[:len(indent)] == indent:
                            without_indents += c[len(indent):] + "\n"
                        else:
                            without_indents += c + "\n"

                    without_indents = without_indents[:-1]
                    return without_indents

        return content

    def add_indents(self, content, indent):
        with_indent = ""
        for c in content.split("\n"):
            with_indent += indent + c + "\n"

        return with_indent


# md = markdown.Markdown(extensions=["coffee-ninja"])
# text = """
# ||| "Coder Studio"
#     /// "Tab1"
#         tab 1.
#     /// "Tab2"
#         tab 2.
#
#     foo bar.
# ||| "Coder Cloud"
#
#     bar boo.
#
# ||| "What"
#     Hello World
# ||| "How"
#     Foo Bar
#
# """
# print(md.convert(text))