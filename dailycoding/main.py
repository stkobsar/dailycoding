import argparse
import dailycoding.programms.day1 as d1
import dailycoding.programms.day5 as d5

def main():
    k = 17
    integer_list = [10, 15, 3, 7]
    result_day1 = d1.get_day1(k, integer_list)

    object_from_cons_day5 = d5.cons(1, 5)
    result_car_day5 = d5.get_object_value_car(4, 7)
    print(result_car_day5)
    result_cdr_day5 = d5.get_object_value_crd(1, 7)
    print(result_cdr_day5)







if __name__ == '__main__':
    main()

    #############ARGPARSE########
    parser = argparse.ArgumentParser(description='daily coding')
    args = parser.parse_args()
    ############################
