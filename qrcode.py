import qrcode
import pygame as pg
import time as t

uip="abcd"
name="mohan"
amount=1234
c="Inr"
data=f"upi://pa={uip},name={name},amount={amount},c={c}"
qr = qrcode.QRCode(version=1,error_correction=2,box_size=10,border=4)
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("qr.png")
print("qr.png")

pg.init()
pg.display.set_caption("qrcode")
p=pg.display.set_mode((450,450))
p1=pg.image.load("qr.png")
p.blit(p1,(0,0))
pg.display.update()
t.sleep(3)
pg.quit()







