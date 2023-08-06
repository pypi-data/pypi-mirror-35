import argparse
import markdown

from mdx_link2md.markdownlinks import MarkdownLinkExtension


def main():
    """
    A utility script that converts markdown files to HTML files, with the internal links
    to local markdown files changed to corresponding HTML files with the same names.
    """

    md = markdown.Markdown(output_format='html5',
                           extensions=[MarkdownLinkExtension(ignore_url=True)])
    parser = argparse.ArgumentParser(
        description='Convert .md files to HTML with the converted files saved at the '
                    'same location as the original markdown files with html extension.')
    parser.add_argument(dest='target_files', nargs='+', help='files to be processed')

    args = parser.parse_args()

    for md_file in args.target_files:
        try:
            idx = md_file.lower().rindex('.md')
        except ValueError:
            continue

        output_file_name = md_file[:idx] + '.html'
        md.convertFile(md_file, output=output_file_name, encoding='utf-8')

        md.reset()


if __name__ == '__main__':
    main()
