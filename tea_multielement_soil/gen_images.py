# -*- coding: utf-8 -*-
"""Parallel hero-image generation for the tea multi-element deck.
FLUX.1 Dev via fal.run. Reads FAL_KEY from env. Downloads to generated/."""
import os, json, threading, urllib.request, traceback

KEY = os.environ.get("FAL_KEY")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "generated")
os.makedirs(OUT, exist_ok=True)

PREFIX = ("Premium dark editorial scientific illustration. Deep tea-green and warm "
          "amber-gold palette on a near-black charcoal background. Subtle glowing jade "
          "neon accents, soft cinematic volumetric lighting, elegant, high detail, clean "
          "composition. No text, no letters, no words, no numbers. ")

SPECS = [
    ("cover", "landscape_16_9",
     "A single elegant oolong tea leaf and a few rolled tea pearls resting on a dark "
     "surface, with delicate faint glowing molecular network lines and tiny luminous "
     "elemental dots floating upward from the leaf like a constellation fingerprint. "
     "Premium tea-meets-science mood. Large empty negative space on the left and bottom."),
    ("fingerprint", "square_hd",
     "Conceptual cross-section: a tea shrub growing in layered soil, its roots drawing up "
     "glowing colored mineral particles from the earth into the green leaves, each particle "
     "a different luminous hue suggesting different trace elements. Sense of a geochemical "
     "fingerprint absorbed from the land. Centered composition."),
    ("icpms", "square_hd",
     "Abstract high-tech depiction of an ICP-MS argon plasma torch: a brilliant cone of "
     "superheated plasma flame ionizing a fine sample mist, streams of glowing ionized "
     "particles flying toward a mass analyzer slit, futuristic analytical instrument glow. "
     "Energetic, scientific, luminous, dark surroundings."),
    ("closing", "landscape_16_9",
     "A warm cup of golden oolong tea seen from a high side angle, gentle steam rising and "
     "softly forming the silhouette of mountainous islands and terrain, evoking geographic "
     "origin and authenticity. Calm, premium, evocative. Negative space at bottom."),
]

ENDPOINT = "https://fal.run/fal-ai/flux/dev"
results = {}

def gen(key, size, prompt):
    body = json.dumps({"prompt": PREFIX + prompt, "image_size": size,
                       "num_images": 1, "enable_safety_checker": False}).encode("utf-8")
    req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
        "Authorization": "Key " + KEY, "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=180) as r:
            data = json.loads(r.read().decode("utf-8"))
        url = data["images"][0]["url"]
        dest = os.path.join(OUT, key + ".jpg")
        with urllib.request.urlopen(url, timeout=180) as im, open(dest, "wb") as f:
            f.write(im.read())
        sz = os.path.getsize(dest)
        results[key] = "OK %s (%d KB)" % (dest, sz // 1024)
    except Exception as e:
        results[key] = "FAIL: %s\n%s" % (e, traceback.format_exc()[-400:])

if not KEY:
    raise SystemExit("FAL_KEY not set")

threads = [threading.Thread(target=gen, args=s) for s in SPECS]
for t in threads: t.start()
for t in threads: t.join()
for k in [s[0] for s in SPECS]:
    print(k, "->", results.get(k))
print("DONE")
