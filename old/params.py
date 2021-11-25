
from math import log

I_PPC = 1.5 # products per client
I_PRODUCTS = 3649215 # products on period 0
I_CLIENTS = I_PRODUCTS / I_PPC

PDR = .1 # project discount rate
MP = 5 # mean prime in Chilean UF
EXE_RES = .05354 # exercise result
YEARS = 10 # period

combinatios = {
    "nocs" : {
        "ngc" : .033,
        "ppgc": .018
    },
    "pessimistic" : {
        "ngc" : .03,
        "ppgc": .020
    },
    "neutral" : {
        "ngc" : .030,
        "ppgc": .021
    },
    "project" : {
        "ngc" : .032,
        "ppgc": .022
    },
    "good" : {
        "ngc" : .032,
        "ppgc": .028
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
