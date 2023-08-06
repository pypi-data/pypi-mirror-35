from xeno import scan_methods, MethodAttributes, ClassAttributes
import inspect
import bottle
import re

# -------------------------------------------------------------------
__all__ = (
    'route',
    'get',
    'post',
    'put',
    'delete',
    'patch',
    'error',
    'request',
    'response',
    'App'
)

# -------------------------------------------------------------------
def meta_route(router_gen):
    def decorator(*args, **kwargs):
        method = None
        if args and inspect.isfunction(args[0]):
            method = args[0]
            args = args[1:]
        def impl(method):
            attrs = MethodAttributes.for_method(method, write=True)
            attrs.put("bottleapp-route", (router_gen, args, kwargs))
            return method
        if method:
            return impl(method)
        else:
            return impl
    return decorator

# -------------------------------------------------------------------
def meta_error(router_gen):
    def decorator(*args, **kwargs):
        method = None
        if args and inspect.isfunction(args[0]):
            method = args[0]
            args = args[1:]
        def impl(method):
            attrs = MethodAttributes.for_method(method, write=True)
            attrs.put("bottleapp-error", (router_gen, args, kwargs))
            return method
        if method:
            return impl(method)
        else:
            return impl
    return decorator

# -------------------------------------------------------------------
route = meta_route(lambda app: app.route)
get = meta_route(lambda app: app.get)
post = meta_route(lambda app: app.post)
put = meta_route(lambda app: app.put)
delete = meta_route(lambda app: app.delete)
patch = meta_route(lambda app: app.patch)
error = meta_error(lambda app: app.error)
request = bottle.request
response = bottle.response

# -------------------------------------------------------------------
def parse_path_param_names(path):
    return [x[1:][:-1].split(':')[0] for x in re.findall(r"<[^>]*>", path)]

# -------------------------------------------------------------------
def resolve_method_routes(app, method, prefix = ''):
    method_attrs = MethodAttributes.for_method(method, create=True)
    router_gen, args, kwargs = method_attrs.get("bottleapp-route")
    router = router_gen(app)
    router_sig = inspect.signature(router)
    method_sig = inspect.signature(method)
    binding = router_sig.bind_partial(*args, **kwargs)
    if not 'path' in binding.arguments:
        binding.arguments["path"] = "/" + method_attrs.get("name")
    binding.arguments["path"] = prefix + binding.arguments["path"]
    path_params = parse_path_param_names(binding.arguments["path"])
    for param in method_attrs.get("params")[1:]:
        if param.name not in path_params:
            binding.arguments["path"] += "/<%s>" % param.name
    return router, binding.args, binding.kwargs

# -------------------------------------------------------------------
class App:
    def __init__(self, prefix='', parent=None):
        self._parent = parent or bottle.Bottle()
        self._multiapp_tenant = parent is not None
        self._prefix = prefix
        routed_methods = scan_methods(self, lambda attr: attr.check("bottleapp-route"))
        error_methods = scan_methods(self, lambda attr: attr.check("bottleapp-error"))
        if not routed_methods:
            raise Exception("App class '%s' contains no routed methods.  Try adding some routes." % self.__class__)
        for _, method in routed_methods:
            router, args, kwargs = resolve_method_routes(self._parent, method, self._prefix)
            router(*args, **kwargs)(method)
        for _, method in error_methods:
            method_attrs = MethodAttributes.for_method(method)
            router_gen, args, kwargs = method_attrs.get("bottleapp-error")
            router = router_gen(self._parent)
            router(*args, **kwargs)(method)
    
    def run(self, host='localhost', port=8080):
        if self._multiapp_tenant:
            raise Exception('This app cannot be started by itself because it was initialized as part of a multi-app Bottle instance.  Please run() the Bottle object this app was constructed with directly instead.')
        bottle.run(self._parent, host=host, port=port)

