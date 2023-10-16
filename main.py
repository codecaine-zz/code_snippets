from code_snippet_manager import CodeSnippetManager
import webview

# load index.html


def load_html(window):
    with open('index.html', 'r') as f:
        html = f.read()
        window.load_html(html)

    with open('css/w3.css', 'r') as f:
        css = f.read()

    window.load_css(css)


if __name__ == '__main__':
    window = webview.create_window('Code Snippet Manager', width=1000, height=800, resizable=True)
    webview.start(load_html, window)
