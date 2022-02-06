def calculate_time(time_enter_str, time_out_str):
    def parse_time(time_str):
        time = 60 * int(time_str[:2]) + int(time_str[3:])
        return time

    time_enter = parse_time(time_enter_str)
    time_out = parse_time(time_out_str)
    time_parked = time_out - time_enter
    return time_parked


def calculate_fee(time_parked, fees):
    """
        :param fees: 주차 요금
                fees[0]: 기본 시간(분)
                fees[1]: 기본 요금(원)
                fees[2]: 단위 시간(분)
                fees[3]: 단위 요금(원)
    """

    # 주차 시간이 기본 시간 이하일 경우
    if time_parked <= fees[0]:
        price = fees[1]

    # 주차 시간이 기본 시간 초과일 경우
    else:
        price = fees[1] + fees[3] * ((time_parked - fees[0]) // fees[2])
        # 올림 처리
        if (time_parked - fees[0]) % fees[2] > 0:
            price += fees[3]

    # print(time_parked, price, fees)
    return price

def solution(fees, records):
    """
    :param fees: 주차 요금
                fees[0]: 기본 시간(분)
                fees[1]: 기본 요금(원)
                fees[2]: 단위 시간(분)
                fees[3]: 단위 요금(원)
    :param records: 자동차 입/출차 내역
                record: "시각 차량번호 내역"
                        "05:34 5961 IN"
                        "06:34 0000 OUT"
    :return:
    """

    entered_cars = dict([]) # 자동차별 입차 내역
    time_cars = dict([]) # 자동차별 주차 시간 내역
    paid_cars = dict([]) # 자동차별 기 지불된 요금 내역


    for record in records:
        record_list = record.split(" ")

        if record_list[2] == "IN":
            car_number = record_list[1]
            time_enter_str = record_list[0]
            entered_cars[car_number] = time_enter_str

        elif record_list[2] == "OUT":
            car_number = record_list[1]
            time_out_str = record_list[0]
            time_enter_str = entered_cars[car_number]

            time_parked = calculate_time(time_enter_str, time_out_str)
            if car_number in time_cars:
                time_cars[car_number] += time_parked
            else:
                time_cars[car_number] = time_parked

            del entered_cars[car_number]

    # 나오지 않은 차들에 대해 시간 재측정
    for car_number in entered_cars:
        time_enter_str = entered_cars[car_number]

        time_parked = calculate_time(time_enter_str, "23:59")
        if car_number in time_cars:
            time_cars[car_number] += time_parked
        else:
            time_cars[car_number] = time_parked


    # print(time_cars)
    answer = []
    for car_number in sorted(time_cars.keys()):
        time_parked = time_cars[car_number]
        price = calculate_fee(time_parked, fees)
        answer.append(price)

    return answer


fees, records = [180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                       "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))