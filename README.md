# pyfiglet-banner

A simple Python script that converts text into stylish ASCII banners using the **pyfiglet** library. Perfect for terminal aesthetics, scripts, or just for fun! 🎨💻

## 🔥 Features
- Convert any text into an ASCII banner instantly
- Supports multiple fonts for customization
- Lightweight and easy to use
- Great for enhancing terminal scripts

## 🚀 Installation
Make sure you have Python installed, then install the required library:
```bash
pip install pyfiglet
```

## 🎯 Usage
Run the script and enter any text:
```bash
python pyfiglet-banner.py
```
Example output:
```
Enter your text here: Hello
 _   _      _ _  
| | | |    | | |
| |_| | ___| | | ___
|  _  |/ _ \ | |/ _ \
| | | |  __/ | | (_) |
\_| |_/\___|_|_|\___/
```

## 🛠 Customization
You can modify the font by changing this line in the script:
```python
ascii_art = pyfiglet.figlet_format(text, font="slant")
```
To see available fonts, run:
```python
import pyfiglet
print(pyfiglet.getFonts())
```


