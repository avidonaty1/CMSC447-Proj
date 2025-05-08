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
        assert res[1]["name"] == "Mechanical Engineering B.S."

    except (KeyError, TypeError, json.JSONDecodeError, AssertionError) as e:
        pytest.fail(f"Failed to process /api/v2/majors response: {e}")


# runs the test once for each major_id (currently just 1 and 2)
@pytest.mark.parametrize("major_id", [major.value for major in sample_data.Major])
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
@pytest.mark.parametrize("course_id", [id.value for id in sample_data.Course])
def test_course_info(course_id):
    response = app.test_client().get(f'/api/v2/courses/{str(course_id)}')

    try:
        assert response.status_code == 200
        id = response.get_json().get("_id")
        assert id == course_id

        prerequisites = response.get_json().get("prerequisites")
        corequisites = response.get_json().get("corequisites")
        assert type(prerequisites) is list
        assert type(corequisites) is list

    except (KeyError, TypeError, AssertionError, json.JSONDecodeError) as e:
        pytest.fail(f"Failed to process /api/v2/courses/{str(course_id)}: {e}")


# runs the test for each course id in sample data
@pytest.mark.parametrize("course_id", [id.value for id in sample_data.Course])
def test_course_requirements(course_id):
    response = app.test_client().get(f'/api/v2/courses/{str(course_id)}/requirements')

    try:
        assert response.status_code == 200
        course = next((c for c in sample_data.courses if c['_id'] == course_id), None)
        prerequisites = response.get_json().get("prerequisites")
        corequisites = response.get_json().get("corequisites")

        assert type(prerequisites) is list
        assert type(corequisites) is list
        assert course["prerequisites"] == prerequisites
        assert course["corequisites"] == corequisites

    except (KeyError, TypeError, AssertionError, json.JSONDecodeError) as e:
        pytest.fail(f"Failed to process /api/v2/courses/{str(course_id)}/requirements: {e}")


# tests for each student
@pytest.mark.parametrize("email", [i["email"] for i in sample_data.students])
def test_student_email(email):
    response = app.test_client().get(f'/api/v2/students/email/{str(email)}')

    try:
        assert response.status_code == 200
        student = next((s for s in sample_data.students if s["email"] == email), None)
        student_id = response.get_json().get("student_id")
        assert type(student_id) is int
        assert student["_id"] == student_id

    except (KeyError, TypeError, AssertionError, json.JSONDecodeError) as e:
        pytest.fail(f"Failed to process /api/v2/students/email/{str(email)}: {e}")

# tests for each student
@pytest.mark.parametrize("_id", [i["_id"] for i in sample_data.students])
def test_student_major(_id):
    response = app.test_client().get(f'/api/v2/students/{str(_id)}/major')

    try:
        assert response.status_code == 200
        student = next((s for s in sample_data.students if s["_id"] == _id), None)
        student_id = response.get_json().get("student_id")
        major_id = response.get_json().get("major_id")
        assert student_id == _id
        assert major_id == student["major_id"]

    except (KeyError, TypeError, AssertionError, json.JSONDecodeError) as e:
        pytest.fail(f"Failed to process /api/v2/students/{str(_id)}/major: {e}")


@pytest.mark.parametrize("student_id", [i["_id"] for i in sample_data.students])
def test_student_plan(student_id):
    response = app.test_client().get(f'/api/v2/students/{str(student_id)}/plan')

    try:
        assert response.status_code == 200
        student_id = response.get_json().get("student_id") == student_id
    
    except (KeyError, TypeError, AssertionError, json.JSONDecodeError) as e:
        pytest.fail(f"Failed to process /api/v2/students/{str(student_id)}/plan: {e}")