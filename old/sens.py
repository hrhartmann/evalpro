from params import *

CHOSEN = "good"
# TITLE = f"{CHOSEN}"
CC = combinatios[CHOSEN]

class period:

    def __init__(self, year, products, clients):
        int_exe_res = EXE_RES
        int_media_prime = MP
        self.year = year
        self.products = products
        self.clients = clients
        self.ppc = products / clients
        self.sales = self.products * int_media_prime
        self.costs = self.sales * (1 - int_exe_res)
        self.utilities = self.sales - self.costs


def build_csv(periods, years, title):
    csv_data = ""
    rows = {
        "period" : "",
        "products": "",
        "clients": "",
        "ppc": "",
        "sales": "",
        "costs": "",
        "utilities": ""
        }

    for y in range(years):
        rows["period"] += f"{y + 1},"
        rows["products"] += f"{periods[y].products},"
        rows["clients"] += f"{periods[y].clients},"
        rows["ppc"] += f"{periods[y].ppc},"
        rows["sales"] += f"{periods[y].sales},"
        rows["costs"] += f"{periods[y].costs},"
        rows["utilities"] += f"{periods[y].utilities},"

    csv_data = f"period,0,{rows['period']}\n"
    csv_data += f"products,3649215,{rows['products']}\n"
    csv_data += f"clients,2432810,{rows['clients']}\n"
    csv_data += f"ppc,1.5,{rows['ppc']}\n"
    csv_data += f"sales,18246075,{rows['sales']}\n"
    csv_data += f"costs,17269180,{rows['costs']}\n"
    # csv_data += f"utilities,{rows['utilities']}\n"

    gen_csv(csv_data, title)


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
    period_list = []
    for year in range(1, years + 1):

        products = products * (1 + ngc + ppcg)
        clients = clients + products*ngc
        ppc = products / clients
        sales = products * MP
        costs = sales * (1 - EXE_RES)
        utilities = sales - costs
        new_period = period(year, products, clients)
        period_list.append(new_period)
        # ysummary = f"\nyear: {year} \nproducts: {products}\n"\
        #            f"sales: {sales}\n"\
        #            f"costs: {costs}\n"\
        #            f"utilities: {utilities}\n"\
        #            f"clients: {clients} \nppc: {ppc} \n"
        # print()
        # print(f"year: {year}")
        # print(f"products: {products}")
        # print(f"clients: {clients}")
        # print(f"ppc: {ppc}")
        # reportdata += ysummary
    # gen_report(reportdata, title)
    build_csv(period_list, years, title)

def gen_report(data, title):
    with open(f"reports/report_{title}_nv.txt", "w") as file:
        file.writelines(data)

def gen_csv(data, title):
    with open(f"csvs/report_{title}_nv.csv", "w") as file:
        file.writelines(data)


if __name__ == "__main__":
    for s in combinatios:
        grow(I_PPC, I_CLIENTS, I_PRODUCTS, combinatios[s], YEARS, s)






































# Nothing By AbyssalBit ~With Style
