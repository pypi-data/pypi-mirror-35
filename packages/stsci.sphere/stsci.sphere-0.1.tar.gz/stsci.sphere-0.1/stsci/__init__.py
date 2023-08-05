# This is a special __init__.py required to place sample_package under the
# stsci namespace package.  There should be no other code in this module.
try:
    from pkg_resources import declare_namespace
    declare_namespace(__name__)
except ImportError:
    from pkgutil import extend_path
    __path__ = extend_path(__path__, __name__)
