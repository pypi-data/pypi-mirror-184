# Finds the best fitting text size for a bounding box

```python
# Tested with:
# Python 3.9.13
# Windows 10

pip install cv2-fit-text-in-box

from cv2_fit_text_in_box import fit_text_in_box
text = """Eins, zwei, drei, vier, fünf, 
sechs, sieben, acht, neun, aus!
Alle warten auf das Licht.
Fürchtet euch, fürchtet euch nicht!
Die Sonne scheint mir aus den Augen,
sie wird heut Nacht nicht untergehen,
und die Welt zählt laut bis zehn.
Eins, hier kommt die Sonne.
Zwei, hier kommt die Sonne.
Drei, sie ist der hellste Stern von allen.
Vier, hier kommt die Sonne.
Die Sonne scheint mir aus den Händen,
kann verbrennen, kann euch blenden,
wenn sie aus den Fäusten bricht,
legt sich heiß auf dein Gesicht,
legt sich schmerzend auf die Brust,
das Gleichgewicht wird zum Verlust,
lässt dich hart zu Boden gehen,
und die Welt zählt laut bis zehn.
Eins, hier kommt die Sonne.
Zwei, hier kommt die Sonne.
Drei, sie ist der hellste Stern von allen,
vier, und wird nie vom Himmel fallen.
Fünf, hier kommt die Sonne.
Sechs, hier kommt die Sonne.
Sieben, sie ist der hellste Stern von allen.
Acht, neun, hier kommt die Sonne.
"""

fertig = fit_text_in_box(
    text,
    textcolor=[(255, 255, 0), (0, 0, 0)],
    backgroundcolor=[(0, 0, 150), (0, 110, 0)],
    transparent=True,
    filepath="f:\\testpicture1.png",
    maximalx=1280,
    maximaly=420,
    columns=2,
    fontart="arial.ttf",
    fontborder=2,
    distance_upper_left=(1, 1),
)
```
<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/testpicture1.png"/>




```python

fertig = fit_text_in_box(
    text,
    textcolor=[(255, 0, 0)],
    backgroundcolor=[(50, 50, 0), (30, 30, 0), (10, 0, 0)],
    transparent=False,
    filepath="f:\\testpicture3.png",
    maximalx=720,
    maximaly=720,
    columns=1,
    fontart="arial.ttf",
    fontborder=2,
    distance_upper_left=(1, 1),
)

```
<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/testpicture3.png"/>


```python

fertig = fit_text_in_box(
    text,
    textcolor=[(255, 255, 0)],
    backgroundcolor=[(0, 0, 150), (0, 0, 0)],
    transparent=True,
    filepath="f:\\testpicture4.png",
    maximalx=1280,
    maximaly=720,
    columns=3,
    fontart="arial.ttf",
    fontborder=2,
    distance_upper_left=(1, 1),
)



```


<img src="https://raw.githubusercontent.com/hansalemaos/screenshots/main/testpicture4.png"/>

