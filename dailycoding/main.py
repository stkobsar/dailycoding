import argparse
import dailycoding.programms.day1 as d1
import dailycoding.programms.day5 as d5

def main(args):
    if args.day1:
        k = 17
        integer_list = [10, 15, 3, 7]
        result_day1 = d1.get_day1(k, integer_list)
        print(f"The result for the given k and integer list is: {result_day1}")
    if args.day5:
        object_from_cons_day5 = d5.cons(1, 5)
        result_car_day5 = d5.get_object_value_car(4, 7)
        print(result_car_day5)
        result_cdr_day5 = d5.get_object_value_crd(1, 7)
        print(result_cdr_day5)



if __name__ == '__main__':
    #############ARGPARSE########
    parser = argparse.ArgumentParser(description='daily coding')
    parser.add_argument("--day1", action="store_true", help="Execute day1 problem")
    parser.add_argument("--day5", action="store_true", help="Execute day5 problem")
    args = parser.parse_args()
    ############################
    main(args)


