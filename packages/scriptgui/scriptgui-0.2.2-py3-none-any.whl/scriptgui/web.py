import sys
from flask import Flask
from idom import component, html
from idom.backend.flask import configure, Options, use_request
from .decorator import ENDPOINTS

@component
def Navigation(_request):
    links = []
    for path in ENDPOINTS:
        links.append(
            html.li({},
                html.a({"href": path}, path)))

    return html.div({}, html.h1("Navigation", links))

@component
def App():
    request = use_request()

    def norm_path(path):
        p = path.replace("/_idom/stream","")
        if len(p) == 0:
            return "/"
        return p

    return ENDPOINTS.get(norm_path(request.path), Navigation)(request)


def main():
    print(f"Calling args: {sys.argv}")
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        load_demo()
    app = Flask(__name__)
    configure(app, App, Options(
        head=({'tagName': 'title', 'children': ['Mul-Ti']}),
        url_prefix='', cors=False))
    app.run(debug=True, host="0.0.0.0", port=8080)

def load_demo():
    from examples import basic_text

if __name__ == "__main__":
    main()