import sample_data

def build_nested_plan(plan):
  
    """
    Build a nested plan organized by year and session.
    Args:
        plan (dict): A dictionary where keys are course IDs and values are year/session
        Returns:
        dict: A nested dictionary grouped by year and session
    """
    nested_plan = {
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
                nested_plan[year_key][session].append((course["_id"], course["number"]))
    return nested_plan