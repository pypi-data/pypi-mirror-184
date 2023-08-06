import cwbplot
from pathlib import Path
import matplotlib
import os
from matplotlib.font_manager import FontProperties


__version__= "0.0.7"

verlist = matplotlib.__version__.split(".")
_cntjude4matplt = 0
if int(verlist[0]) < 3:
    _cntjude4matplt = 1
if _cntjude4matplt == 0 and int(verlist[1]) < 2:
    _cntjude4matplt = 1

cwbpakpath = cwbplot.__path__[0]
#bentham blue-highway caliban carlito expressway-free raleway rosario TaipeiSansTCBeta times
def font(lang = "en", style = "times", weight="normal", size = 12):
    if lang.lower() == "en":
        if _cntjude4matplt == 0 and weight == "normal":
            getfont = Path(os.path.join(cwbpakpath, f"fonts/{style}.ttf"))
        elif _cntjude4matplt == 0 and weight == "bold":
            getfont = Path(os.path.join(cwbpakpath, f"fonts/{style}bd.ttf"))
        elif _cntjude4matplt == 1 and weight == "normal":
            getfont = os.path.join(cwbpakpath, f"fonts/{style}.ttf")
        elif _cntjude4matplt == 1 and weight == "bold":
            getfont = os.path.join(cwbpakpath, f"fonts/{style}bd.ttf")
    if lang.lower() == "cht":
        if _cntjude4matplt == 0 and weight == "normal":
            getfont = Path(os.path.join(cwbpakpath, "fonts/TaipeiSansTCBeta.ttf"))
        elif _cntjude4matplt == 0 and weight == "bold":
            getfont = Path(os.path.join(cwbpakpath, "fonts/TaipeiSansTCBetabd.ttf"))
        elif _cntjude4matplt == 1 and weight == "normal":
            getfont = os.path.join(cwbpakpath, "fonts/TaipeiSansTCBeta.ttf")
        elif _cntjude4matplt == 1 and weight == "bold":
            getfont = os.path.join(cwbpakpath, "fonts/TaipeiSansTCBetabd.ttf")
    if _cntjude4matplt == 0:
        fontdict = {"fname":getfont,"size":size}
    else:
        fontdict = FontProperties(fname=getfont,size=size)
    return fontdict
