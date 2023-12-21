import sys
if "pyodide" in sys.modules:
    import piplite
    await piplite.install('pyb2d-jupyterlite-backend>=0.4.2')
