from setuptools import setup
__VERSION__='0.8.1'

packages=['pyjs', 'pyjs.builtin', 'pyjs.lib', 'pyjs.lib.logging', 'pyjs.lib.os', 'pyjs.lib.test',
          'pyjs.lib_trans', 'pyjs.lib_trans.pycompiler', 'pyjs.lib_trans.pyparser', 'pyjs.lib_trans.test',
          'pyjs.boilerplate',
          'pgen', 'pgen.lib2to3', 'pgen.lib2to3.pgen2', 'pgen.lib2to3.compiler', ]
package_data={'pyjs': ['boilerplate/*.html', 'boilerplate/pyjampiler_wrapper.js.tmpl',
                       'builtin/__builtin__.py.in', 'builtin/public/*.js',
                       'contrib/compiler.jar'],
              }
entry_points = {'console_scripts':[
    'pyjampiler=pyjs.pyjampiler:pyjampiler',
    'pyjscompile=pyjs.translator:main',
    'pyjsbuild=pyjs.browser:build_script',
    'pyv8run=pyjs.pyv8.pyv8run:main',
    'pyjstest=pyjs.pyjstest:pyjstest',
    'java2py=pyjs.contrib.java2py:main',
    'mo2json=pyjs.contrib.mo2json:main',
    'pyjscompressor=pyjs.contrib.pyjscompressor:main',
]}

# setup(
#     name="pyjs_tools",
#     version=__VERSION__,
#     packages=packages,
#     package_data=package_data,
#     zip_safe = False,
#     install_requires = install_requires,
#     entry_points = entry_points,
#     )
