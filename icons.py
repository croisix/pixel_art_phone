from pathlib import Path

# Fonction retournant un tab: lien des images
def getAllApps():
    res =[]
    p = Path('static/images/icons')
    files = p.rglob('*.png')
    for f in files:
        res.append(f"{f.stem}")
    return res
    
# Fonction retournant un entier: nbm d'images
def getCountApps():
    res=0
    p = Path('static/images/icons')
    files = p.rglob('*.png')
    for f in files:
        res+=1
    return res

print(getAllApps())
