import unittest
import os
import io
import mock

from mkdocs.structure.files import Files, File, get_files, _sort_files, _filter_paths
from mkdocs.tests.base import load_config, tempdir, PathAssertionMixin


class TestFiles(PathAssertionMixin, unittest.TestCase):

    def test_file_eq(self):
        file = File('a.md', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        self.assertTrue(file == File('a.md', '/path/to/docs', '/path/to/site', use_directory_urls=False))

    def test_file_ne(self):
        file = File('a.md', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        # Different filename
        self.assertTrue(file != File('b.md', '/path/to/docs', '/path/to/site', use_directory_urls=False))
        # Different src_path
        self.assertTrue(file != File('a.md', '/path/to/other', '/path/to/site', use_directory_urls=False))
        # Different URL
        self.assertTrue(file != File('a.md', '/path/to/docs', '/path/to/site', use_directory_urls=True))

    def test_sort_files(self):
        self.assertEqual(
            _sort_files(['b.md', 'bb.md', 'a.md', 'index.md', 'aa.md']),
            ['index.md', 'a.md', 'aa.md', 'b.md', 'bb.md']
        )

        self.assertEqual(
            _sort_files(['b.md', 'index.html', 'a.md', 'index.md']),
            ['index.html', 'index.md', 'a.md', 'b.md']
        )

        self.assertEqual(
            _sort_files(['a.md', 'index.md', 'b.md', 'index.html']),
            ['index.md', 'index.html', 'a.md', 'b.md']
        )

        self.assertEqual(
            _sort_files(['.md', '_.md', 'a.md', 'index.md', '1.md']),
            ['index.md', '.md', '1.md', '_.md', 'a.md']
        )

        self.assertEqual(
            _sort_files(['a.md', 'b.md', 'a.md']),
            ['a.md', 'a.md', 'b.md']
        )

        self.assertEqual(
            _sort_files(['A.md', 'B.md', 'README.md']),
            ['README.md', 'A.md', 'B.md']
        )

    def test_md_file(self):
        f = File('foo.md', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        self.assertPathsEqual(f.src_path, 'foo.md')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo.md')
        self.assertPathsEqual(f.dest_path, 'foo.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo.html')
        self.assertEqual(f.url, 'foo.html')
        self.assertEqual(f.name, 'foo')
        self.assertTrue(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_md_file_use_directory_urls(self):
        f = File('foo.md', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        self.assertPathsEqual(f.src_path, 'foo.md')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo.md')
        self.assertPathsEqual(f.dest_path, 'foo/index.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/index.html')
        self.assertEqual(f.url, 'foo/')
        self.assertEqual(f.name, 'foo')
        self.assertTrue(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_md_file_nested(self):
        f = File('foo/bar.md', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        self.assertPathsEqual(f.src_path, 'foo/bar.md')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.md')
        self.assertPathsEqual(f.dest_path, 'foo/bar.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar.html')
        self.assertEqual(f.url, 'foo/bar.html')
        self.assertEqual(f.name, 'bar')
        self.assertTrue(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_md_file_nested_use_directory_urls(self):
        f = File('foo/bar.md', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        self.assertPathsEqual(f.src_path, 'foo/bar.md')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.md')
        self.assertPathsEqual(f.dest_path, 'foo/bar/index.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar/index.html')
        self.assertEqual(f.url, 'foo/bar/')
        self.assertEqual(f.name, 'bar')
        self.assertTrue(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_md_index_file(self):
        f = File('index.md', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        self.assertPathsEqual(f.src_path, 'index.md')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/index.md')
        self.assertPathsEqual(f.dest_path, 'index.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/index.html')
        self.assertEqual(f.url, 'index.html')
        self.assertEqual(f.name, 'index')
        self.assertTrue(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_md_index_file_use_directory_urls(self):
        f = File('index.md', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        self.assertPathsEqual(f.src_path, 'index.md')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/index.md')
        self.assertPathsEqual(f.dest_path, 'index.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/index.html')
        self.assertEqual(f.url, '.')
        self.assertEqual(f.name, 'index')
        self.assertTrue(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_md_index_file_nested(self):
        f = File('foo/index.md', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        self.assertPathsEqual(f.src_path, 'foo/index.md')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/index.md')
        self.assertPathsEqual(f.dest_path, 'foo/index.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/index.html')
        self.assertEqual(f.url, 'foo/index.html')
        self.assertEqual(f.name, 'index')
        self.assertTrue(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_md_index_file_nested_use_directory_urls(self):
        f = File('foo/index.md', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        self.assertPathsEqual(f.src_path, 'foo/index.md')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/index.md')
        self.assertPathsEqual(f.dest_path, 'foo/index.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/index.html')
        self.assertEqual(f.url, 'foo/')
        self.assertEqual(f.name, 'index')
        self.assertTrue(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_static_file(self):
        f = File('foo/bar.html', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        self.assertPathsEqual(f.src_path, 'foo/bar.html')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.html')
        self.assertPathsEqual(f.dest_path, 'foo/bar.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar.html')
        self.assertEqual(f.url, 'foo/bar.html')
        self.assertEqual(f.name, 'bar')
        self.assertFalse(f.is_documentation_page())
        self.assertTrue(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_static_file_use_directory_urls(self):
        f = File('foo/bar.html', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        self.assertPathsEqual(f.src_path, 'foo/bar.html')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.html')
        self.assertPathsEqual(f.dest_path, 'foo/bar.html')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar.html')
        self.assertEqual(f.url, 'foo/bar.html')
        self.assertEqual(f.name, 'bar')
        self.assertFalse(f.is_documentation_page())
        self.assertTrue(f.is_static_page())
        self.assertFalse(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_media_file(self):
        f = File('foo/bar.jpg', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        self.assertPathsEqual(f.src_path, 'foo/bar.jpg')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.jpg')
        self.assertPathsEqual(f.dest_path, 'foo/bar.jpg')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar.jpg')
        self.assertEqual(f.url, 'foo/bar.jpg')
        self.assertEqual(f.name, 'bar')
        self.assertFalse(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertTrue(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_media_file_use_directory_urls(self):
        f = File('foo/bar.jpg', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        self.assertPathsEqual(f.src_path, 'foo/bar.jpg')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.jpg')
        self.assertPathsEqual(f.dest_path, 'foo/bar.jpg')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar.jpg')
        self.assertEqual(f.url, 'foo/bar.jpg')
        self.assertEqual(f.name, 'bar')
        self.assertFalse(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertTrue(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_javascript_file(self):
        f = File('foo/bar.js', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        self.assertPathsEqual(f.src_path, 'foo/bar.js')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.js')
        self.assertPathsEqual(f.dest_path, 'foo/bar.js')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar.js')
        self.assertEqual(f.url, 'foo/bar.js')
        self.assertEqual(f.name, 'bar')
        self.assertFalse(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertTrue(f.is_media_file())
        self.assertTrue(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_javascript_file_use_directory_urls(self):
        f = File('foo/bar.js', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        self.assertPathsEqual(f.src_path, 'foo/bar.js')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.js')
        self.assertPathsEqual(f.dest_path, 'foo/bar.js')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar.js')
        self.assertEqual(f.url, 'foo/bar.js')
        self.assertEqual(f.name, 'bar')
        self.assertFalse(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertTrue(f.is_media_file())
        self.assertTrue(f.is_javascript())
        self.assertFalse(f.is_css())

    def test_css_file(self):
        f = File('foo/bar.css', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        self.assertPathsEqual(f.src_path, 'foo/bar.css')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.css')
        self.assertPathsEqual(f.dest_path, 'foo/bar.css')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar.css')
        self.assertEqual(f.url, 'foo/bar.css')
        self.assertEqual(f.name, 'bar')
        self.assertFalse(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertTrue(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertTrue(f.is_css())

    def test_css_file_use_directory_urls(self):
        f = File('foo/bar.css', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        self.assertPathsEqual(f.src_path, 'foo/bar.css')
        self.assertPathsEqual(f.abs_src_path, '/path/to/docs/foo/bar.css')
        self.assertPathsEqual(f.dest_path, 'foo/bar.css')
        self.assertPathsEqual(f.abs_dest_path, '/path/to/site/foo/bar.css')
        self.assertEqual(f.url, 'foo/bar.css')
        self.assertEqual(f.name, 'bar')
        self.assertFalse(f.is_documentation_page())
        self.assertFalse(f.is_static_page())
        self.assertTrue(f.is_media_file())
        self.assertFalse(f.is_javascript())
        self.assertTrue(f.is_css())

    def test_files(self):
        fs = [
            File('index.md', '/path/to/docs', '/path/to/site', use_directory_urls=True),
            File('foo/bar.md', '/path/to/docs', '/path/to/site', use_directory_urls=True),
            File('foo/bar.html', '/path/to/docs', '/path/to/site', use_directory_urls=True),
            File('foo/bar.jpg', '/path/to/docs', '/path/to/site', use_directory_urls=True),
            File('foo/bar.js', '/path/to/docs', '/path/to/site', use_directory_urls=True),
            File('foo/bar.css', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        ]
        files = Files(fs)
        self.assertEqual([f for f in files], fs)
        self.assertEqual(len(files), 6)
        self.assertEqual(files.documentation_pages(), [fs[0], fs[1]])
        self.assertEqual(files.static_pages(), [fs[2]])
        self.assertEqual(files.media_files(), [fs[3], fs[4], fs[5]])
        self.assertEqual(files.javascript_files(), [fs[4]])
        self.assertEqual(files.css_files(), [fs[5]])
        self.assertEqual(files.get_file_from_path('foo/bar.jpg'), fs[3])
        self.assertEqual(files.get_file_from_path('foo/bar.jpg'), fs[3])
        self.assertEqual(files.get_file_from_path('missing.jpg'), None)
        self.assertTrue(fs[2].src_path in files)
        self.assertTrue(fs[2].src_path in files)
        extra_file = File('extra.md', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        self.assertFalse(extra_file.src_path in files)
        files.append(extra_file)
        self.assertEqual(len(files), 7)
        self.assertTrue(extra_file.src_path in files)
        self.assertEqual(files.documentation_pages(), [fs[0], fs[1], extra_file])

    def test_filter_paths(self):
        # Root level file
        self.assertFalse(_filter_paths('foo.md', 'foo.md', False, ['bar.md']))
        self.assertTrue(_filter_paths('foo.md', 'foo.md', False, ['foo.md']))

        # Nested file
        self.assertFalse(_filter_paths('foo.md', 'baz/foo.md', False, ['bar.md']))
        self.assertTrue(_filter_paths('foo.md', 'baz/foo.md', False, ['foo.md']))

        # Wildcard
        self.assertFalse(_filter_paths('foo.md', 'foo.md', False, ['*.txt']))
        self.assertTrue(_filter_paths('foo.md', 'foo.md', False, ['*.md']))

        # Root level dir
        self.assertFalse(_filter_paths('bar', 'bar', True, ['/baz']))
        self.assertFalse(_filter_paths('bar', 'bar', True, ['/baz/']))
        self.assertTrue(_filter_paths('bar', 'bar', True, ['/bar']))
        self.assertTrue(_filter_paths('bar', 'bar', True, ['/bar/']))

        # Nested dir
        self.assertFalse(_filter_paths('bar', 'foo/bar', True, ['/bar']))
        self.assertFalse(_filter_paths('bar', 'foo/bar', True, ['/bar/']))
        self.assertTrue(_filter_paths('bar', 'foo/bar', True, ['bar/']))

        # Files that look like dirs (no extension). Note that `is_dir` is `False`.
        self.assertFalse(_filter_paths('bar', 'bar', False, ['bar/']))
        self.assertFalse(_filter_paths('bar', 'foo/bar', False, ['bar/']))

    def test_get_relative_url_use_directory_urls(self):
        to_files = [
            'index.md',
            'foo/index.md',
            'foo/bar/index.md',
            'foo/bar/baz/index.md',
            'foo.md',
            'foo/bar.md',
            'foo/bar/baz.md'
        ]

        to_file_urls = [
            '.',
            'foo/',
            'foo/bar/',
            'foo/bar/baz/',
            'foo/',
            'foo/bar/',
            'foo/bar/baz/'
        ]

        from_file = File('img.jpg', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        expected = [
            'img.jpg',           # img.jpg relative to .
            '../img.jpg',        # img.jpg relative to foo/
            '../../img.jpg',     # img.jpg relative to foo/bar/
            '../../../img.jpg',  # img.jpg relative to foo/bar/baz/
            '../img.jpg',        # img.jpg relative to foo
            '../../img.jpg',     # img.jpg relative to foo/bar
            '../../../img.jpg'   # img.jpg relative to foo/bar/baz
        ]

        for i, filename in enumerate(to_files):
            file = File(filename, '/path/to/docs', '/path/to/site', use_directory_urls=True)
            self.assertEqual(from_file.url, 'img.jpg')
            self.assertEqual(file.url, to_file_urls[i])
            self.assertEqual(from_file.url_relative_to(file.url), expected[i])
            self.assertEqual(from_file.url_relative_to(file), expected[i])

        from_file = File('foo/img.jpg', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        expected = [
            'foo/img.jpg',    # foo/img.jpg relative to .
            'img.jpg',        # foo/img.jpg relative to foo/
            '../img.jpg',     # foo/img.jpg relative to foo/bar/
            '../../img.jpg',  # foo/img.jpg relative to foo/bar/baz/
            'img.jpg',        # foo/img.jpg relative to foo
            '../img.jpg',     # foo/img.jpg relative to foo/bar
            '../../img.jpg'   # foo/img.jpg relative to foo/bar/baz
        ]

        for i, filename in enumerate(to_files):
            file = File(filename, '/path/to/docs', '/path/to/site', use_directory_urls=True)
            self.assertEqual(from_file.url, 'foo/img.jpg')
            self.assertEqual(file.url, to_file_urls[i])
            self.assertEqual(from_file.url_relative_to(file.url), expected[i])
            self.assertEqual(from_file.url_relative_to(file), expected[i])

        from_file = File('index.html', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        expected = [
            '.',         # . relative to .
            '..',        # . relative to foo/
            '../..',     # . relative to foo/bar/
            '../../..',  # . relative to foo/bar/baz/
            '..',        # . relative to foo
            '../..',     # . relative to foo/bar
            '../../..'   # . relative to foo/bar/baz
        ]

        for i, filename in enumerate(to_files):
            file = File(filename, '/path/to/docs', '/path/to/site', use_directory_urls=True)
            self.assertEqual(from_file.url, '.')
            self.assertEqual(file.url, to_file_urls[i])
            self.assertEqual(from_file.url_relative_to(file.url), expected[i])
            self.assertEqual(from_file.url_relative_to(file), expected[i])

        from_file = File('file.md', '/path/to/docs', '/path/to/site', use_directory_urls=True)
        expected = [
            'file/',           # file relative to .
            '../file/',        # file relative to foo/
            '../../file/',     # file relative to foo/bar/
            '../../../file/',  # file relative to foo/bar/baz/
            '../file/',        # file relative to foo
            '../../file/',     # file relative to foo/bar
            '../../../file/'   # file relative to foo/bar/baz
        ]

        for i, filename in enumerate(to_files):
            file = File(filename, '/path/to/docs', '/path/to/site', use_directory_urls=True)
            self.assertEqual(from_file.url, 'file/')
            self.assertEqual(file.url, to_file_urls[i])
            self.assertEqual(from_file.url_relative_to(file.url), expected[i])
            self.assertEqual(from_file.url_relative_to(file), expected[i])

    def test_get_relative_url(self):
        to_files = [
            'index.md',
            'foo/index.md',
            'foo/bar/index.md',
            'foo/bar/baz/index.md',
            'foo.md',
            'foo/bar.md',
            'foo/bar/baz.md'
        ]

        to_file_urls = [
            'index.html',
            'foo/index.html',
            'foo/bar/index.html',
            'foo/bar/baz/index.html',
            'foo.html',
            'foo/bar.html',
            'foo/bar/baz.html'
        ]

        from_file = File('img.jpg', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        expected = [
            'img.jpg',           # img.jpg relative to .
            '../img.jpg',        # img.jpg relative to foo/
            '../../img.jpg',     # img.jpg relative to foo/bar/
            '../../../img.jpg',  # img.jpg relative to foo/bar/baz/
            'img.jpg',           # img.jpg relative to foo.html
            '../img.jpg',        # img.jpg relative to foo/bar.html
            '../../img.jpg'      # img.jpg relative to foo/bar/baz.html
        ]

        for i, filename in enumerate(to_files):
            file = File(filename, '/path/to/docs', '/path/to/site', use_directory_urls=False)
            self.assertEqual(from_file.url, 'img.jpg')
            self.assertEqual(file.url, to_file_urls[i])
            self.assertEqual(from_file.url_relative_to(file.url), expected[i])
            self.assertEqual(from_file.url_relative_to(file), expected[i])

        from_file = File('foo/img.jpg', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        expected = [
            'foo/img.jpg',    # foo/img.jpg relative to .
            'img.jpg',        # foo/img.jpg relative to foo/
            '../img.jpg',     # foo/img.jpg relative to foo/bar/
            '../../img.jpg',  # foo/img.jpg relative to foo/bar/baz/
            'foo/img.jpg',    # foo/img.jpg relative to foo.html
            'img.jpg',        # foo/img.jpg relative to foo/bar.html
            '../img.jpg'      # foo/img.jpg relative to foo/bar/baz.html
        ]

        for i, filename in enumerate(to_files):
            file = File(filename, '/path/to/docs', '/path/to/site', use_directory_urls=False)
            self.assertEqual(from_file.url, 'foo/img.jpg')
            self.assertEqual(file.url, to_file_urls[i])
            self.assertEqual(from_file.url_relative_to(file.url), expected[i])
            self.assertEqual(from_file.url_relative_to(file), expected[i])

        from_file = File('index.html', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        expected = [
            'index.html',           # index.html relative to .
            '../index.html',        # index.html relative to foo/
            '../../index.html',     # index.html relative to foo/bar/
            '../../../index.html',  # index.html relative to foo/bar/baz/
            'index.html',           # index.html relative to foo.html
            '../index.html',        # index.html relative to foo/bar.html
            '../../index.html'      # index.html relative to foo/bar/baz.html
        ]

        for i, filename in enumerate(to_files):
            file = File(filename, '/path/to/docs', '/path/to/site', use_directory_urls=False)
            self.assertEqual(from_file.url, 'index.html')
            self.assertEqual(file.url, to_file_urls[i])
            self.assertEqual(from_file.url_relative_to(file.url), expected[i])
            self.assertEqual(from_file.url_relative_to(file), expected[i])

        from_file = File('file.html', '/path/to/docs', '/path/to/site', use_directory_urls=False)
        expected = [
            'file.html',           # file.html relative to .
            '../file.html',        # file.html relative to foo/
            '../../file.html',     # file.html relative to foo/bar/
            '../../../file.html',  # file.html relative to foo/bar/baz/
            'file.html',           # file.html relative to foo.html
            '../file.html',        # file.html relative to foo/bar.html
            '../../file.html'      # file.html relative to foo/bar/baz.html
        ]

        for i, filename in enumerate(to_files):
            file = File(filename, '/path/to/docs', '/path/to/site', use_directory_urls=False)
            self.assertEqual(from_file.url, 'file.html')
            self.assertEqual(file.url, to_file_urls[i])
            self.assertEqual(from_file.url_relative_to(file.url), expected[i])
            self.assertEqual(from_file.url_relative_to(file), expected[i])

    @tempdir(files=[
        'index.md',
        'bar.css',
        'bar.html',
        'bar.jpg',
        'bar.js',
        'bar.md',
        '.dotfile',
        'templates/foo.html'
    ])
    def test_get_files(self, tdir):
        config = load_config(docs_dir=tdir, extra_css=['bar.css'], extra_javascript=['bar.js'])
        files = get_files(config)
        expected = ['index.md', 'bar.css', 'bar.html', 'bar.jpg', 'bar.js', 'bar.md']
        self.assertIsInstance(files, Files)
        self.assertEqual(len(files), len(expected))
        self.assertEqual([f.src_path for f in files], expected)

    @tempdir(files=[
        'README.md',
        'foo.md'
    ])
    def test_get_files_include_readme_without_index(self, tdir):
        config = load_config(docs_dir=tdir)
        files = get_files(config)
        expected = ['README.md', 'foo.md']
        self.assertIsInstance(files, Files)
        self.assertEqual(len(files), len(expected))
        self.assertEqual([f.src_path for f in files], expected)

    @tempdir(files=[
        'index.md',
        'README.md',
        'foo.md'
    ])
    def test_get_files_exclude_readme_with_index(self, tdir):
        config = load_config(docs_dir=tdir)
        files = get_files(config)
        expected = ['index.md', 'foo.md']
        self.assertIsInstance(files, Files)
        self.assertEqual(len(files), len(expected))
        self.assertEqual([f.src_path for f in files], expected)

    @tempdir()
    @tempdir(files={'test.txt': 'source content'})
    def test_copy_file(self, src_dir, dest_dir):
        file = File('test.txt', src_dir, dest_dir, use_directory_urls=False)
        dest_path = os.path.join(dest_dir, 'test.txt')
        self.assertPathNotExists(dest_path)
        file.copy_file()
        self.assertPathIsFile(dest_path)

    @tempdir(files={'test.txt': 'destination content'})
    @tempdir(files={'test.txt': 'source content'})
    def test_copy_file_clean_modified(self, src_dir, dest_dir):
        file = File('test.txt', src_dir, dest_dir, use_directory_urls=False)
        file.is_modified = mock.Mock(return_value=True)
        dest_path = os.path.join(dest_dir, 'test.txt')
        file.copy_file(dirty=False)
        self.assertPathIsFile(dest_path)
        with io.open(dest_path, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), 'source content')

    @tempdir(files={'test.txt': 'destination content'})
    @tempdir(files={'test.txt': 'source content'})
    def test_copy_file_dirty_modified(self, src_dir, dest_dir):
        file = File('test.txt', src_dir, dest_dir, use_directory_urls=False)
        file.is_modified = mock.Mock(return_value=True)
        dest_path = os.path.join(dest_dir, 'test.txt')
        file.copy_file(dirty=True)
        self.assertPathIsFile(dest_path)
        with io.open(dest_path, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), 'source content')

    @tempdir(files={'test.txt': 'destination content'})
    @tempdir(files={'test.txt': 'source content'})
    def test_copy_file_dirty_not_modified(self, src_dir, dest_dir):
        file = File('test.txt', src_dir, dest_dir, use_directory_urls=False)
        file.is_modified = mock.Mock(return_value=False)
        dest_path = os.path.join(dest_dir, 'test.txt')
        file.copy_file(dirty=True)
        self.assertPathIsFile(dest_path)
        with io.open(dest_path, 'r', encoding='utf-8') as f:
            self.assertEqual(f.read(), 'destination content')
