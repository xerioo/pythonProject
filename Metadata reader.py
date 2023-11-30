import os
from moviepy.editor import *
from path import *
from ffprobe import FFProbe

def gyujtsd_ossze_metaadatokat(mappa_ut):
    metaadatok_lista = []

    # Ellenőrizzük a mappa létezését
    if not os.path.exists(mappa_ut):
        print(f"A mappa nem található: {mappa_ut}")
        return

    # Az összes fájl listázása a mappában
    for fajlnev in os.listdir(mappa_ut):
        fajl_ut = mappa_ut+"/"+fajlnev

        # Ellenőrizze, hogy a fájl egy .mov vagy .mp4 kiterjesztésű videófájl-e
        if os.path.isfile(fajl_ut) and fajlnev.lower().endswith(('.mov', '.mp4')):
            # Videó klip létrehozása a fájlból
            clip = VideoFileClip(fajl_ut)
            metada2 = FFProbe(fajl_ut)
            for key, value in metada2.all().items():
                print(f"{key}: {value}")
            # Metaadatok kinyerése
            metaadatok = {
                "Fájlnév": fajlnev,
 #               "Cím": clip.title,
 #               "Készítette": clip.creator,
 #               "Fájlformátum": clip.fmt,
                "Képkockasebesség": clip.fps,
                "Képkockák száma": clip.reader.nframes,
                "Képarány (szélesség x magasság)": clip.size,
                "Időtartam (mp)": clip.duration
            }

            # Metaadatok hozzáadása a listához
            metaadatok_lista.append(metaadatok)

            # Video klip lezárása
            clip.close()

    return metaadatok_lista

# Tesztelés: Add meg a mappa elérési útját
mappa_eleresi_ut = 'p:/tmp/iTTHONVAGY/2016.09.12 Bükk'
metaadatok = gyujtsd_ossze_metaadatokat(mappa_eleresi_ut)

# Metaadatok kiírása
for metaadat in metaadatok:
    print("\nVideó metaadatok:")
    for kulcs, ertek in metaadat.items():
        print(f"{kulcs}: {ertek}")
