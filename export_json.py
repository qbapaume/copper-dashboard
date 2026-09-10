import json
import pandas as pd

# ==========================================
# CONFIGURATION
# ==========================================

EXCEL_FILE = r"\\192.33.50.2\Bureautique\Cours cuivre automatique\Historique_Metaux.xlsx"

# ==========================================
# FONCTION DE CALCUL DES VARIATIONS
# ==========================================

def calc_variation(current, previous):

    variation = round(
        float(current) - float(previous),
        2
    )

    pct = round(
        (variation / float(previous)) * 100,
        2
    )

    if variation > 0:

        arrow = "▲"
        color = "positive"

    elif variation < 0:

        arrow = "▼"
        color = "negative"

    else:

        arrow = "►"
        color = "neutral"

    return variation, pct, arrow, color


# ==========================================
# LECTURE EXCEL
# ==========================================

df = pd.read_excel(EXCEL_FILE)

derniere = df.iloc[-1]

# ==========================================
# CALCUL DES VARIATIONS
# ==========================================

if len(df) >= 2:

    precedente = df.iloc[-2]

    var_lme, pct_lme, arrow_lme, color_lme = calc_variation(
        derniere["LME"],
        precedente["LME"]
    )

    var_eurusd, pct_eurusd, arrow_eurusd, color_eurusd = calc_variation(
        derniere["EURUSD"],
        precedente["EURUSD"]
    )

    var_girm, pct_girm, arrow_girm, color_girm = calc_variation(
        derniere["GIRM"],
        precedente["GIRM"]
    )

    var_bmc, pct_bmc, arrow_bmc, color_bmc = calc_variation(
        derniere["BMC"],
        precedente["BMC"]
    )

else:

    var_lme = pct_lme = 0
    var_eurusd = pct_eurusd = 0
    var_girm = pct_girm = 0
    var_bmc = pct_bmc = 0

    arrow_lme = "►"
    arrow_eurusd = "►"
    arrow_girm = "►"
    arrow_bmc = "►"

    color_lme = "neutral"
    color_eurusd = "neutral"
    color_girm = "neutral"
    color_bmc = "neutral"

# ==========================================
# DATA PRINCIPALE
# ==========================================

data = {

    "date": str(derniere["Date_MAJ"]),
    "time": str(derniere["Heure_MAJ"]),

    "lme": float(derniere["LME"]),
    "eurusd": float(derniere["EURUSD"]),
    "girm": float(derniere["GIRM"]),
    "bmc": float(derniere["BMC"]),

    "date_lme": str(derniere["Date_LME"]),
    "date_eurusd": str(derniere["Date_EURUSD"]),
    "date_girm": str(derniere["Date_GIRM"]),
    "date_bmc": str(derniere["Date_BMC"]),

    "var_lme": var_lme,
    "pct_lme": pct_lme,
    "arrow_lme": arrow_lme,
    "color_lme": color_lme,

    "var_eurusd": var_eurusd,
    "pct_eurusd": pct_eurusd,
    "arrow_eurusd": arrow_eurusd,
    "color_eurusd": color_eurusd,

    "var_girm": var_girm,
    "pct_girm": pct_girm,
    "arrow_girm": arrow_girm,
    "color_girm": color_girm,

    "var_bmc": var_bmc,
    "pct_bmc": pct_bmc,
    "arrow_bmc": arrow_bmc,
    "color_bmc": color_bmc
}

# ==========================================
# ECRITURE DATA.JSON
# ==========================================

with open(
    "data.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        data,
        f,
        ensure_ascii=False,
        indent=4
    )

# ==========================================
# HISTORIQUE 60 DERNIERES LIGNES
# ==========================================

historique = (
    df.tail(60)
      .iloc[::-1]
      .fillna("")
      .to_dict("records")
)

# ==========================================
# ECRITURE HISTORIQUE.JSON
# ==========================================

with open(
    "historique.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        historique,
        f,
        ensure_ascii=False,
        indent=4,
        default=str
    )

# ==========================================
# FIN
# ==========================================

print()
print("✅ data.json créé")
print("✅ historique.json créé")
print("✅ 60 dernières lignes exportées")