

class VAN:

    def __init__(self,
                 sells,
                 project_costs,
                 list_sells=[],
                 list_costs=[],
                 init_investment=0,
                 ut=0.05,
                 period=10,
                 disc_rate=0.1,
                 linear_growth=0):


        self.sells = sells # annual sales
        self.costs = project_costs # annual costs
        self.init_investment = init_investment
        self.ut = ut # fraction of utilities from sells
        self.utilities = self.sells * self.ut # annual utilities
        self.years = period # years to print
        self.disc_rate = disc_rate
        self.linear_growth = linear_growth
        self.data = {"sells": list_sells, "costs": list_costs}

    def csv_data(self):
        txt = ""
        self.gen_data()
        txt += self.str_data_list("years")
        txt += self.str_data_list("sells")
        txt += self.str_data_list("utilities")
        txt += self.str_data_list("costs")
        txt += self.str_data_list("van")

        return txt

    def gen_data(self):
        self.data["years"] = [t for t in range(self.years)]
        if not self.data["sells"]:
            self.data["sells"] = self.linear_gen(self.sells)
            self.data["utilities"] = self.linear_gen(self.utilities)
        else:
            self.data["utilities"] = self.get_utilities()
        if not self.data["costs"]:
            self.data["costs"] = [self.costs for _ in range(self.years)]
        self.data["costs"][0] += self.init_investment
        van = []
        for t in range(self.years):
            div = (1 + self.disc_rate)**t
            van_y = (self.data["utilities"][t] - self.data["costs"][t])/div
            van.append(van_y)
        van.append(sum(van))
        self.data["van"] = van

    def str_data_list(self, name):
        list = self.data[name]
        return f"{name}," + str(list).strip("[").strip("]") + "\n"

    def linear_gen(self, x):
        return [round(x + x*t*self.linear_growth, 3) for t in range(self.years)]

    def get_utilities(self):
        return [x*self.ut for x in self.data["sells"]]






































        # Nothing By AbyssalBit ~With Style
