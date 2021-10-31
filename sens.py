from params import *

CHOSEN = "optimistic"
# TITLE = f"{CHOSEN}"
CC = combinatios[CHOSEN]


def grow(ippc, iclients, iproducts, cc, years, title):
    ppc = ippc
    ngc = cc["ngc"]
    ppcg = cc["ppgc"]
    clients = iclients
    products = iproducts
    print()
    print(f"year: 0")
    print(f"products: {iproducts}")
    print(f"clients: {iclients}")
    print(f"ppc: {ippc}")
    reportdata = ""
    for year in range(1, years + 1):

        products = products * (1 + ngc + ppcg)
        clients = clients + products*ngc
        ppc = products / clients
        ysummary = f"\nyear: {year} \nproducts: {products}\n"\
                   f"clients: {clients} \nppc: {ppc} \n"
        print()
        print(f"year: {year}")
        print(f"products: {products}")
        print(f"clients: {clients}")
        print(f"ppc: {ppc}")
        reportdata += ysummary
    gen_report(reportdata, title)

def gen_report(data, title):
    with open(f"reports/report_{title}.txt", "w") as file:
        file.writelines(data)


if __name__ == "__main__":

    grow(I_PPC, I_CLIENTS, I_PRODUCTS, CC, YEARS, CHOSEN)






































# Nothing By AbyssalBit ~With Style
