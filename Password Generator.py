# 📌 PASSWORD GENERATOR PROJECT FOR  MICRO IT IN GOOGLE COLAB

import random
import string
import ipywidgets as widgets
from IPython.display import display, clear_output

# 🧱 Widget inputs
length_slider = widgets.IntSlider(value=12, min=4, max=32, description='Length:')
use_uppercase = widgets.Checkbox(value=True, description='Uppercase (A-Z)')
use_lowercase = widgets.Checkbox(value=True, description='Lowercase (a-z)')
use_digits = widgets.Checkbox(value=True, description='Digits (0-9)')
use_specials = widgets.Checkbox(value=True, description='Special (!@#...)')
generate_button = widgets.Button(description="Generate Password", button_style='success')
output = widgets.Output()

# 🔑 Password generation function
def generate_password(length, use_upper, use_lower, use_digits, use_specials):
    character_pool = ''
    if use_upper:
        character_pool += string.ascii_uppercase
    if use_lower:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_specials:
        character_pool += string.punctuation

    if not character_pool:
        return "⚠️ Please select at least one character type!"
    
    return ''.join(random.choice(character_pool) for _ in range(length))

# 📌 Event handler
def on_generate_button_click(b):
    with output:
        clear_output()
        password = generate_password(length_slider.value, use_uppercase.value, use_lowercase.value,
                                     use_digits.value, use_specials.value)
        print(f"🔐 Generated Password: {password}")

# 🔄 Connect button to handler
generate_button.on_click(on_generate_button_click)

# 🎛️ Display UI
display(widgets.VBox([
    widgets.HTML("<h3>Password Generator</h3>"),
    length_slider,
    use_uppercase,
    use_lowercase,
    use_digits,
    use_specials,
    generate_button,
    output
]))
