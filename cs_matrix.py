
from van_class import VAN
from params import (
   YEARS,
   LINEAR_GROWTH, 
   LIST_SELLS, 
   SELLS, 
   COSTS, 
   INIT_INV, 
   CLIENTS,  
   Y_VALUE  
)


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
    
    van_obj = VAN(SELLS, 
                  COSTS, 
                  list_sells=LIST_SELLS, 
                  init_investment=INIT_INV, 
                  linear_growth=LINEAR_GROWTH)
    txt = van_obj.csv_data()
    name = input("Enter file name: ")
    if name != "":
        write_csv(txt, f"{name}.csv")
