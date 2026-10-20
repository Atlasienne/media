import sys, re
sys.path.insert(0, "/home/claude/atlasienne")
import atl2
_orig = atl2.pied
atl2.pied = lambda d, c, pages, img_bg, img=None: _orig(d, c, None, img_bg, img)
which = sys.argv[1]
if which == "lot1":
    src = open("lot1.py").read().replace('BASE = "/home/claude/media/posts/lot01/"', 'BASE = "/home/claude/media/reels_src/lot01/"')
else:
    common = open("lot_common2.py").read().replace('BASE = "/home/claude/media/posts/lot02/"', 'BASE = "/home/claude/media/reels_src/lot02/"')
    open("/tmp/lc2.py", "w").write(common)
    src = open("lot2.py").read().replace('/home/claude/atlasienne/lot_common2.py', '/tmp/lc2.py')
src = src.replace("/home/claude/atlasienne/lot2_grille.png", "/tmp/g.png").replace("/home/claude/atlasienne/review2_", "/tmp/r2_").replace("/home/claude/atlasienne/lot1_grille.png", "/tmp/g1.png")
import os; os.makedirs("/home/claude/media/reels_src/lot01", exist_ok=True); os.makedirs("/home/claude/media/reels_src/lot02", exist_ok=True)
exec(compile(src, which, "exec"), {"__name__": "__main__"})
