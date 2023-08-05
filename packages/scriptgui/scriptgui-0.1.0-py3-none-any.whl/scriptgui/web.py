from flask import Flask
from idom import component, html
from idom.backend.flask import configure, Options, use_request

@component
def NotFound(_request):
    return html.h1("404")

@component
def Tools(_request):
    return html.h1("Tools")

@component
def App():
    request = use_request()

    ROUTES = {
        "/": Tools,
    }

    def norm_path(path):
        p = path.replace("/_idom/stream","")
        if len(p) == 0:
            return "/"
        return p

    return ROUTES.get(norm_path(request.path), NotFound)(request)


app = Flask(__name__)
configure(app, App, Options(
    head=({'tagName': 'title', 'children': ['Mul-Ti']}),
    url_prefix='', cors=False))


def main():
    app.run(debug=True, host="0.0.0.0", port=8080)

if __name__ == "__main__":
    main()