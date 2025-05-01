import sample_data

def build_nested_plan(plan):
  
    """
    Build a nested plan organized by year and session.
    Args:
        plan (dict): A dictionary where keys are course objects and values are year/session
        Returns:
        dict: A nested dictionary grouped by year and session where each session contains 
              an array of course objects
    """
    nested_plan = {
        "year0": {"PastCoursework": []},
        "year1": {"Fall": [], "Winter": [], "Spring": [], "Summer": []},
        "year2": {"Fall": [], "Winter": [], "Spring": [], "Summer": []},
        "year3": {"Fall": [], "Winter": [], "Spring": [], "Summer": []},
        "year4": {"Fall": [], "Winter": [], "Spring": [], "Summer": []},
    }

    for course_id, schedule in plan.items():
        year_key = f"year{schedule['year']}"
        session = schedule["session"]
        if year_key in nested_plan and session in nested_plan[year_key]:
            course = next((c for c in sample_data.courses if c["_id"] == course_id), None)
            if course:
                nested_plan[year_key][session].append(
                    {"id": course["_id"],
                     "number": course["number"],
                     "credit_hours": course["credit_hours"],
                     "offered_winter": course["offered_winter"],
                     "offered_summer": course["offered_summer"],
                     "prerequisites": course["prerequisites"],
                     "corequisites": course["corequisites"],
                     })
    return nested_plan