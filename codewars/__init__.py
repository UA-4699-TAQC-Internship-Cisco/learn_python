from . import (Dbautista,
               YuliaShap,
               mpeshko)

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

    "mpeshko": {
        "kyu8": mpeshko.ky8,
        "kyu7": mpeshko.ky7,
        "kyu6": mpeshko.ky6,
        "kyu5": mpeshko.ky5
    }
}