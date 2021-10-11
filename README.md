# Imoji
A emoji lib for image manipulation which works with pillow library.

by Caio Madeira
___

### Install:

> pip install imoji

### Usage:

Instantiate the main class and pass the text thats you want to get the emoji.  

obs: The debug parameter is not obrigatory. You can set this parameter as True  
to see logs.
```
emoji = Imoji(text="This is a test 🤡", debug=False)
```

To draw this unicode, you can call the method **drawUnicode**

```
img = emoji.drawUnicode()
```

You can paste in any new img

```
emoji.pasteUnicode(emoji_im=im2, foreground=background, posX=10, posY=500)
```

**This is my first python package**