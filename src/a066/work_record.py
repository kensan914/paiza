from itertools import chain


class WorkRecord:
    def __init__(self, work_schedules: list[tuple[int, int]]):
        self.work_schedules = work_schedules

    def get_continuous_work_days(self) -> int:
        work_day_list = list(self.work_day_set)
        work_day_list.sort()
        continuous_work_days = 0
        continuous_work_days_list: list[int] = []
        for i in range(len(work_day_list) - 1):
            current_day = work_day_list[i]
            next_day = work_day_list[i + 1]
            if current_day + 1 == next_day:
                # NOTE: 次の値も連続した数値だった場合
                continuous_work_days += 1
            else:
                # NOTE: 次の値で連続が途切れる場合
                continuous_work_days_list.append(continuous_work_days + 1)
                continuous_work_days = 0
        else:
            continuous_work_days_list.append(continuous_work_days + 1)

        return max(continuous_work_days_list)

    @property
    def work_day_set(self) -> set[int]:
        def _generator():
            for work_schedule in self.work_schedules:
                start_day, end_day = work_schedule
                yield range(start_day, end_day + 1)

        return set(chain.from_iterable(_generator()))
