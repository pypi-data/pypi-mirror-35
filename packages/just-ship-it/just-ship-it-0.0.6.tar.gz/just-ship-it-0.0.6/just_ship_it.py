import hashlib
import importlib
import inspect
import os
import sys
from datetime import datetime
from functools import wraps
from inspect import signature

from flask import Flask, request
from flask_restplus import Resource, Api, fields

from flask_ngrok import run_with_ngrok


def ship_it():
    app = Flask(__name__)
    run_with_ngrok(app)
    app.config.SWAGGER_UI_DOC_EXPANSION = 'list'
    app.config.SWAGGER_UI_REQUEST_DURATION = True

    hostfile = sys.argv[0]
    is_running_in_notebook = 'ipykernel_launcher.py' in hostfile

    hash = hashlib.md5(open(hostfile, 'rb').read()).hexdigest()
    filename = os.path.basename(hostfile)
    api = Api(app, version=hash, title=f'{filename} API',
              description=f'API for {filename} as of {datetime.now()}', ordered=True)

    # ns = api.namespace('functions', description='Call these')
    # utility namespace? for dumping files etc?

    def call_with_request_data(f):
        @wraps(f)
        def wrapper(self):  # Discards the self passed in
            data = request.get_json(force=True)
            return f(*[v for k, v in data.items()])

        return wrapper

    def make_class(name, f):
        function_with_input = call_with_request_data(f)
        new_class = type(name, (Resource,), {
            "post": function_with_input,
        })
        return new_class

    def add_resource(name, f):
        resource = make_class(name, f)
        api.route(f'/{name}', methods=['POST'])(resource)
        parameter_names = f.__code__.co_varnames
        # TODO: default values, example values, args, kwargs
        # TODO: See how fire gets parameter types etc https://flask-restplus.readthedocs.io/en/stable/swagger.html#documenting-the-fields
        # TODO: use api.param? or keep all in json? query params have size limits but are bookmarkable, but I guess
        # TODO: autogen a requests script to query server from python?
        # TODO: Validation
        # TODO: Better error messages, see fire trace @api.response(404, 'User not found.') api.abort(404)
        # TODO: working with file uploads?
        # TODO: Hot reloading???
        # TODO: Use type hints to guess field type if available
        # TODO: Use return doc to specify output shape @api.marshal_with(model) for output shape

        sig = signature(f)
        model = api.model(f'{name}_parameters', {n: fields.String(required=True, example=f"<{n}>") for n in parameter_names})
        api.doc(description=str(sig), body=model)(resource)

    if is_running_in_notebook:
        calling_module = sys.modules['__main__']
    else:
        calling_module = importlib.import_module(os.path.basename(hostfile)[:-3])
    functions = inspect.getmembers(calling_module, inspect.isfunction)
    for fn_name, fn in functions:
        if os.path.basename(fn.__code__.co_filename) == os.path.basename(hostfile)\
                or (is_running_in_notebook and '<ipython-input' in str(fn.__code__.co_filename)):
            add_resource(fn_name, fn)
    app.run()
