#!/usr/bin/env python
# coding: utf-8

from __future__ import unicode_literals
import mock

from mkdocs.structure.pages import Page
from mkdocs.structure.files import File, Files
from mkdocs.structure.nav import get_navigation
from mkdocs.commands import build
from mkdocs.tests.base import load_config, LogTestCase, tempdir, PathAssertionMixin
from mkdocs.utils import meta


def build_page(title, path, config, md_src=''):
    """ Helper which returns a Page object. """

    files = Files([File(path, config['docs_dir'], config['site_dir'], config['use_directory_urls'])])
    page = Page(title, list(files)[0], config)
    # Fake page.read_source()
    page.markdown, page.meta = meta.get_data(md_src)
    return page, files


class BuildTests(PathAssertionMixin, LogTestCase):

    # Test build.get_context

    def test_context_base_url_homepage(self):
        nav_cfg = [
            {'Home': 'index.md'}
        ]
        cfg = load_config(nav=nav_cfg, use_directory_urls=False)
        files = Files([
            File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
        ])
        nav = get_navigation(files, cfg)
        context = build.get_context(nav, files, cfg, nav.pages[0])
        self.assertEqual(context['base_url'], '.')

    def test_context_base_url_homepage_use_directory_urls(self):
        nav_cfg = [
            {'Home': 'index.md'}
        ]
        cfg = load_config(nav=nav_cfg)
        files = Files([
            File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
        ])
        nav = get_navigation(files, cfg)
        context = build.get_context(nav, files, cfg, nav.pages[0])
        self.assertEqual(context['base_url'], '.')

    def test_context_base_url_nested_page(self):
        nav_cfg = [
            {'Home': 'index.md'},
            {'Nested': 'foo/bar.md'}
        ]
        cfg = load_config(nav=nav_cfg, use_directory_urls=False)
        files = Files([
            File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
            File('foo/bar.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])
        ])
        nav = get_navigation(files, cfg)
        context = build.get_context(nav, files, cfg, nav.pages[1])
        self.assertEqual(context['base_url'], '..')

    def test_context_base_url_nested_page_use_directory_urls(self):
        nav_cfg = [
            {'Home': 'index.md'},
            {'Nested': 'foo/bar.md'}
        ]
        cfg = load_config(nav=nav_cfg)
        files = Files([
            File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
            File('foo/bar.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])
        ])
        nav = get_navigation(files, cfg)
        context = build.get_context(nav, files, cfg, nav.pages[1])
        self.assertEqual(context['base_url'], '../..')

    def test_context_base_url_relative_no_page(self):
        cfg = load_config(use_directory_urls=False)
        context = build.get_context(mock.Mock(), mock.Mock(), cfg, base_url='..')
        self.assertEqual(context['base_url'], '..')

    def test_context_base_url_relative_no_page_use_directory_urls(self):
        cfg = load_config()
        context = build.get_context(mock.Mock(), mock.Mock(), cfg, base_url='..')
        self.assertEqual(context['base_url'], '..')

    def test_context_base_url_absolute_no_page(self):
        cfg = load_config(use_directory_urls=False)
        context = build.get_context(mock.Mock(), mock.Mock(), cfg, base_url='/')
        self.assertEqual(context['base_url'], '')

    def test_context_base_url__absolute_no_page_use_directory_urls(self):
        cfg = load_config()
        context = build.get_context(mock.Mock(), mock.Mock(), cfg, base_url='/')
        self.assertEqual(context['base_url'], '')

    def test_context_base_url_absolute_nested_no_page(self):
        cfg = load_config(use_directory_urls=False)
        context = build.get_context(mock.Mock(), mock.Mock(), cfg, base_url='/foo/')
        self.assertEqual(context['base_url'], '/foo')

    def test_context_base_url__absolute_nested_no_page_use_directory_urls(self):
        cfg = load_config()
        context = build.get_context(mock.Mock(), mock.Mock(), cfg, base_url='/foo/')
        self.assertEqual(context['base_url'], '/foo')

    def test_context_extra_css_js_from_homepage(self):
        nav_cfg = [
            {'Home': 'index.md'}
        ]
        cfg = load_config(
            nav=nav_cfg,
            extra_css=['style.css'],
            extra_javascript=['script.js'],
            use_directory_urls=False
        )
        files = Files([
            File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
        ])
        nav = get_navigation(files, cfg)
        context = build.get_context(nav, files, cfg, nav.pages[0])
        self.assertEqual(context['extra_css'], ['style.css'])
        self.assertEqual(context['extra_javascript'], ['script.js'])

    def test_context_extra_css_js_from_nested_page(self):
        nav_cfg = [
            {'Home': 'index.md'},
            {'Nested': 'foo/bar.md'}
        ]
        cfg = load_config(
            nav=nav_cfg,
            extra_css=['style.css'],
            extra_javascript=['script.js'],
            use_directory_urls=False
        )
        files = Files([
            File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
            File('foo/bar.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])
        ])
        nav = get_navigation(files, cfg)
        context = build.get_context(nav, files, cfg, nav.pages[1])
        self.assertEqual(context['extra_css'], ['../style.css'])
        self.assertEqual(context['extra_javascript'], ['../script.js'])

    def test_context_extra_css_js_from_nested_page_use_directory_urls(self):
        nav_cfg = [
            {'Home': 'index.md'},
            {'Nested': 'foo/bar.md'}
        ]
        cfg = load_config(
            nav=nav_cfg,
            extra_css=['style.css'],
            extra_javascript=['script.js']
        )
        files = Files([
            File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
            File('foo/bar.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])
        ])
        nav = get_navigation(files, cfg)
        context = build.get_context(nav, files, cfg, nav.pages[1])
        self.assertEqual(context['extra_css'], ['../../style.css'])
        self.assertEqual(context['extra_javascript'], ['../../script.js'])

    def test_context_extra_css_js_no_page(self):
        cfg = load_config(extra_css=['style.css'], extra_javascript=['script.js'])
        context = build.get_context(mock.Mock(), mock.Mock(), cfg, base_url='..')
        self.assertEqual(context['extra_css'], ['../style.css'])
        self.assertEqual(context['extra_javascript'], ['../script.js'])

    def test_extra_context(self):
        cfg = load_config(extra={'a': 1})
        context = build.get_context(mock.Mock(), mock.Mock(), cfg)
        self.assertEqual(context['config']['extra']['a'], 1)

    # Test build._build_theme_template

    @mock.patch('mkdocs.utils.write_file')
    @mock.patch('mkdocs.commands.build._build_template', return_value='some content')
    def test_build_theme_template(self, mock_build_template, mock_write_file):
        cfg = load_config()
        env = cfg['theme'].get_env()
        build._build_theme_template('main.html', env, mock.Mock(), cfg, mock.Mock())
        mock_write_file.assert_called_once()
        mock_build_template.assert_called_once()

    @mock.patch('mkdocs.utils.write_file')
    @mock.patch('mkdocs.commands.build._build_template', return_value='some content')
    @mock.patch('gzip.open')
    def test_build_sitemap_template(self, mock_gzip_open, mock_build_template, mock_write_file):
        cfg = load_config()
        env = cfg['theme'].get_env()
        build._build_theme_template('sitemap.xml', env, mock.Mock(), cfg, mock.Mock())
        mock_write_file.assert_called_once()
        mock_build_template.assert_called_once()
        mock_gzip_open.assert_called_once()

    @mock.patch('mkdocs.utils.write_file')
    @mock.patch('mkdocs.commands.build._build_template', return_value='')
    def test_skip_missing_theme_template(self, mock_build_template, mock_write_file):
        cfg = load_config()
        env = cfg['theme'].get_env()
        with self.assertLogs('mkdocs', level='WARN') as cm:
            build._build_theme_template('missing.html', env, mock.Mock(), cfg, mock.Mock())
        self.assertEqual(
            cm.output,
            ["WARNING:mkdocs.commands.build:Template skipped: 'missing.html' not found in theme directories."]
        )
        mock_write_file.assert_not_called()
        mock_build_template.assert_not_called()

    @mock.patch('mkdocs.utils.write_file')
    @mock.patch('mkdocs.commands.build._build_template', return_value='')
    def test_skip_theme_template_empty_output(self, mock_build_template, mock_write_file):
        cfg = load_config()
        env = cfg['theme'].get_env()
        with self.assertLogs('mkdocs', level='INFO') as cm:
            build._build_theme_template('main.html', env, mock.Mock(), cfg, mock.Mock())
        self.assertEqual(
            cm.output,
            ["INFO:mkdocs.commands.build:Template skipped: 'main.html' generated empty output."]
        )
        mock_write_file.assert_not_called()
        mock_build_template.assert_called_once()

    # Test build._build_extra_template

    @mock.patch('io.open', mock.mock_open(read_data='template content'))
    def test_build_extra_template(self):
        cfg = load_config()
        files = Files([
            File('foo.html', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
        ])
        build._build_extra_template('foo.html', files, cfg, mock.Mock())

    @mock.patch('io.open', mock.mock_open(read_data='template content'))
    def test_skip_missing_extra_template(self):
        cfg = load_config()
        files = Files([
            File('foo.html', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
        ])
        with self.assertLogs('mkdocs', level='INFO') as cm:
            build._build_extra_template('missing.html', files, cfg, mock.Mock())
        self.assertEqual(
            cm.output,
            ["WARNING:mkdocs.commands.build:Template skipped: 'missing.html' not found in docs_dir."]
        )

    @mock.patch('io.open', side_effect=IOError('Error message.'))
    def test_skip_ioerror_extra_template(self, mock_open):
        cfg = load_config()
        files = Files([
            File('foo.html', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
        ])
        with self.assertLogs('mkdocs', level='INFO') as cm:
            build._build_extra_template('foo.html', files, cfg, mock.Mock())
        self.assertEqual(
            cm.output,
            ["WARNING:mkdocs.commands.build:Error reading template 'foo.html': Error message."]
        )

    @mock.patch('io.open', mock.mock_open(read_data=''))
    def test_skip_extra_template_empty_output(self):
        cfg = load_config()
        files = Files([
            File('foo.html', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls']),
        ])
        with self.assertLogs('mkdocs', level='INFO') as cm:
            build._build_extra_template('foo.html', files, cfg, mock.Mock())
        self.assertEqual(
            cm.output,
            ["INFO:mkdocs.commands.build:Template skipped: 'foo.html' generated empty output."]
        )

    # Test build._populate_page

    @tempdir(files={'index.md': 'page content'})
    def test_populate_page(self, docs_dir):
        cfg = load_config(docs_dir=docs_dir)
        file = File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])
        page = Page('Foo', file, cfg)
        build._populate_page(page, cfg, Files([file]))
        self.assertEqual(page.content, '<p>page content</p>')

    @tempdir(files={'testing.html': '<p>page content</p>'})
    def test_populate_page_dirty_modified(self, site_dir):
        cfg = load_config(site_dir=site_dir)
        file = File('testing.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])
        page = Page('Foo', file, cfg)
        build._populate_page(page, cfg, Files([file]), dirty=True)
        self.assertTrue(page.markdown.startswith('# Welcome to MkDocs'))
        self.assertTrue(page.content.startswith('<h1 id="welcome-to-mkdocs">Welcome to MkDocs</h1>'))

    @tempdir(files={'index.md': 'page content'})
    @tempdir(files={'index.html': '<p>page content</p>'})
    def test_populate_page_dirty_not_modified(self, site_dir, docs_dir):
        cfg = load_config(docs_dir=docs_dir, site_dir=site_dir)
        file = File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])
        page = Page('Foo', file, cfg)
        build._populate_page(page, cfg, Files([file]), dirty=True)
        # Content is empty as file read was skipped
        self.assertEqual(page.markdown, None)
        self.assertEqual(page.content, None)

    @tempdir(files={'index.md': 'new page content'})
    @mock.patch('io.open', side_effect=IOError('Error message.'))
    def test_populate_page_read_error(self, docs_dir, mock_open):
        cfg = load_config(docs_dir=docs_dir)
        file = File('missing.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])
        page = Page('Foo', file, cfg)
        with self.assertLogs('mkdocs', level='ERROR') as cm:
            self.assertRaises(IOError, build._populate_page, page, cfg, Files([file]))
        self.assertEqual(
            cm.output, [
                'ERROR:mkdocs.structure.pages:File not found: missing.md',
                "ERROR:mkdocs.commands.build:Error reading page 'missing.md': Error message."
            ]
        )
        mock_open.assert_called_once()

    # Test build._build_page

    @tempdir()
    def test_build_page(self, site_dir):
        cfg = load_config(site_dir=site_dir, nav=['index.md'], plugins=[])
        files = Files([File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])])
        nav = get_navigation(files, cfg)
        page = files.documentation_pages()[0].page
        # Fake populate page
        page.title = 'Title'
        page.markdown = 'page content'
        page.content = '<p>page content</p>'
        build._build_page(page, cfg, files, nav, cfg['theme'].get_env())
        self.assertPathIsFile(site_dir, 'index.html')

    # TODO: fix this. It seems that jinja2 chokes on the mock object. Not sure how to resolve.
    # @tempdir()
    # @mock.patch('jinja2.environment.Template')
    # def test_build_page_empty(self, site_dir, mock_template):
    #     mock_template.render = mock.Mock(return_value='')
    #     cfg = load_config(site_dir=site_dir, nav=['index.md'], plugins=[])
    #     files = Files([File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])])
    #     nav = get_navigation(files, cfg)
    #     page = files.documentation_pages()[0].page
    #     # Fake populate page
    #     page.title = ''
    #     page.markdown = ''
    #     page.content = ''
    #     with self.assertLogs('mkdocs', level='INFO') as cm:
    #         build._build_page(page, cfg, files, nav, cfg['theme'].get_env())
    #     self.assertEqual(
    #         cm.output,
    #         ["INFO:mkdocs.commands.build:Page skipped: 'index.md'. Generated empty output."]
    #     )
    #     mock_template.render.assert_called_once()
    #     self.assertPathNotFile(site_dir, 'index.html')

    @tempdir(files={'index.md': 'page content'})
    @tempdir(files={'index.html': '<p>page content</p>'})
    @mock.patch('mkdocs.utils.write_file')
    def test_build_page_dirty_modified(self, site_dir, docs_dir, mock_write_file):
        cfg = load_config(docs_dir=docs_dir, site_dir=site_dir, nav=['index.md'], plugins=[])
        files = Files([File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])])
        nav = get_navigation(files, cfg)
        page = files.documentation_pages()[0].page
        # Fake populate page
        page.title = 'Title'
        page.markdown = 'new page content'
        page.content = '<p>new page content</p>'
        build._build_page(page, cfg, files, nav, cfg['theme'].get_env(), dirty=True)
        mock_write_file.assert_not_called()

    @tempdir(files={'testing.html': '<p>page content</p>'})
    @mock.patch('mkdocs.utils.write_file')
    def test_build_page_dirty_not_modified(self, site_dir, mock_write_file):
        cfg = load_config(site_dir=site_dir, nav=['index.md'], plugins=[])
        files = Files([File('testing.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])])
        nav = get_navigation(files, cfg)
        page = files.documentation_pages()[0].page
        # Fake populate page
        page.title = 'Title'
        page.markdown = 'page content'
        page.content = '<p>page content</p>'
        build._build_page(page, cfg, files, nav, cfg['theme'].get_env(), dirty=True)
        mock_write_file.assert_called_once()

    @tempdir()
    def test_build_page_custom_template(self, site_dir):
        cfg = load_config(site_dir=site_dir, nav=['index.md'], plugins=[])
        files = Files([File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])])
        nav = get_navigation(files, cfg)
        page = files.documentation_pages()[0].page
        # Fake populate page
        page.title = 'Title'
        page.meta = {'template': '404.html'}
        page.markdown = 'page content'
        page.content = '<p>page content</p>'
        build._build_page(page, cfg, files, nav, cfg['theme'].get_env())
        self.assertPathIsFile(site_dir, 'index.html')

    @tempdir()
    @mock.patch('mkdocs.utils.write_file', side_effect=IOError('Error message.'))
    def test_build_page_error(self, site_dir, mock_write_file):
        cfg = load_config(site_dir=site_dir, nav=['index.md'], plugins=[])
        files = Files([File('index.md', cfg['docs_dir'], cfg['site_dir'], cfg['use_directory_urls'])])
        nav = get_navigation(files, cfg)
        page = files.documentation_pages()[0].page
        # Fake populate page
        page.title = 'Title'
        page.markdown = 'page content'
        page.content = '<p>page content</p>'
        with self.assertLogs('mkdocs', level='ERROR') as cm:
            self.assertRaises(IOError, build._build_page, page, cfg, files, nav, cfg['theme'].get_env())
        self.assertEqual(
            cm.output,
            ["ERROR:mkdocs.commands.build:Error building page 'index.md': Error message."]
        )
        mock_write_file.assert_called_once()

    # Test build.build

    @tempdir(files={
        'index.md': 'page content',
        'empty.md': '',
        'img.jpg': '',
        'static.html': 'content',
        '.hidden': 'content',
        '.git/hidden': 'content'
    })
    @tempdir()
    def test_copying_media(self, site_dir, docs_dir):
        cfg = load_config(docs_dir=docs_dir, site_dir=site_dir)
        build.build(cfg)

        # Verify that only non-empty md file (coverted to html), static HTML file and image are copied.
        self.assertPathIsFile(site_dir, 'index.html')
        self.assertPathIsFile(site_dir, 'img.jpg')
        self.assertPathIsFile(site_dir, 'static.html')
        self.assertPathNotExists(site_dir, 'empty.md')
        self.assertPathNotExists(site_dir, '.hidden')
        self.assertPathNotExists(site_dir, '.git/hidden')

    @tempdir(files={'index.md': 'page content'})
    @tempdir()
    def test_copy_theme_files(self, site_dir, docs_dir):
        cfg = load_config(docs_dir=docs_dir, site_dir=site_dir)
        build.build(cfg)

        # Verify only theme media are copied, not templates or Python files.
        self.assertPathIsFile(site_dir, 'index.html')
        self.assertPathIsFile(site_dir, '404.html')
        self.assertPathIsDir(site_dir, 'js')
        self.assertPathIsDir(site_dir, 'css')
        self.assertPathIsDir(site_dir, 'img')
        self.assertPathIsDir(site_dir, 'fonts')
        self.assertPathNotExists(site_dir, '__init__.py')
        self.assertPathNotExists(site_dir, '__init__.pyc')
        self.assertPathNotExists(site_dir, 'base.html')
        self.assertPathNotExists(site_dir, 'content.html')
        self.assertPathNotExists(site_dir, 'main.html')

    # Test build.site_directory_contains_stale_files

    @tempdir(files=['index.html'])
    def test_site_dir_contains_stale_files(self, site_dir):
        self.assertTrue(build.site_directory_contains_stale_files(site_dir))

    @tempdir()
    def test_not_site_dir_contains_stale_files(self, site_dir):
        self.assertFalse(build.site_directory_contains_stale_files(site_dir))
