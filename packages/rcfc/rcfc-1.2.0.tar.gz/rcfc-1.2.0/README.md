# rcfc - Remote Control For Computers
Welcome to RCFC.  This is a pet project started to help out with some automation around the house.

It provides a way to write Python functions that can be exposed as buttons on a website.  There are plans to make an Android app that would automatically connect to RCFC servers and provide a UI to the user.  For now, we have to deal with a ugly website UI (if you want to spruce it up, feel free to submit a PR)

## Installing 

Just `pip install rcfc`.  Note, this is only supported by Python 3.6 and later (no legacy Python)

## There's barely any types of buttons!

So, in typical open source fashion, this is a work in progress.  Buttons will be added as time goes on, such as color-picker buttons, input buttons, toggles and more.  Write an issue if there's something you'd like to see (or submit a PR)  

## Starting the server

We run a bottle webserver underneath the hood to serve provide a REST API and provide a demo webserver.

To start the server, do the following:

```python
from rcfc import server

server.start()
```

Now if you navigate to http://\<ip-address\>:7232 you should see a simple webpage that provides a simple UI (long term plans is Android App)

## Buttons
### Simple
To get a simple push button, you just need to decorate one of your Python functions like so:

```python
from rcfc import button

@button.simple("Press Me!")
def button_has_been_pressed():
    print("This button has been pressed")
```
This will provide a pressable button with the text you provide (in this case, "Press Me!")
This is great if you want to do things like turn on/turn off something, perform a one time action, etc.

### Toggles
A toggle provides an on / off switch
```python
from rcfc import button

def get_state():
    # write your own function that returns the current state of the toggle
    return True

@button.toggle("Toggle", get_state)
def button_has_been_toggled(value):
    print(f"The value is {value}")
```

The function decorated will be passed a True/False value when the toggle is set.   There is also a getter function that reflects the correct state. 

## Other Input Methods
### Sliders

A slider provides a range of input values (such as what may be used in a dimmer)

```python
from rcfc import input_methods

def get_value():
    #write your own function that returns the current state of the slider
    return 30

@input_methods.slider("Slider Text", get_value)
def set_slider_value(value):
    print(f"The value is {value}")
```

If you need to customize the min/max (Default is 0/100), you can pass in the range as an additional argument

```python
@input_methods.slider("Slider Text", get_value, input_range=(50,60))
```

### Left/Right Arrows

A set of arrows that let you choose a left/right option

```python
from rcfc import input_methods

@input_methods.left_right_arrows("Arrows Text")
def set_arrows(value):
    print(f"The value set is {value}")
```

The value passed down will be either input_methods.DIRECTIONAL.LEFT or input_methods.DIRECTIONAL.RIGHT.

### Colorpicker

A color picker giving RGB values

```python
from rcfc import input_methods

def get_value():
    #write your own function that returns the current state of the slider
    return (30, 255, 0)

@input_methods.colorpicker("Colorpicker text", get_value)
def set_color(value):
    print(f"The value set is {value}")

```

The value set is a tuple in the form of (red, green, blue)

### Grouping Buttons

It is possible to group buttons.

You may assign a button a single group, like so: 

```python
@button.simple("Click me!", group="Group Alpha")
```

or you may assign multiple groups to the button:

```python
@button.simple("Click me!", group=["Group Alpha", "Group Omega"])
```

## Demo
There is a built-in demo if you'd like to see it in action.  Simply execute rcfc_demo on your shell (or make demo if you're in the project) and a demo server will launch on port 7232.
Open up http://localhost:7232 to see buttons that are available.  You can see the source code at [demo source code](rcfc/demo.py)

You can also check the companion GUI project, which makes it look a lot nicer.  See it [here](https://github.com/pviafore/rcfc-ionic)

## Why Bottle under the hood? Why not use Flask, Django, Pyramid, etc.?
Bottle had a very small footprint and very few dependencies.  The goal is to get this project up and going as quickly as possible.

# Useful Links

Want to contribute? Check out our [guide](CONTRIBUTING.md)

Want to write a GUI?  Check out our API docs [here](docs/api.md)
