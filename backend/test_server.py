import pytest
import json
from server import app
import sample_data


# test to make sure that all majors appear
def test_get_all_majors():
    response = app.test_client().get('/api/v2/majors')

    try:
        assert response.status_code == 200
        res = response.get_json().get("majors")
        assert type(res[0]) is dict
        assert type(res[1]) is dict
        assert res[0]["_id"] == 1
        assert res[1]["name"] == "Mechanical Engineering Gateway"

    except (KeyError, TypeError, json.JSONDecodeError, AssertionError) as e:
        pytest.fail(f"Failed to process /api/v2/majors response: {e}")


# runs the test once for each major_id (currently just 1 and 2)
@pytest.mark.parametrize("major_id", [1, 2])
def test_major_plan(major_id):
    response = app.test_client().get(f'/api/v2/majors/{str(major_id)}/plan')
    
    try:
        assert response.status_code == 200
        id = response.get_json().get("major_id")
        default_plan = response.get_json().get("default_plan")
        assert type(default_plan) is dict
        for i in range(1,5):
            assert type(default_plan[f"year{i}"]) is dict
        assert id == major_id

    except (KeyError, TypeError, AssertionError, json.JSONDecodeError) as e:
        pytest.fail(f"Failed to process /api/v2/majors/{str(major_id)}/plan: {e}")


# runs the test for each course id in sample data
@pytest.mark.parametrize("course_id", [id for id in range(101, 108)])
def test_course_info(course_id):
    response = app.test_client().get(f'/api/v2/courses/{str(course_id)}')

    try:
        assert response.status_code == 200
        id = response.get_json().get("_id")
        assert id == course_id

        prerequisites = response.get_json().get("prerequisites")
        corequisites = response.get_json().get("corequisites")
        assert type(prerequisites) == list
        assert type(corequisites) == list

    except (KeyError, TypeError, AssertionError, json.JSONDecodeError) as e:
        pytest.fail(f"Failed to process /api/v2/courses/{str(course_id)}: {e}")


# runs the test for each course id in sample data
@pytest.mark.parametrize("course_id", [id for id in range(101, 108)])
def test_course_requirements(course_id):
    response = app.test_client().get(f'/api/v2/courses/{str(course_id)}/requirements')

    try:
        assert response.status_code == 200
        course = next((c for c in sample_data.courses if c['_id'] == course_id), None)
        prerequisites = response.get_json().get("prerequisites")
        corequisites = response.get_json().get("corequisites")

        assert type(prerequisites) == list
        assert type(corequisites) == list
        assert course["prerequisites"] == prerequisites
        assert course["corequisites"] == corequisites

    except (KeyError, TypeError, AssertionError, json.JSONDecodeError) as e:
        pytest.fail(f"Failed to process /api/v2/courses/{str(course_id)}/requirements: {e}")