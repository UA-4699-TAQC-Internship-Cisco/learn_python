from . import (Dbautista,
               YuliaShap,
               BrekhovaT)

IMPLEMENTATIONS = {
    "Dbautista": {
        "kyu8": Dbautista.codewars_tasks_8kyu,
        "kyu7": Dbautista.codewars_tasks_7kyu,
        "kyu6": Dbautista.codewars_tasks_6kyu,
        "kyu5": Dbautista.codewars_tasks_5kyu
    },

    "YuliaShap": {
        "kyu8": YuliaShap.kyu8,
        "kyu7": YuliaShap.kyu7,
        "kyu6": YuliaShap.kyu6,
        "kyu5": YuliaShap.kyu5
    },
    "BrekhovaT": {
        "kyu8": BrekhovaT.kyu8,
        "kyu7": BrekhovaT.kyu7,
        "kyu6": BrekhovaT.kyu6,
        "kyu5": BrekhovaT.kyu5
    }
}
