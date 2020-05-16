from tkinter import *
from PIL import ImageTk, Image
import datetime
d1=datetime.datetime.today().strftime("%d/%m/%Y")
# d1 = today.strftime("%d/%m/%Y")
def every_100(text):
    final_text=""
    for i in range(0,len(text)):
        final_text+=text[i]
        if i%100==0 and i!=0:
            final_text+="\n"
    return final_text
root=Tk()
root.geometry("1000x100")
texts=[]
photos=[]
for i in range(0,4):
    with open(f"{i+1}.txt") as f:
        text=f.read()
        texts.append(every_100(text))
    image=Image.open(f"{i+1}.jpg")
    #TODO:resize images
    image=image.resize((255, 265), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))
f0=Frame(root, width=800, height=70)
Label(f0, text="Today's News", font="lucida 33 bold").pack()
Label(f0, text=f"{d1}", font="lucida 33 bold").pack()
f0.pack()
f1=Frame(root, width=900, height=200, pady=14)
Label(f1, text=texts[1], padx=22, pady=22).pack(side="left")
Label(f1, image=photos[1], anchor="e").pack()
f1.pack(anchor="w", fill="both")
f2=Frame(root, width=900, height=200, pady=14)
Label(f2, text=texts[2], padx=22, pady=22).pack(side="right")
Label(f2, image=photos[2], anchor="e").pack()
f2.pack(anchor="w", fill="both")
f3=Frame(root, width=900, height=200, pady=14)
Label(f3, text=texts[3], padx=22, pady=22).pack(side="left")
Label(f3, image=photos[3], anchor="e").pack()
f3.pack(anchor="w",fill="both")
# f4=Frame(root, width=900, height=200, pady=14)
# Label(f4, text=texts[4], padx=22, pady=22).pack(side="right")
# Label(f4, image=photos[4], anchor="e").pack()
# f4.pack(anchor="w", fill="both")
root.mainloop()