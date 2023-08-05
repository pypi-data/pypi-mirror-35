from .views import *

import importlib


def datatable_manager(request):
    """
    Return the json data for a datatable
    """
    module_name = request.GET.get("module")
    name = request.GET.get("name")
    if not module_name or not name:
        return None
    module = importlib.import_module(module_name)
    cls = getattr(module, name)
    instance = cls()
    instance.request = request
    view_method = instance.dispatch
    return view_method(request)
