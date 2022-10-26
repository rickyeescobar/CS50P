import pytest
import datetime
import seasons

def test_dates():
    assert seasons.get_dob("2021-08-23") == datetime.date(2021, 8, 23)


if __name__ == "__main__":
    main()