from idom import component, html

ENDPOINTS = {}

def text_widget(text_supplier, *args):
    return html.h1(text_supplier())

WIDGETS = {
    'Text': text_widget,
}

class BaseWidget:
    def __init__(self):
        self.elements = []
    
    def append(self, element):
        self.elements.append(element)

    def __call__(self, _request):
        return html.div(self.elements)

def build_widget(props, func, *args):
    typ = props['type']
    if typ not in WIDGETS:
        raise ValueError(f"Unknown widget type: {typ}")
    return component(lambda: WIDGETS[typ](func, *args))()

def sgui(path, props, *args, **kwargs):
    """Decorator to register a scriptgui endpoint from a function."""
    if path not in ENDPOINTS:
        ENDPOINTS[path] = BaseWidget()
    
    def inner(func):
        print(f"Registering {path} with props [{props}], function [{func}], and args [{args}]")
        widget = build_widget(props, func, *args)
        ENDPOINTS[path].append(widget)
        return func
    return inner