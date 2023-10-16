import os
import pytest
from code_snippet_manager import CodeSnippetManager


@pytest.fixture
def snippet_manager():
    """Fixture to create a CodeSnippetManager instance for testing."""
    filename = 'test_snippets.db'
    manager = CodeSnippetManager(filename)
    yield manager
    os.remove(filename)


def test_add_snippet(snippet_manager):
    """Test adding a new snippet."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')
    snippets = snippet_manager.list_snippets()
    assert len(snippets) == 1
    assert snippets[0]['language'] == 'Python'
    assert snippets[0]['title'] == 'Hello World'
    assert snippets[0]['code'] == 'print("Hello, World!")'
    assert snippets[0]['category'] == 'Getting Started'
    assert snippets[0]['additional_info'] == 'A simple program to print "Hello, World!"'


def test_read_snippet(snippet_manager):
    """Test reading a snippet by its ID."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')
    snippet = snippet_manager.read_snippet(1)
    assert snippet is not None
    assert snippet['language'] == 'Python'
    assert snippet['title'] == 'Hello World'
    assert snippet['code'] == 'print("Hello, World!")'
    assert snippet['category'] == 'Getting Started'
    assert snippet['additional_info'] == 'A simple program to print "Hello, World!"'


def test_update_snippet(snippet_manager):
    """Test updating a snippet by its ID."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')
    snippet_manager.update_snippet(
        1, title='Hello, World!', code='print("Hello, World!")')
    snippet = snippet_manager.read_snippet(1)
    assert snippet is not None
    assert snippet['language'] == 'Python'
    assert snippet['title'] == 'Hello, World!'
    assert snippet['code'] == 'print("Hello, World!")'
    assert snippet['category'] == 'Getting Started'
    assert snippet['additional_info'] == 'A simple program to print "Hello, World!"'


def test_delete_snippet(snippet_manager):
    """Test deleting a snippet by its ID."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')
    assert snippet_manager.delete_snippet(1)
    snippets = snippet_manager.list_snippets()
    assert len(snippets) == 0


def test_delete_all_snippets(snippet_manager):
    """Test deleting all the snippets."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Simple', 'A simple program to print "Hello, World!"')
    assert snippet_manager.delete_all_snippets()
    snippets = snippet_manager.list_snippets()
    assert len(snippets) == 0


def test_list_snippets(snippet_manager):
    """Test listing all the snippets."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')
    snippets = snippet_manager.list_snippets()
    print(snippets)
    assert len(snippets) == 1


def test_snippet_exists(snippet_manager):
    """Test checking if a snippet exists."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')
    assert snippet_manager.snippet_exists(
        'Python', 'Hello World', 'Getting Started')
    assert not snippet_manager.snippet_exists(
        'Python', 'Hello World', 'Advanced')


def test_get_languages(snippet_manager):
    """Test getting a list of all the languages."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')
    snippet_manager.add_snippet('Javascript', 'Hello World', 'console.log("Hello, World!")',
                                'Simple', 'A simple program to print "Hello, World!"')

    languages = snippet_manager.get_languages()
    print(languages)
    assert len(languages) == 2
    assert 'Python' in languages
    assert 'Javascript' in languages


def test_get_categories(snippet_manager):
    """Test getting a list of all the categories."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Simple', 'A simple program to print "Hello, World!"')

    categories = snippet_manager.get_categories()
    print(categories)
    assert len(categories) == 2
    assert 'Getting Started' in categories
    assert 'Simple' in categories


def test_get_snippets_by_language(snippet_manager):
    """Test getting a list of all the snippets by language."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')

    snippets = snippet_manager.get_snippets_by_language('Python')
    print(snippets)
    assert len(snippets) == 1
    assert snippets[0]['language'] == 'Python'
    assert snippets[0]['title'] == 'Hello World'
    assert snippets[0]['code'] == 'print("Hello, World!")'
    assert snippets[0]['category'] == 'Getting Started'
    assert snippets[0]['additional_info'] == 'A simple program to print "Hello, World!"'

    snippets = snippet_manager.get_snippets_by_language('Javascript')
    print(snippets)
    assert len(snippets) == 0


def test_get_snippets_by_category(snippet_manager):
    """Test getting a list of all the snippets by category."""
    snippet_manager.add_snippet('Python', 'Hello World', 'print("Hello, World!")',
                                'Getting Started', 'A simple program to print "Hello, World!"')

    snippets = snippet_manager.get_snippets_by_category('Getting Started')
    print(snippets)
    assert len(snippets) == 1
    assert snippets[0]['language'] == 'Python'
    assert snippets[0]['title'] == 'Hello World'
    assert snippets[0]['code'] == 'print("Hello, World!")'
    assert snippets[0]['category'] == 'Getting Started'
    assert snippets[0]['additional_info'] == 'A simple program to print "Hello, World!"'

    snippets = snippet_manager.get_snippets_by_category('Simple')
    print(snippets)
    assert len(snippets) == 0
