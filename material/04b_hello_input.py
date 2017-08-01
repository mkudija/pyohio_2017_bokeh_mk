# widget documentation:
# http://bokeh.pydata.org/en/latest/docs/user_guide/interaction/widgets.html#select

# 0. imports
from bokeh.io import curdoc
from bokeh.layouts import column
from bokeh.models.widgets import TextInput, Button, Paragraph, Select

# 1. create some widgets
title = Paragraph()
title.text = 'Name Selector'
button = Button(label="Say HI")
input = TextInput(value="Bokeh")
output = Paragraph()

# 2. add a callback to a widget
def update():
    output.text = "Hello, " + input.value
button.on_click(update)

# 3. create a layout for everything
layout = column(button, input, output)

# 4. add the layout to curdoc
curdoc().add_root(layout)