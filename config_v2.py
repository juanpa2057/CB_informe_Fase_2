NIGHT_HOURS = [0, 1, 2, 3, 4, 5, 19, 20, 21, 22, 23]

# date format would be "YYYY-MM-DD"
# last baseline date must be the same
# date as start of study. Basically all
# dates must be mondays.
BASELINE = ['2025-03-01', '2025-07-21']
STUDY = ['2025-07-21', '2025-07-28']
PAST_WEEK = ['2025-07-14', '2025-07-21']

DATE_INTERVALS_TO_DISCARD = {
}

# variables that make up totalizer measurement
ENERGY_VAR_LABELS = ('aa-consumo-activa', 'ilu-consumo-activa')
POWER_VAR_LABELS = ('aa-potencia-activa', 'ilu-potencia-activa')


WHITELISTED_VAR_LABELS = (
    "ilu-consumo-activa",
    "consumo-energia-reactiva-total",
    "aa-consumo-activa",
    "front-consumo-activa",
    "aa-potencia-activa",
    "consumo-energia-reactiva-capacitiva",
    "consumo-energia-reactiva-inductiva",
    "factor-de-potencia",
    "area",
    "tr",
    "kw-tr",
    # "front-tension-3",
    # "front-tension-2",
    # "front-tension-1",
    "front-potencia-activa",
    "ilu-potencia-activa",
)

print("Baseline en config_v2.py:", BASELINE)
print("Study en config_v2.py:", STUDY)
