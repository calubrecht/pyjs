from setuptools import setup
__VERSION__='0.8.1'

packages=['pyjswidgets', 'pyjswidgets.pyjamas',
          'pyjswidgets.pyjamas.Canvas', 'pyjswidgets.pyjamas.builder',
          'pyjswidgets.pyjamas.chart', 'pyjswidgets.pyjamas.django',
          'pyjswidgets.pyjamas.dnd', 'pyjswidgets.pyjamas.feed',
          'pyjswidgets.pyjamas.gears', 'pyjswidgets.pyjamas.gears.database',
          'pyjswidgets.pyjamas.gears.localserver', 'pyjswidgets.pyjamas.gears.workerpool',
          'pyjswidgets.pyjamas.gmaps', 'pyjswidgets.pyjamas.graphael', 
          'pyjswidgets.pyjamas.logging', 'pyjswidgets.pyjamas.media', 
          'pyjswidgets.pyjamas.raphael', 'pyjswidgets.pyjamas.selection', 
          'pyjswidgets.pyjamas.ui', 'pyjswidgets.pyjamas.ui.public',
          'pyjswaddons',
          ]
package_data={'pyjswidgets': ['*.js',],
              'pyjswidgets/pyjamas/ui': ['public/*.html', 'public/css.d/*.css', 
                                            'public/images/*.png', 'public//images/*.gif'],
              }
entry_points = {}

# setup(
#     name="pyjs_pyjamas",
#     version=__VERSION__,
#     packages=packages,
#     package_data=package_data,
#     entry_points=entry_points,
#     zip_safe = False,
#     )
