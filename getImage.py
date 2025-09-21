from pathlib import Path

# Fonction retournant un tab: lien des images
def getImages(path):
    res =[]
    p = Path(path)
    files = p.rglob('*.png')
    for f in files:
        res.append(f"{f.stem}")
    return res