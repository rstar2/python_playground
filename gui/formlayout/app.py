"""
     Example with 'formlayout' - A tiny Python module for creating form dialogs/widgets
     to edit various type of parameters with having to write any GUI code.
"""

# a little hack as have install PyQt5
# but formlayout searches the  PyQt4/ PyQt5 version from this environment variable
#  and if not set just set it here temporary
# import os
# os.environ.setdefault('QT_API', 'pyqt5')

from formlayout import fedit

datalist = [('Name', 'Paul'),
            (None, None),
            (None, 'Information:'),
            ('Age', 30),
            ('Sex', [0, 'Male', 'Female']),
            ('Size', 12.1),
            ('Eyes', 'green'),
            ('Married', True),
           ]

fedit(datalist, title="Describe yourself",
      comment="This is just an <b>example</b>.")
