import pytest

from src.a066.work_record import WorkRecord


@pytest.mark.parametrize(
    ["work_schedules", "expected"],
    [
        ([(1, 4), (5, 7)], 7),
        ([(1, 2), (2, 3), (5, 7), (8, 15)], 11),
        ([(1, 4), (5, 6), (3, 7)], 7),
        ([(5, 6), (3, 7), (1, 4), (20, 28)], 9),
    ],
)
def test_get_continuous_work_days(work_schedules, expected):
    work_record = WorkRecord(work_schedules)

    result = work_record.get_continuous_work_days()

    assert result == expected


@pytest.mark.parametrize(
    ["work_schedules", "expected"],
    [
        ([(1, 4), (5, 7)], {1, 2, 3, 4, 5, 6, 7}),
        (
            [(1, 2), (2, 3), (5, 7), (8, 15)],
            {1, 2, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15},
        ),
        (
            [(1, 4), (5, 6), (3, 7)],
            {1, 2, 3, 4, 5, 6, 7},
        ),
    ],
)
def test_work_day_set(work_schedules, expected):
    work_record = WorkRecord(work_schedules)

    result = work_record.work_day_set

    assert result == expected
