from work_record import WorkRecord


def main():
    row_length = int(input())

    work_schedules = []
    for _ in range(row_length):
        row = input()
        start_day_str, end_day_str = row.split(" ")
        work_schedules.append((int(start_day_str), int(end_day_str)))

    continuous_work_days = WorkRecord(work_schedules).get_continuous_work_days()
    print(continuous_work_days)


if __name__ == "__main__":
    main()
