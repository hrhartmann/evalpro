
from van_class import VAN

YEARS = 10
LINEAR_GROWTH = 0.03
SELLS = 90000
COSTS = 7397
INIT_INV = 2464
CLIENTS = 200000
Y_VALUE = 15

def min_cross_one_p(y_value,
                    x_clients,
                      period=5,
                      objective=17000):
    objective = objective / 0.05
    y_annual_sells = get_annual_sales(objective, y_value, period)
    cross_x = y_annual_sells / x_clients
    return cross_x


def get_annual_sales(x, y, t):
    return x / (y*t)


def show_values(value, name):
    print("min cross: {}".format(name))
    print("in %: {}%".format(value * 100))


def write_csv(data, filename):
    with open(f"csvs/{filename}", "w") as file:
        file.writelines(data)


if __name__ == "__main__":
    min_cross_v1 = min_cross_one_p(Y_VALUE, CLIENTS, period=YEARS, objective=COSTS)
    show_values(min_cross_v1, "Vehicles x vehicles")
    annual_sales = get_annual_sales(COSTS, 15, 5)
    van_obj = VAN(SELLS, COSTS, init_investment=INIT_INV, linear_growth=LINEAR_GROWTH)
    txt = van_obj.csv_data()
    name = input("Enter file name: ")
    if name != "":
        write_csv(txt, f"{name}.csv")
