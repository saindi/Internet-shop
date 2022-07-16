from typing import Any, Dict, List


def filter_by_first_met_value(
        dataset: List[Dict[str, Any]], keys: List[str]
) -> List[Dict[str, Any]]:
    """Filter dataset by first met value in keys"""

    answer = []
    temp_values = []

    for item in dataset:
        temp_value = []
        for key in keys:
            temp_value.append(item[key])

        if temp_value not in temp_values:
            temp_values.append(temp_value)
            answer.append(item)

    return answer


if __name__ == "__main__":
    origin = [
        {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
        {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
        {"name": "Serhii", "company": "Hillel", "job": "Python Trainer"},
        {"name": "Vlad", "company": "A-Level", "job": "Python Trainer"},
        {"name": "Serhii", "company": "A-Level", "job": "Python Trainer"},
    ]
    test_name = [
        {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
        {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
    ]
    test_name_job = [
        {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
        {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
        {"name": "Serhii", "company": "Hillel", "job": "Python Trainer"},
        {"name": "Vlad", "company": "A-Level", "job": "Python Trainer"},
    ]
    test_name_company = [
        {"name": "Serhii", "company": "SoftServe", "job": "Software Engineer"},
        {"name": "Vlad", "company": "SoftServe", "job": "Release Manager"},
        {"name": "Serhii", "company": "Hillel", "job": "Python Trainer"},
        {"name": "Vlad", "company": "A-Level", "job": "Python Trainer"},
        {"name": "Serhii", "company": "A-Level", "job": "Python Trainer"},
    ]

    assert filter_by_first_met_value(origin, ["name"]) == test_name
    assert filter_by_first_met_value(origin, ["name", "job"]) == test_name_job
    assert filter_by_first_met_value(origin, ["name", "company"]) == test_name_company