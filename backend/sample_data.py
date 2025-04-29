from enum import Enum
TITLE = "Simple Planner"

# constants for the fills_up_quickly field
ALWAYS = "Always"
RARELY = "Rarely"
SOMETIMES = "Sometimes"

# Enums for Major and Course IDs
# Access the major id with the Enum: Major.<major_abbreviation>.value
# Access the course id with the Enum: Course.<course_number>.value
class Major(Enum):
    CMSC_GATEWAY = 1
    ENME_GATEWAY = 2


class Course(Enum):
    MATH151 = 101
    MATH152 = 102
    CMSC201 = 103
    CMSC202 = 104
    PHYS121 = 105
    ENES101 = 106
    ENME110 = 107


    def __str__(self):
        return self.name

# Define the courses collection
#
# This is a list of dictionaries, where each course is a dictionary
# with these attributes (key/value pairs):
# id: int (i.e. 101)
# number: string (i.e. "MATH151")
# title: string (i.e. "Calculus and Analytic Geometry")
# description: string (i.e. "Calculus and Analytic Geometry")
# credit hours: int (i.e. 4)
# fills_up_quickly: string constant (i.e RARELY)
# offered_winter: bool (i.e. False)
# offered_summer: bool (i.e. True)
# prerequisites: list of ints corresponding to course ids, or []
# corequisites: list of ints corresponding to course ids, or []
# advisor notes: optional notes on registering for the course
# Note that id's are hardcoded for now for ease of development

courses = [
    {
        "_id": Course.MATH151.value,
        "number": "MATH151",
        "title": "Calculus and Analytic Geometry I",
        "description": """Topics of this course include limits, continuity, the rate 
        of change, derivatives, differentiation formulas for algebraic, trigonometric, 
        logarithmic, and exponential functions, maxima and minima, integration and 
        computation of areas, the Fundamental Theorem of Calculus, areas and volumes 
        of solids of revolution, and applications. Note: Non-science oriented students 
        should consider MATH 155. Credit will not be given for both MATH 151 and MATH 155.""",
        "credit_hours": 4,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Note: You may test out of this course, or need to take additional prequisites.",
    },
    {
        "_id": Course.MATH152.value,
        "number": "MATH152",
        "title": "Calculus and Analytic Geometry II",
        "description": """Topics of this course include inverse functions, methods of 
        integration, improper integrals, hyperbolic functions, sequences and infinite 
        series, power series, Taylor series, conic sections, polar coordinates, and applications. """,
        "credit_hours": 4,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.MATH151.value],
        "corequisites": [],
        "advisor_notes": """You may test out of this course, or need to take additional prequisites. 
        Consult your advisor.""",
    },
    {
        "_id": Course.CMSC201.value,
        "number": "CMSC201",
        "title": "Computer Science I",
        "description": """An introduction to computer science through problem solving 
        and computer programming. Programming techniques covered by this course include 
        modularity, abstraction, top-down design, specifications documentation, debugging 
        and testing. The core material for this course includes control structures, functions, 
        lists, strings, abstract data types, file I/O, and recursion.""",
        "credit_hours": 4,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": """You cannot take MATH151 at the same time unless you have taken at least MATH150
        or tested out of MATH. Consult your advisor.""",
    },
    {
        "_id": Course.CMSC202.value,
        "number": "CMSC202",
        "title": "Computer Science II",
        "description": """This course continues the student’s development of programming 
        and problem-solving skills by providing an introduction to object-oriented design 
        and programming (OOP). The primary focus is on OOP principles and techniques, including 
        encapsulation, composition, inheritance, and polymorphism. Other OOP topics such as exception 
        handling, containers, and generic programming are also covered. This is the second course for 
        students interested in pursuing further study in computer science.""",
        "credit_hours": 4,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMSC201.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.PHYS121.value,
        "number": "PHYS121",
        "title": "Introductory Physics I",
        "description": """This is the first-semester introductory calculus-based physics course. 
        Topics include kinematics, Newton’s laws, gravitation, conservation laws, rotation, and 
        simple harmonic motion. This course consists of lectures and discussions. (Fall/Spring)""",
        "credit_hours": 4,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [Course.MATH151.value],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENES101.value,
        "number": "ENES101",
        "title": "Introduction to Engineering",
        "description": """This course is an introduction to engineering that covers “thinking like an engineer;” 
        including professional practice, data analysis and curve fitting, estimation, engineering units and 
        dimensional analysis, and the engineering design process. Students must work in teams on a design project, 
        which includes design, construction, evaluation, testing, modeling and presentation. The course includes 
        an introduction to computer programming in MATLAB and to engineering ethics.""",
        "credit_hours": 4,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [],
        "corequisites": [Course.MATH151.value],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME110.value,
        "number": "ENME110",
        "title": "Statics",
        "description": """The equilibrium of stationary bodies under the influence of various kinds of forces. 
        Forces, moments, couples, equilibrium, trusses, frames and machines, centroids, moments of inertia, 
        beams, friction and hydrostatics. Vector and scalar methods are used to solve problems.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.MATH151.value],
        "corequisites": [Course.PHYS121.value],
        "advisor_notes": "None",
    },
]

# Define the majors collection
# This is a list of dictionaries, where each major is a dictionary with
# these attributes:
# id: int (i.e. 1)
# name: string (i.e. "Computer Science Gateway")
# number_credits: int (i.e 12)
# required_courses: list of ints, where each int is a course id ***MAY BE ABLE TO DELETE THIS ATTRIBUTE***
# default_plan: dictionary of dictionaries, where each top-level key is a course in the plan, and each
# top-level value is a dictionary for the scheduled time of the plan. This subdictionary has keys of year
# and session. This allows courses to be reused in other major course sequences. 

majors = [
    {
        "_id": Major.CMSC_GATEWAY.value,
        "name": "Computer Science Gateway",
        "number_credits": 12,
        "required_courses": [Course.MATH151.value, Course.CMSC201.value, Course.CMSC202.value],
        "default_plan": {
            Course.MATH151.value: {"year": 1, "session": "Fall"},
            Course.CMSC201.value: {"year": 1, "session": "Fall"},
            Course.CMSC202.value: {"year": 1, "session": "Spring"}
        }
    },
    {
        "_id": Major.ENME_GATEWAY.value,
        "name": "Mechanical Engineering Gateway",
        "number_credits": 19,
        "required_courses": [Course.MATH151.value, Course.MATH152.value, Course.PHYS121.value, Course.ENES101.value, Course.ENME110.value],
        "default_plan": {
            Course.MATH151.value: {"year": 1, "session": "Fall"},
            Course.MATH152.value: {"year": 1, "session": "Spring"},
            Course.PHYS121.value: {"year": 1, "session": "Fall"},
            Course.ENES101.value: {"year": 1, "session": "Fall"},
            Course.ENME110.value: {"year": 1, "session": "Spring"}
        }
    },
]

# Define the student collection
# This is a list of dictionaries, where each dictionary corresponds to a student
# Student attibutes are key/value pairs as follows:
# _id: int (i.e. 1000)
# email: string (i.e. student@umbc.edu)
# major_id: int (the id of the major which they have selected, i.e. Major.CMCS_Gateway) 
# custom_plan: dictionary of dictionaries, where each top-level key is a course in the plan, and each
# top-level value is a dictionary for the scheduled time of the plan. This subdictionary has keys of year
# and session. This allows the student plan to diverge from the default plan. 
students = [
    {
        "_id": 1000,
        "email": "umbc",
        "major_id": Major.CMSC_GATEWAY.value,
        "custom_plan": {}
    },
]