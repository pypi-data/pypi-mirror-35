''' docserve.py

A tool for quick and easy Markdown project documentation.

'''

import os
import re
import sys
import csv
import glob
import time
import signal
import shutil
import urllib
import base64
import hashlib
import argparse
import tempfile
import datetime
import threading
import traceback
import subprocess
import collections
from urllib.parse import urlparse

import timeago
import xml.etree.ElementTree as ET
from flask import Flask, url_for, abort, send_from_directory, \
    render_template, Markup, make_response

import markdown
import markdown.util
from markdown.extensions import Extension
from markdown.inlinepatterns import LinkPattern, IMAGE_LINK_RE, dequote, handleAttributes
from markdown.blockprocessors import HashHeaderProcessor


class MultiPurposeLinkPattern(LinkPattern):
    ''' Embed image, video, youtube, csv or file download links
    by extending the typical image tag pattern.

    # ![alttxt](http://x.com/) or ![alttxt](<http://x.com/>)

    If the link has "DOWNLOAD" in the alt text, treat it as a download.
    Otherwise, see if its a YouTube video.  Otherwise, see if its a
    csv that can be turned into a table, otherwise if the link cannot be parsed
    as a video, it will always be treated as an image.
    '''
    SUPPORTED_VIDEO = ('ogv', 'ogg', 'avi', 'mp4', 'webm', )
    SUPPORTED_TABLES = ('csv', )

    def get_src(self, m):
        ''' Get the source and parts from the matched groups: src, parts '''
        src_parts = m.group(9).split()
        if src_parts:
            src = src_parts[0]
            if src[0] == "<" and src[-1] == ">":
                src = src[1:-1]
            return self.sanitize_url(self.unescape(src)), src_parts
        else:
            return '', src_parts

    def youtube_url_validation(self, url):
        ''' Given a YouTube URL, return the ID component.
        https://stackoverflow.com/questions/4705996
        '''
        youtube_regex = (r'(https?://)?(www\.)?'
                         '(youtube|youtu|youtube-nocookie)\.(com|be)/'
                         '(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})')
        youtube_regex_match = re.match(youtube_regex, url)
        return youtube_regex_match.group(6) if youtube_regex_match else None

    def as_youtube(self, m, video_id):
        ''' Return a DOM element that embeds a YouTube video. '''
        el = ET.Element('iframe')
        el.set('class', 'video')
        el.set('src', f'https://www.youtube.com/embed/{video_id}?rel=0')
        el.set('frameborder', '0')
        el.set('allow', 'autoplay; encrypted-media')
        el.set('allowfullscreen', '1')
        return el

    def as_video(self, m):
        ''' Return a video element '''
        src, parts = self.get_src(m)
        el = ET.Element('video')
        el.set('src', src)
        el.set("controls", "true")
        handleAttributes(m.group(2), el)
        return el

    def as_image(self, m):
        ''' Return an image element '''
        el = ET.Element('img')
        src, parts = self.get_src(m)
        el.set('src', src)

        # Set the title if present.
        if len(parts) > 1:
            el.set('title', dequote(self.unescape(" ".join(parts[1:]))))

        # Set the attributes on the element, if enabled.
        # Set the 'alt' attribute with whatever is left from `handleAttributes`.
        attrs = self.markdown.enable_attributes
        alt_text = handleAttributes(m.group(2), el) if attrs else m.group(2)
        el.set('alt', self.unescape(alt_text))
        return el

    def as_csv(self, m):
        src, parts = self.get_src(m)
        root = ET.Element('table')
        root.set('class', 'csv-table table thead-light table-hover')
        file_path = os.path.join(self.markdown.page_root, src)
        with open(file_path) as f:
            reader = csv.reader(f)
            headers = next(reader)
            rows = [r for r in reader]
            thead = ET.SubElement(root, 'thead')
            for col in headers:
                ET.SubElement(thead, 'th').text = col
            for row in rows:
                tr = ET.SubElement(root, 'tr')
                for col in row:
                    ET.SubElement(tr, 'td').text = col
        return root

    def as_download(self, m):
        ''' Create card layers used to make a download button. '''
        src, parts = self.get_src(m)

        # Returns a human readable string reprentation of bytes
        def _human_size(bytes, units=[' bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB']):
            return str(bytes) + units[0] if bytes < 1024 else _human_size(bytes >> 10, units[1:])

        # Get information required for card.
        split_src = os.path.split(src)
        file_path = os.path.join(self.markdown.page_root, *split_src)
        file_size = os.path.getsize(file_path)
        file_basename = os.path.basename(file_path)
        card_text = dequote(self.unescape(" ".join(parts[1:]))) if len(parts) > 1 else ''

        # If its a pptx, extract the thumbnail previews.
        # NOTE: This works, but is is removed until we support other
        # file types, which for now is not a priority.
        # preview_uri = None
        # import zipfile
        # if (file_path.endswith('pptx')):
        #     with zipfile.ZipFile(file_path) as zipper:
        #         with zipper.open('docProps/thumbnail.jpeg', 'r') as fp:
        #             mime = 'image/jpeg'
        #             data64 = base64.b64encode(fp.read()).decode('utf-8')
        #             preview_uri = u'data:%s;base64,%s' % (mime, data64)

        # Card and structure.
        card = ET.Element("div")
        card.set('class', 'card download-card')
        header = ET.SubElement(card, 'div')
        header.set('class', 'download-card-header')
        body = ET.SubElement(card, 'div')
        body.set('class', 'download-card-body')

        # Add preview image.
        # if preview_uri:
        #     img = ET.SubElement(header, 'img')
        #     img.set('src', preview_uri)

        # Filename link heading.
        heading = ET.SubElement(body, 'a')
        heading.set('class', 'download-card-title')
        heading.set('href', src)
        download_icon = ET.SubElement(heading, 'i')
        download_icon.set('class', 'fa fa-download')
        download_text = ET.SubElement(heading, 'span')
        download_text.text = file_basename

        # Title element from the "quote marks" part.
        body_desc = ET.SubElement(body, 'span')
        body_desc.text = card_text

        # File size span at the bottom.
        body_size = ET.SubElement(body, 'span')
        body_size.set('class', 'small text-muted')
        body_size.text = f'{_human_size(file_size)}'
        return card

    def _is_download(self, m):
        ''' Determine if the ALT text [] part of the link says 'DOWNLOAD'. '''
        alt = m.group(2)
        return alt.lower() == 'download'

    def handleMatch(self, m):
        ''' Use the URL extension to render the link. '''
        src, parts = self.get_src(m)
        if self._is_download(m):
            return self.as_download(m)
        youtube = self.youtube_url_validation(src)
        if youtube:
            return self.as_youtube(m, youtube)
        src_lower = src.lower()
        if src_lower.endswith(self.SUPPORTED_TABLES):
            return self.as_csv(m)
        elif src_lower.endswith(self.SUPPORTED_VIDEO):
            return self.as_video(m)
        return self.as_image(m)


class OffsetHashHeaderProcessor(HashHeaderProcessor):
    ''' Process hash headers with an offset to control the type of heading
    DOM element that is generated. '''

    HEADING_LEVEL_OFFSET = 1

    def run(self, parent, blocks):
        block = blocks.pop(0)
        m = self.RE.search(block)
        if m:
            before = block[:m.start()]
            after = block[m.end():]
            if before:
                self.parser.parseBlocks(parent, [before])
            heading_level = len(m.group('level'))
            h = ET.SubElement(parent, 'h%d' % (heading_level + self.HEADING_LEVEL_OFFSET))
            h.text = m.group('header').strip()
            if after:
                blocks.insert(0, after)


# Remove the `video`, `iframe`, and `table` elements as block elements.
markdown.util.BLOCK_LEVEL_ELEMENTS = re.compile(
    r"^(p|div|h[1-6]|blockquote|pre|dl|ol|ul"
    r"|script|noscript|form|fieldset|math"
    r"|hr|hr/|style|li|dt|dd|thead|tbody"
    r"|tr|th|td|section|footer|header|group|figure"
    r"|figcaption|aside|article|canvas|output"
    r"|progress|nav|main)$",
    re.IGNORECASE
)


class MultiExtension(Extension):
    ''' Markdown `Extension` that adds our new components and
    overrides some that we are not using.
    '''
    def extendMarkdown(self, md, md_globals):
        ''' Configure markdown by disabling elements and replacing them with
        others. '''
        # Remove default patterns.
        del md.inlinePatterns['image_link']

        # Create a new one and insert into pipeline.
        multi_purpose_pattern = MultiPurposeLinkPattern(IMAGE_LINK_RE, md)
        md.inlinePatterns['multi_purpose_pattern'] = multi_purpose_pattern

        # Remove line headers.
        del md.parser.blockprocessors['setextheader']

        # Swap hash headers for one that can change the DOM h1, h2 level.
        md.parser.blockprocessors['hashheader'] = OffsetHashHeaderProcessor(md.parser)


# https://python-markdown.github.io/extensions/
mdextensions = [MultiExtension(),
                'markdown.extensions.tables',
                'markdown.extensions.meta',
                'markdown_checklist.extension',
                'markdown.extensions.def_list',
                'markdown.extensions.headerid',
                'markdown.extensions.fenced_code',
                'markdown.extensions.attr_list']


def build_meta_cache(root):
    ''' Recursively search for Markdown files and build a cache of `Meta`
    from metadata in the Markdown.
    :param str root The path to search for files from.
    '''
    doc_files = glob.iglob(root + '/**/*.md', recursive=True)

    def _meta(path):
        with open(path, 'r') as f:
            md = markdown.Markdown(extensions=mdextensions)
            md.page_root = os.path.dirname(path)
            Markup(md.convert(f.read()))
            return md.Meta
        return None

    doc_files_meta = {os.path.relpath(path, start=root): _meta(path) for path in doc_files}
    doc_files_meta = {path: value for path, value in doc_files_meta.items() if value is not None}
    return doc_files_meta


def build_nav_menu(meta_cache):
    ''' Given a cache of Markdown `Meta` data, compile a structure that can be
    used to generate the NAV menu.
    This uses the `nav: Assembly>Bench>Part` variable at the top of the Markdown file.
    '''
    tree = collections.UserDict()
    for url, meta in meta_cache.items():
        # Get the NAV string from the metadata.
        navstr = meta.get('nav', None)
        navstr = navstr[0] if navstr else None
        if not navstr:
            continue
        t = tree
        for part in navstr.split('>'):
            t = t.setdefault(part, collections.UserDict())
        t.meta = meta
        t.link = url
    return tree


def build_reload_files_list(extra_dirs=[]):
    ''' Given a list of directories, return a list of files to watch for modification
    and subsequent server reload. '''
    extra_files = extra_dirs[:]
    for extra_dir in extra_dirs:
        for dirname, dirs, files in os.walk(extra_dir):
            for filename in files:
                filename = os.path.join(dirname, filename)
                if os.path.isfile(filename):
                    extra_files.append(filename)
    return extra_files


def _render_markdown(file_path, **kwargs):
    ''' Given a `file_path` render the Markdown and return the result of `render_template`.
    '''
    global NAV_MENU, PROJECT_LOGO, PDF_GENERATION_ENABLED
    DEFAULT_TEMPLATE = 'document'
    with open(file_path, 'r') as f:
        md = markdown.Markdown(extensions=mdextensions)
        md.page_root = os.path.dirname(file_path)
        markup = Markup(md.convert(f.read()))

        # Fetch the template defined in the metadata.
        template = md.Meta.get('template', None)
        template = template[0] if template else DEFAULT_TEMPLATE
        if not template:
            raise Exception('no template found for document')
        template = f'{template}.html'
        return render_template(template,
                               content=markup,
                               nav_menu=NAV_MENU,
                               project_logo=PROJECT_LOGO,
                               pdf_enabled=PDF_GENERATION_ENABLED,
                               **md.Meta,
                               **kwargs)


def configure_flask(app, root_dir):
    ''' Setup the flask application within this scope. '''

    @app.template_filter('gravatar')
    def gravatar(email, size=100, rating='g', default='retro', use_ssl=False):
        ''' Return a gravatar link for a given email address. '''
        url = "https://secure.gravatar.com/avatar/" if use_ssl else "http://www.gravatar.com/avatar/"
        email = email.strip().lower().encode('utf-8')
        hashemail = hashlib.md5(email).hexdigest()
        return f'{url}{hashemail}?s={size}&r={rating}&d={default}'

    @app.template_filter()
    def timesince(dt, past_="ago", future_="from now", default="just now"):
        ''' Returns string representing "time since" e.g. 3 days ago, 5 hours ago etc.
        :param str dt Input date string in the format %Y/%m/%d
        http://flask.pocoo.org/snippets/33/
        '''
        dt = datetime.datetime.strptime(dt, '%Y/%m/%d')
        return timeago.format(dt, datetime.datetime.utcnow())

    @app.template_filter()
    def url_unquote(url):
        ''' Removes encoding around a URL. '''
        return urllib.parse.unquote(url)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route("/print_header")
    def print_header():
        ''' Render the template for the header used when printing with WKPDFTOHTML. '''
        global PROJECT_LOGO
        return render_template('print_header.html', project_logo=PROJECT_LOGO)

    @app.route("/print_footer")
    def print_footer():
        ''' Render the template for the footer used when printing with WKPDFTOHTML. '''
        global PROJECT_LOGO
        return render_template('print_footer.html', project_logo=PROJECT_LOGO)

    @app.errorhandler(404)
    def page_not_found(e):
        global NAV_MENU, PROJECT_LOGO
        return render_template('404.html', nav_menu=NAV_MENU, project_logo=PROJECT_LOGO), 404

    @app.route("/w/<path:page>")
    def wiki(page):
        ''' Render the page. '''
        file_path = os.path.abspath(os.path.join(root_dir, page))
        if not os.path.isfile(file_path):
            abort(404)

        if '.md' in [ext.lower() for ext in os.path.splitext(file_path)]:
            return _render_markdown(file_path, current_page=page)
        else:
            return send_from_directory(os.path.dirname(file_path), os.path.basename(file_path))

    @app.route("/")
    @app.route("/w/")
    def homepage():
        return wiki('home.md')

    @app.route("/pdf/<path:page>")
    def wiki_pdf(page):
        file_path = os.path.abspath(os.path.join(root_dir, page))
        if not os.path.isfile(file_path):
            abort(404)

        if '.md' not in [ext.lower() for ext in os.path.splitext(file_path)]:
            return send_from_directory(os.path.dirname(file_path), os.path.basename(file_path))

        # Configure the different paths.
        pdf_temp = f'{tempfile.mktemp()}.pdf'
        binary_path = 'wkhtmltopdf_0.12.5.exe'
        input_url = url_for('wiki', page=page, _external=True)
        header_url = url_for('print_header', _external=True)
        footer_url = url_for('print_footer', _external=True)
        args = f'{binary_path} --header-html {header_url} --footer-html {footer_url} \
                --print-media-type --header-spacing 2  {input_url} {pdf_temp}'

        # Invoke WkHTMLtoPDF
        result = subprocess.check_output(args, shell=True)
        if not result:
            pass

        # Write the newly generated temp pdf into a response.
        with open(pdf_temp, 'rb') as f:
            binary_pdf = f.read()
            target_file_name = page.replace("/", "_").replace("\\", "_")
            response = make_response(binary_pdf)
            response.headers['Content-Type'] = 'application/pdf'
            # response.headers['Content-Disposition'] = f'attachment; filename={target_file_name}.pdf'
            response.headers['Content-Disposition'] = f'inline; filename={target_file_name}.pdf'

        # Delete the temp file and return the response.
        os.remove(pdf_temp)
        return response


def generate_static_pdf(app, root_dir, output_dir='build'):
    ''' Generate a static PDF directory for the documentation in `root_dir`
    into `output_dir`.
    '''
    # All the document URLs.
    markdown_docs_urls = [file.replace(f'{root_dir}\\', 'pdf/').replace('\\', '/')
                          for file in glob.iglob(f'{root_dir}/**/*', recursive=True)
                          if os.path.isfile(file) and file.endswith('.md')]

    # Generate URl to file pairs.
    pairs = [(f'http://localhost:5000/{url}',
             f'{os.path.join(output_dir, *os.path.split(url))}.pdf')
             for url in markdown_docs_urls]

    # Download each pair.
    for source, target in pairs:
        os.makedirs(os.path.dirname(target), mode=755, exist_ok=True)
        urllib.request.urlretrieve(source, target)


def generate_static_html(app, root_dir, output_dir='build'):
    ''' Generate a static HTML site for the documentation in `root_dir`
    into `output_dir`.
    '''
    from flask_frozen import Freezer

    # Update the flask config.
    app.config['FREEZER_RELATIVE_URLS'] = True
    app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
    app.config['FREEZER_DESTINATION'] = output_dir

    # Create the freezer app.  Make it use specific URLs.
    freezer = Freezer(app, with_no_argument_rules=False, log_url_for=False)

    # Register a generator that passes ALL files in the docs directory into the
    # `wiki` flask route.
    @freezer.register_generator
    def wiki():
        all_docs = [file.replace(f'{root_dir}\\', '/w/').replace('\\', '/')
                    for file in glob.iglob(f'{root_dir}/**/*', recursive=True)
                    if os.path.isfile(file)]
        for doc in all_docs:
            yield doc

    # Save all the URLs using the correct extension and MIME type.
    freezer.freeze()

    # Helper function to return the domain if present.
    def is_absolute(url):
        return bool(urlparse(url).netloc)

    # For each `.md` file in the output directory:
    for markdown_file in glob.iglob(f'{output_dir}/**/*.md', recursive=True):

        # Rewrite all relative links to other `.md` files to `.html.`
        output = ''
        with open(markdown_file, 'r') as f:
            html = f.read()

            def _href_replace(m):
                href = m.group()
                if is_absolute(href[6:-1]):
                    return href
                return href.replace('.md', '.html')

            output = re.sub('href="(.*md)"', _href_replace, html)

        # Rename the file from `.md` to HTML.
        with open(markdown_file[:-3] + '.html', 'w') as f:
            f.write(output)

        # Delete the Markdown file.
        os.remove(markdown_file)


def load_project_logo(logo_file=None):
    ''' Attempt to load the project logo from the specified path.
    If this fails, return None.  If this succeeds, convert it to a data-uri.
    '''
    if not logo_file:
        return None
    if not os.path.exists(logo_file):
        return None
    with open(logo_file, 'rb') as fp:
        mime = 'image/png'
        data64 = base64.b64encode(fp.read()).decode('utf-8')
        preview_uri = u'data:%s;base64,%s' % (mime, data64)
        return preview_uri


def check_pdf_generation_cap():
    ''' Check to see if we can use PDF generation by attempting to use the binary. '''
    global WKHTMLTOPDF_BINARY
    dev_null = open(os.devnull, 'wb')
    try:
        subprocess.check_output(f'{WKHTMLTOPDF_BINARY} --version', shell=True)
        return True
    except Exception:
        return False
    finally:
        dev_null.close()


def copy_local_project():
    ''' Copy the sample docs and style into the local working directory.
    Note: This will overwrite anything currently in those folders.
    '''
    source_root = os.path.dirname(__file__)
    target_root = os.getcwd()

    targets = ['docs', 'style', 'logo.png']
    pairs = [(os.path.join(source_root, path), os.path.join(target_root, path))
             for path in targets]

    for source, target in pairs:
        print(f'Copying: {source} -> {target}')
        if os.path.isdir(source):
            if os.path.exists(target):
                shutil.rmtree(target)
            shutil.copytree(source, target)
        else:
            if os.path.exists(target):
                os.remove(target)
            shutil.copyfile(source, target)


global NAV_MENU, PROJECT_LOGO, WKHTMLTOPDF_BINARY, PDF_GENERATION_ENABLED

NAV_MENU = {}
PROJECT_LOGO = None
WKHTMLTOPDF_BINARY = None
PDF_GENERATION_ENABLED = False


def main():
    ''' Application entrypoint. '''

    # Parse the command line arguments.
    parser = argparse.ArgumentParser(description='DocServe: Lightweight server for rendering \
                                     Markdown documentation with different templates.')

    parser.add_argument('--html', action='store', dest='html_output_dir',
                        help='Generate a static site from the server and output to the \
                        specified directory.')

    parser.add_argument('--pdf', action='store', dest='pdf_output_dir',
                        help='Generate static PDFs from the server and output to the \
                        specified directory.')

    parser.add_argument('--new', action="store_true", dest='new_project',
                        default=False,
                        help='Copy the `docs` and `styles` folder into the working directory \
                        and output a config file that addresses them.')

    parser.add_argument('--dirs', action="store_true", dest='show_dirs',
                        default=False,
                        help='Display the different directories the software is using \
                        to search for documentation and styles.')
    args = parser.parse_args()

    # If the user is asking to create a new project.
    if args.new_project:
        copy_local_project()
        sys.exit()

    # Load config from the environment and validate it.
    global PROJECT_LOGO, PDF_GENERATION_ENABLED, NAV_MENU, WKHTMLTOPDF_BINARY
    TRUE = 'TRUE'
    FALSE = 'FALSE'
    flask_debug = os.environ.get('DS_FLASK_DEBUG', FALSE) == TRUE
    flask_watch = os.environ.get('DS_FLASK_CHANGERELOAD', TRUE) == TRUE
    WKHTMLTOPDF_BINARY = os.environ.get('DS_WKHTMLTOPDF', 'wkhtmltopdf_0.12.5.exe')
    PDF_GENERATION_ENABLED = check_pdf_generation_cap()
    # TODO: flask_server_name = os.environ.get('DS_FLASK_SERVER_NAME', 'localhost:5000')

    dir_documents = os.environ.get('DS_DOCS_DIR', os.path.join(os.getcwd(), 'docs'))
    dir_style = os.environ.get('DS_STYLE_DIR', os.path.join(os.getcwd(), 'style'))
    logo_location = os.environ.get('DS_PROJECT_LOGO', os.path.join(os.getcwd(), 'logo.png'))

    # If `style` folder does not exist, use the one in site-packages.
    if not os.path.exists(dir_style) and not os.path.isdir(dir_style):
        dir_style = os.path.join(os.path.dirname(__file__), 'style')

    # app_project_name = os.environ.get('DS_PROJECT_NAME', 'Documentation')
    # app_project_icon = os.environ.get('DS_PROJECT_ICON', os.path.join(dir_style, 'icon.png'))

    # Attempt to load the project logo into a base64 data uri.
    PROJECT_LOGO = load_project_logo(logo_location)

    # Compute the static and template directories.
    dir_static = os.path.join(dir_style, 'static')
    dir_templates = os.path.join(dir_style, 'templates')

    if args.show_dirs:
        print('The following directories are being used: ')
        print('\t', f'Documents  -> {dir_documents}')
        print('\t', f'Logo       -> {logo_location}')
        print('\t', f'Style      -> {dir_style}')
        print('\t', f' Static    -> {dir_static}')
        print('\t', f' Templates -> {dir_templates}')
        sys.exit()

    if not os.path.exists(dir_documents) and not os.path.isdir(dir_documents):
        print(f'Error: Documents directory "{dir_documents}" does not exist.  \
        Create one called `docs` and fill it with your documentation.', file=sys.stderr)
        sys.exit(-1)

    if not os.path.exists(dir_static) and not os.path.isdir(dir_static):
        print(f'Error: Static directory "{dir_static}" does not exist.', file=sys.stderr)
        sys.exit(-1)

    if not os.path.exists(dir_templates) and not os.path.isdir(dir_templates):
        print(f'Error: Templates directory "{dir_templates}" does not exist.', file=sys.stderr)
        sys.exit(-1)

    # Build an in-memory cache of document meta-data.
    # NOTE: The design choice is made to crash the application if any
    # of the markdown files cannot be opened and parsed. In the
    # future when it becomes more stable, this will probably change.
    meta_cache = build_meta_cache(dir_documents)

    # Build the nav menu data-structure.
    nav_menu = build_nav_menu(meta_cache)
    NAV_MENU = nav_menu

    # Create the server.
    app = Flask(__name__,
                static_url_path='',
                template_folder=dir_templates,
                static_folder=dir_static)

    # Attach routes and filters.
    configure_flask(app, dir_documents)

    # Output PDF files.
    if args.pdf_output_dir:
        if not check_pdf_generation_cap():
            print(f'Error: PDF generation requires WkHTMLtoPDF.', file=sys.stderr)
            sys.exit(-1)

        def gen_pdfs():
            time.sleep(2)
            generate_static_pdf(app, dir_documents, output_dir=args.pdf_output_dir)
            time.sleep(5)
            os.kill(os.getpid(), signal.SIGTERM)

        t1 = threading.Thread(target=gen_pdfs)
        t1.start()
        app.run(debug=flask_debug, threaded=True)
        sys.exit()

    # Output a static site.
    if args.html_output_dir:
        PDF_GENERATION_ENABLED = False
        try:
            generate_static_html(app, dir_documents, args.html_output_dir)
        except Exception as err:
            traceback.print_exc(file=sys.stderr)
            sys.exit(-1)
        sys.exit()

    # If we are running with a watcher, build the files to watch.
    extra_files = build_reload_files_list([dir_documents, dir_style]) if flask_watch else []
    app.run(debug=flask_debug, extra_files=extra_files)


# if running brainerd directly, boot the app
if __name__ == "__main__":
    main()
