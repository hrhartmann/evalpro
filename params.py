
from math import log

I_PPC = 1.5 # products per client
I_PRODUCTS = 3649215
I_CLIENTS = I_PRODUCTS / I_PPC
YEARS = 10

combinatios = {
    "nocs" : {
        "ngc" : .033,
        "ppgc": .018
    },
    "pessimistic" : {
        "ngc" : .030,
        "ppgc": .020
    },
    "neutral" : {
        "ngc" : .030,
        "ppgc": .021
    },
    "optimistic" : {
        "ngc" : .040,
        "ppgc": .030
    },
    "goal" : {
        "ngc" : .012,
        "ppgc": .040
    },
    "optimistic_goal" : {
        "ngc" : .030,
        "ppgc": .056
    }
}


# GROWTH = 0.05
