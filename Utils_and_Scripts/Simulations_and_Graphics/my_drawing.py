"""
File: my_drawing.py
Name: Alan
----------------------
This program generates a graphical portrait of the character
Nick Wilde from Disney's "Zootopia".

It utilizes the campy graphics library to assembly the image
using layered geometric objects, including polygons, arcs,
and ovals, to create facial features and clothing details.
"""

from campy.graphics.gobjects import GOval, GLine, GArc, GPolygon, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Zootopia!! Nick Wilde

    This is Nick Wilde, the main character of Zootopia.
    Zootopia 2 is my favorite Disney movie of 2025
    I hope you guys like it too!! I highly recommend watching it.
    """
    window = GWindow(800, 800, title='zootopia')

    # Background part
    background = GPolygon()
    background.add_vertex((0, 800))
    background.add_vertex((800, 800))
    background.add_vertex((800, 70))
    background.add_vertex((0, 120))
    background.filled = True
    background.fill_color = '#FFC498'
    window.add(background, x=0, y=300)

    background2 = GPolygon()
    background2.add_vertex((0, 0))
    background2.add_vertex((0, 420))
    background2.add_vertex((800, 370))
    background2.add_vertex((800, 0))
    window.add(background2)

    # Text part
    offsets = [(-1, -1), (-1, 1), (1, -1), (1, 1), (-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in offsets:
        shadow = GLabel('ZOOTOPIA', x=20 + dx, y=120 + dy)
        shadow.font = '-50-bold'
        shadow.color = 'black'
        window.add(shadow)

    headline = GLabel('ZOOTOPIA', x=20, y=120)
    headline.font = '-50-bold'
    headline.color = 'white'
    window.add(headline)

    # Face part
    face = GArc(300, 800, 0, 180)
    face.filled = True
    face.fill_color = '#FC6D42'
    face.color = '#FC6D42'
    window.add(face, x=400, y=200)

    # Ears part
    left_ear = GPolygon()
    left_ear.add_vertex((410, 320))
    left_ear.add_vertex((500, 210))
    left_ear.add_vertex((370, 80))
    left_ear.filled = True
    left_ear.fill_color = '#FC6D42'
    left_ear.color = '#FC6D42'
    window.add(left_ear)

    left_in_ear = GPolygon()
    left_in_ear.add_vertex((410, 320))
    left_in_ear.add_vertex((450, 200))
    left_in_ear.add_vertex((380, 100))
    left_in_ear.filled = True
    left_in_ear.fill_color = '#FEC290'
    left_in_ear.color = '#FEC290'
    window.add(left_in_ear)

    right_ear = GPolygon()
    right_ear.add_vertex((550, 200))
    right_ear.add_vertex((650, 250))
    right_ear.add_vertex((620, 80))
    right_ear.filled = True
    right_ear.fill_color = '#FC6D42'
    right_ear.color = '#FC6D42'
    window.add(right_ear)

    right_in_ear = GPolygon()
    right_in_ear.add_vertex((625, 235))
    right_in_ear.add_vertex((650, 250))
    right_in_ear.add_vertex((620, 80))
    right_in_ear.filled = True
    right_in_ear.fill_color = '#FEC290'
    right_in_ear.color = '#FEC290'
    window.add(right_in_ear)

    # Left arm part
    left_arm = GPolygon()
    left_arm.add_vertex((160, 120))
    left_arm.add_vertex((100, 130))
    left_arm.add_vertex((200, 300))
    left_arm.add_vertex((150, 370))
    left_arm.add_vertex((160, 380))
    left_arm.add_vertex((320, 380))
    left_arm.filled = True
    left_arm.fill_color = '#4C0206'
    window.add(left_arm, x=220, y=400)

    # Left hand part

    left_hand1 = GArc(50, 200, 200, -170)
    left_hand1.filled = True
    left_hand1.fill_color = '#670302'
    window.add(left_hand1, x=353, y=710)

    left_hand2 = GArc(40, 200, 200, -170)
    left_hand2.filled = True
    left_hand2.fill_color = '#29191A'
    window.add(left_hand2, x=360, y=710)

    left_hand3 = GArc(20, 80, 200, -170)
    left_hand3.filled = True
    left_hand3.fill_color = '#29191A'
    window.add(left_hand3, x=390, y=712)

    left_hand4 = GOval(5, 5)
    left_hand4.filled = True
    window.add(left_hand4, x=375, y=706)

    left_hand5 = GOval(5, 5)
    left_hand5.filled = True
    window.add(left_hand5, x=396, y=708)

    # Right arm part
    right_arm = GPolygon()
    right_arm.add_vertex((100, 130))
    right_arm.add_vertex((284, 32))
    right_arm.add_vertex((110, 70))
    right_arm.filled = True
    right_arm.fill_color = '#670302'
    window.add(right_arm, x=370, y=590)

    # Table
    table = GPolygon()
    table.add_vertex((300, 800))
    table.add_vertex((800, 800))
    table.add_vertex((800, 700))
    table.add_vertex((700, 600))
    table.filled = True
    table.fill_color = 'saddlebrown'
    window.add(table)

    # Eye part
    l_eye = GArc(90, 130, 180, 180)
    l_eye.filled = True
    l_eye.fill_color = 'white'
    window.add(l_eye, x=470, y=330)

    l_eye_circle1 = GOval(35, 35)
    l_eye_circle1.filled = True
    l_eye_circle1.fill_color = 'green'
    window.add(l_eye_circle1, x=517, y=350)

    l_eye_circle2 = GOval(28, 28)
    l_eye_circle2.filled = True
    l_eye_circle2.fill_color = 'black'
    window.add(l_eye_circle2, x=520, y=351)

    l_eye_circle3 = GOval(5, 5)
    l_eye_circle3.filled = True
    l_eye_circle3.fill_color = 'white'
    window.add(l_eye_circle3, x=522, y=365)

    l_eyelid = GArc(90, 200, 0, 180)
    l_eyelid.filled = True
    l_eyelid.fill_color = '#922F1E'
    window.add(l_eyelid, x=470, y=311.5)

    r_eye = GArc(70, 130, 180, 180)
    r_eye.filled = True
    r_eye.fill_color = 'white'
    window.add(r_eye, x=600, y=330)

    r_eye_circle1 = GOval(35, 35)
    r_eye_circle1.filled = True
    r_eye_circle1.fill_color = 'green'
    window.add(r_eye_circle1, x=605, y=350)

    r_eye_circle2 = GOval(26, 26)
    r_eye_circle2.filled = True
    r_eye_circle2.fill_color = 'black'
    window.add(r_eye_circle2, x=610, y=353)

    r_eye_circle3 = GOval(5, 5)
    r_eye_circle3.filled = True
    r_eye_circle3.fill_color = 'white'
    window.add(r_eye_circle3, x=610, y=365)

    r_eyelid = GArc(70, 180, 0, 180)
    r_eyelid.filled = True
    r_eyelid.fill_color = '#922F1E'
    window.add(r_eyelid, x=600, y=318)

    l_eyebrow = GPolygon()
    l_eyebrow.add_vertex((100, 150))
    l_eyebrow.add_vertex((115, 135))
    l_eyebrow.add_vertex((140, 130))
    l_eyebrow.add_vertex((165, 140))
    l_eyebrow.add_vertex((180, 155))

    l_eyebrow.add_vertex((160, 150))
    l_eyebrow.add_vertex((135, 145))
    l_eyebrow.add_vertex((100, 150))
    l_eyebrow.filled = True
    l_eyebrow.fill_color = '#510401'
    window.add(l_eyebrow, x=490, y=120)

    r_eyebrow = GPolygon()
    r_eyebrow.add_vertex((180, 120))
    r_eyebrow.add_vertex((130, 120))
    r_eyebrow.add_vertex((90, 140))

    r_eyebrow.add_vertex((120, 135))
    r_eyebrow.add_vertex((180, 130))
    r_eyebrow.filled = True
    r_eyebrow.fill_color = '#510401'
    window.add(r_eyebrow, x=370, y=140)

    # Clothes part
    clothes = GPolygon()
    clothes.add_vertex((130, 200))
    clothes.add_vertex((90, 210))
    clothes.add_vertex((80, 170))
    clothes.add_vertex((85, 120))
    clothes.add_vertex((170, 110))
    clothes.add_vertex((180, 150))
    clothes.add_vertex((200, 170))
    clothes.add_vertex((240, 170))
    clothes.add_vertex((260, 150))
    clothes.add_vertex((320, 100))
    clothes.add_vertex((350, 110))
    clothes.add_vertex((380, 250))
    clothes.add_vertex((210, 290))
    clothes.add_vertex((190, 350))
    clothes.add_vertex((140, 370))
    clothes.filled = True
    clothes.fill_color = '#D1BC4F'
    window.add(clothes, x=280, y=370)

    necktie = GPolygon()
    necktie.add_vertex((85, 85))
    necktie.add_vertex((120, 130))
    necktie.add_vertex((110, 220))
    necktie.add_vertex((150, 210))
    necktie.add_vertex((140, 130))
    necktie.add_vertex((150, 100))
    necktie.add_vertex((120, 100))
    necktie.add_vertex((100, 100))
    necktie.filled = True
    necktie.fill_color = 'midnightblue'

    window.add(necktie, x=380, y=440)

    # Collar part
    collar = GPolygon()
    collar.add_vertex((150, 110))
    collar.add_vertex((135, 150))
    collar.add_vertex((150, 220))
    collar.add_vertex((175, 145))
    window.add(collar, x=300, y=370)

    collar2 = GPolygon()
    collar2.add_vertex((210, 90))
    collar2.add_vertex((135, 150))
    collar2.add_vertex((150, 220))
    collar2.add_vertex((165, 200))
    window.add(collar2, x=400, y=370)

    # muzzle part
    muzzle = GPolygon()
    muzzle.add_vertex((90, 100))
    muzzle.add_vertex((120, 160))
    muzzle.add_vertex((80, 220))
    muzzle.add_vertex((100, 240))
    muzzle.add_vertex((141, 240))
    muzzle.add_vertex((220, 168))
    muzzle.add_vertex((250, 180))
    muzzle.add_vertex((275, 150))
    muzzle.add_vertex((320, 100))
    muzzle.add_vertex((250, 110))
    muzzle.add_vertex((240, 150))
    muzzle.add_vertex((210, 150))
    muzzle.add_vertex((180, 110))
    muzzle.filled = True
    muzzle.fill_color = '#FFC79F'
    window.add(muzzle, x=380, y=300)

    # Cheek part
    cheek = GPolygon()
    cheek.add_vertex((100, 100))
    cheek.add_vertex((150, 130))
    cheek.add_vertex((150, 180))
    cheek.add_vertex((159, 220))
    cheek.add_vertex((200, 157))
    cheek.add_vertex((170, 100))
    cheek.filled = True
    cheek.fill_color = '#FC6D42'
    cheek.color = '#FC6D42'
    window.add(cheek, x=300, y=300)

    # Philtrum part
    philtrum = GPolygon()
    philtrum.add_vertex((50, 90))
    philtrum.add_vertex((140, 100))
    philtrum.add_vertex((160, 130))
    philtrum.add_vertex((200, 130))
    philtrum.add_vertex((210, 100))
    philtrum.add_vertex((280, 90))
    philtrum.filled = True
    philtrum.fill_color = '#FC6D42'
    philtrum.color = '#FC6D42'
    window.add(philtrum, x=420, y=310)

    # Nose part
    nose = GOval(50, 30)
    nose.filled = True
    nose.fill_color = '#8F6C83'
    window.add(nose, x=580, y=430)

    nose1 = GOval(40, 20)
    nose1.filled = True
    nose1.fill_color = '#2C0F14'
    window.add(nose1, x=590, y=435)

    # Mouth part
    mouth = GArc(450, 200, 180, 90)
    mouth.filled = False
    window.add(mouth, x=510, y=368)

    mouth1 = GLine(600, 460, 600, 470)
    window.add(mouth1)

    # Nick name
    for dx, dy in offsets:
        shadow2 = GLabel('Nick Wilde', x=550 + dx, y=750 + dy)
        shadow2.font = '-30-bold'
        shadow2.color = 'black'
        window.add(shadow2)

    nickname = GLabel('Nick Wilde', x=550, y=750)
    nickname.font = '-30-bold'
    nickname.color = 'white'
    window.add(nickname)


if __name__ == '__main__':
    main()
