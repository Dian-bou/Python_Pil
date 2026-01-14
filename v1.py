from PIL import Image, ImageDraw
"""
pour instaler pil cest pip install pil


view > commande pallette> python environnement
venv , choisir python, fermer terminal et re ouvrir pour avoir .venv
venv vert premeir mot 
pil -> pillow




"""

# create new image
ima = Image.new("RGBA", (400, 800), "white")

draw = ImageDraw.Draw(ima)
print(ima.size)
draw.line((0, 0) + ima.size, fill="black")
draw.line((0, ima.size[1], ima.size[0], 0), fill="green")

draw.ellipse((100, 100, 300, 300), fill="blue", outline="red")



ima.show("My new image")