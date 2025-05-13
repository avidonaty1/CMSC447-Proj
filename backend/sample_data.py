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
    CMSC = 1
    ENME = 2


class Course(Enum):
    MATH151 = 101
    MATH152 = 102
    CMSC201 = 103
    CMSC202 = 104
    PHYS121 = 105
    ENES101 = 106
    ENME110 = 107
    CMSC203 = 108
    CMSC304 = 109
    CMSC313 = 110
    CMSC331 = 111
    CMSC341 = 112
    CMSC411 = 113
    CMSC421 = 114
    CMSC441 = 115
    CMSC447 = 116
    MATH221 = 117
    STAT355 = 118
    SCISEQ1 = 119
    SCISEQ2 = 120
    SCILAB1 = 121
    CMSCEL1 = 122
    CMSCTC1 = 123
    ENGL100 = 124
    GEPANH1 = 125
    GEPSOC1 = 126
    GEPCUL1 = 127
    FREEEL1 = 128
    GEPLAN1 = 129
    GEPLAN2 = 130
    GEPLAN3 = 131
    CMSCEL2 = 132
    CMSCTC2 = 133
    CMSCTC3 = 134
    FREEEL2 = 135
    FREEEL3 = 136
    FREEEL4 = 137
    FREEEL5 = 138
    FREEEL6 = 139
    GEPANH2 = 140
    GEPANH3 = 141
    GEPSOC2 = 142
    GEPSOC3 = 143
    GEPCUL2 = 144

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
        "advisor_notes": "If you have not taken at least MATH150 or tested out of math, you must be enrolled in MATH151",
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
    {
        "_id": Course.CMSC203.value,
        "number": "CMSC203",
        "title": "Discrete Structures",
        "description": """This course introduces the fundamental tools, topics and concepts of discrete mathematics 
        needed to study computer science. This course emphasizes counting methods, proof techniques and problem-solving 
        strategies. Topics include Boolean algebra; set theory; symbolic logic; predicate calculus; number theory; the 
        methods of direct, indirect and inductive proofs; objective functions; equivalence relations; graphs; set partitions; 
        combinatorics; modular arithmetic; summations; and recurrences.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.MATH151.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMSC304.value,
        "number": "CMSC304",
        "title": "Social and Ethical Issues in Information Technology",
        "description": """A survey course that reviews social issues and the ethical impact of information 
        technology throughout the world. The course examines the policy issues that relate to the use of information 
        technology, such as personal privacy, rights of access, security, transborder information flow and confidentiality.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENGL100.value, Course.CMSC202.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMSC313.value,
        "number": "CMSC313",
        "title": "Computer Organization and Assembly Language Programming",
        "description": """This course introduces the student to the low-level abstraction of a computer system from
        a programmer’s point of view, with an emphasis on low-level programming. Topics include data representation, 
        assembly language programming, C programming, the process of compiling and linking, low-level memory management, 
        exceptional control flow, and basic processor architecture.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMSC202.value, Course.CMSC203.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMSC331.value,
        "number": "CMSC331",
        "title": "Principles of Programming Language",
        "description": """This course examines the theory, design and implementation of programming languages and 
        provides students with an introduction to programming languages that are likely to be new to them. Topics 
        include specifications of syntax and semantics, declarations, binding, allocation, data structures, data types, 
        control structures, control and data flow, concurrency, and the implementation and execution of programs. 
        The major language paradigms will be described and explored, including imperative, object-oriented, functional, 
        logic programming, concurrent and others. Programming projects will provide experience in several languages.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMSC202.value, Course.CMSC203.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMSC341.value,
        "number": "CMSC341",
        "title": "Data Structures",
        "description": """An examination of a range of advanced data structures, with an emphasis on an object-oriented 
        approach. Topics include asymptotic analysis; various binary search trees, including red-black and splay trees; 
        skip lists as alternatives to binary search trees; data structures for multidimensional data such as K-D trees; 
        heaps and priority queues, including binary heaps, binomial heaps, leftist heaps (and/or other mergeable heaps); 
        B-trees for external storage; other commonly used data structures, such as hash tables and disjoint sets. 
        Programming projects in this course will focus on implementation issues for data structures and on empirical 
        analysis of their asymptotic performance.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMSC202.value, Course.CMSC203.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMSC411.value,
        "number": "CMSC411",
        "title": "Computer Architecture",
        "description": """This course covers the design of complex computer systems making heavy use of the components 
        and techniques discussed in CMSC 313, CMPE 212 and CMPE 310. All parts of the computer system - CPU, memory and 
        input/output - are discussed in detail. Topics include information representation, floating-point arithmetic, 
        instructions set design issues (RISC vs. CISC), microprogrammed control, hardwired control, pipelining, memory 
        caches, bus control and timing, input/output mechanism and issues in the construction of parallel processors.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMSC313.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMSC421.value,
        "number": "CMSC421",
        "title": "Principles of Operating Systems",
        "description": """An introduction to the fundamentals of operating systems. Topics include interprocess 
        communication, process scheduling, deadlock, memory management, virtual memory, file systems and distributed 
        systems. Formal principles are illustrated with examples and case studies of one or more contemporary 
        operating systems.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMSC341.value, Course.CMSC313.value],
        "corequisites": [],
        "advisor_notes": "Recommended to NOT take this at the same time as CMSC441.",
    },
    {
        "_id": Course.CMSC441.value,
        "number": "CMSC441",
        "title": "Design and Analysis of Algorithms",
        "description": """This course studies fundamental algorithms, strategies for designing algorithms, and 
        mathematical tools for analyzing algorithms. Fundamental algorithms studied in this course include 
        algorithms for sorting and searching, hashing, and graph algorithms. Mathematical tools include asymptotic 
        notations and methods for solving recurrences. Algorithm design strategies include the greedy method, 
        divide-and-conquer, dynamic programming, and randomization.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMSC341.value, Course.STAT355.value],
        "corequisites": [],
        "advisor_notes": "Recommended to NOT take this at the same time as CMSC421.",
    },
    {
        "_id": Course.CMSC447.value,
        "number": "CMSC447",
        "title": "Software Engineering I",
        "description": """This course introduces the basic concepts of software engineering, including software life 
        cycle, requirements analysis and software design methods. Professional ethics in computer science and the 
        social impact of computing are discussed as an integral part of the software development process. Additional 
        topics may include tools for software development, software testing, software metrics and software maintenance.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.CMSC341.value],
        "corequisites": [],
        "advisor_notes": "In addition to CMSC341, you must also pass another 400-level CMSC course prior to taking this.",
    },
    {
        "_id": Course.MATH221.value,
        "number": "MATH221",
        "title": "Introduction to Linear Algebra",
        "description": """Topics of this course include: linear equations, Gauss-Jordan reduction, 
        matrices and determinants and their properties, vector spaces and subspaces, basis and 
        dimension, linear transformations, kernel and range, eigenvalues and eigenvectors, and 
        matrix diagonalization.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.MATH151.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.STAT355.value,
        "number": "STAT355",
        "title": "Introduction to Probability and Statistics for Scientists and Engineers",
        "description": """An introduction to applied statistics designed for science majors and others 
        with demonstrated quantitative ability. Topics include nature of statistical methods, random 
        variables and their distribution functions, general principles of estimation and hypothesis 
        testing. A laboratory introduces students to computer techniques in statistical analysis. Note: 
        Not open to students who have passed with a grade of ‘C’ or better or are currently taking 
        STAT 350, STAT 351, STAT 355H, STAT 453 or CMPE 320.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.MATH152.value],
        "corequisites": [],
        "advisor_notes": "Note that other prerequisites may be used, consult the course catalog.",
    },
    {
        "_id": Course.SCISEQ1.value,
        "number": "SCISEQ1",
        "title": "Science Sequence I",
        "description": "First of a two course sequence for science (i.e. CHEM101 then CHEM102).",
        "credit_hours": 4,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Prerequisites vary, generally MATH is required. Allowable sequence depends on major.",
    },
    {
        "_id": Course.SCISEQ2.value,
        "number": "SCISEQ2",
        "title": "Science Sequence II",
        "description": "Second of a two course sequence for science (i.e. CHEM101 then CHEM102).",
        "credit_hours": 4,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.SCISEQ1.value],
        "corequisites": [],
        "advisor_notes": "Allowable sequence depends on major.",
    },
    {
        "_id": Course.SCILAB1.value,
        "number": "SCILAB1",
        "title": "Science Lab",
        "description": "Science course which includes a lab.",
        "credit_hours": 2,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Prerequisites will vary. Acceptable lab courses may depend on your specific major. Consult your advisor.",
    },
    {
        "_id": Course.CMSCEL1.value,
        "number": "CMSC4XX",
        "title": "Computer Science Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. Some computer science
        electives may count for either a computer science elective or a techncial elective.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMSC341.value, Course.CMSC313.value],
        "corequisites": [],
        "advisor_notes": "Note that prerequisites will vary. Generally, CMSC313 and CMSC341 are needed. Consult your advisor.",
    },
    {
        "_id": Course.CMSCTC1.value,
        "number": "CMSCTEC",
        "title": "Computer Science Technical Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. Some computer science
        electives may count for either a computer science elective or a techncial elective. Most other options are MATH.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Note that prerequisites will vary. Generally, CMSC313 and CMSC341 are needed. Consult your advisor.",
    },
    {
        "_id": Course.ENGL100.value,
        "number": "ENGL100",
        "title": "Composition",
        "description": """A course in critical thinking, reading, and composing, with an emphasis on 
        integrating academic research and documentation. Students read and produce work for a variety 
        of purposes and audiences, focusing on strategies for researching, organizing, drafting, sharing, 
        and revising. To satisfy the composition general education requirement, this course must be taken 
        within a student’s first 30 credit hours of enrollment at UMBC. Recommended Preparation: In 
        consultation with an advisor, a student will self-place into ENGL 100. (Fall/Spring/Summer)""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPANH1.value,
        "number": "GEPARTH",
        "title": "Arts and Humanities GEP",
        "description": "Used to fulfill the Arts and Humanities GEP requirement.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPSOC1.value,
        "number": "GEPSOCS",
        "title": "Social Sciences GEP",
        "description": "Used to fulfill the Social Sciences GEP requirement.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPCUL1.value,
        "number": "GEPCULT",
        "title": "Culture GEP",
        "description": "Used to fulfill the Culture GEP requirement.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.FREEEL1.value,
        "number": "FREEELC",
        "title": "Free Elective",
        "description": "Used to reach the 120 credit hour minimum.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPLAN1.value,
        "number": "GEPLAN1",
        "title": "Elementary Foreign Language I",
        "description": "101 level language course, required for GEP.",
        "credit_hours": 4,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may test out of this with AP credits. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPLAN2.value,
        "number": "GEPLAN2",
        "title": "Elementary Foreign Language II",
        "description": "102 level language course, required for GEP.",
        "credit_hours": 4,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [Course.GEPLAN1.value],
        "corequisites": [],
        "advisor_notes": "You may test out of this with AP credits. Consult your advisor.",
    },
    {
        "_id": Course.GEPLAN3.value,
        "number": "GEPLAN3",
        "title": "Intermediate Foreign Language I",
        "description": "201 level language course, required for GEP.",
        "credit_hours": 4,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [Course.GEPLAN2.value],
        "corequisites": [],
        "advisor_notes": "You may test out of this with AP credits. Consult your advisor.",
    },
    {
        "_id": Course.CMSCEL2.value,
        "number": "CMSC4XX",
        "title": "Computer Science Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. Some computer science
        electives may count for either a computer science elective or a techncial elective.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMSC341.value, Course.CMSC313.value],
        "corequisites": [],
        "advisor_notes": "Note that prerequisites will vary. Generally, CMSC313 and CMSC341 are needed. Consult your advisor.",
    },
    {
        "_id": Course.CMSCTC2.value,
        "number": "CMSCTEC",
        "title": "Computer Science Technical Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. Some computer science
        electives may count for either a computer science elective or a techncial elective. Most other options are MATH.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Note that prerequisites will vary. Generally, CMSC313 and CMSC341 are needed. Consult your advisor.",
    },
    {
        "_id": Course.CMSCTC3.value,
        "number": "CMSCTEC",
        "title": "Computer Science Technical Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. Some computer science
        electives may count for either a computer science elective or a techncial elective. Most other options are MATH.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Note that prerequisites will vary. Generally, CMSC313 and CMSC341 are needed. Consult your advisor.",
    },
    {
        "_id": Course.FREEEL2.value,
        "number": "FREEELC",
        "title": "Free Elective",
        "description": "Used to reach the 120 credit hour minimum.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.FREEEL3.value,
        "number": "FREEELC",
        "title": "Free Elective",
        "description": "Used to reach the 120 credit hour minimum.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.FREEEL4.value,
        "number": "FREEELC",
        "title": "Free Elective",
        "description": "Used to reach the 120 credit hour minimum.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.FREEEL5.value,
        "number": "FREEELC",
        "title": "Free Elective",
        "description": "Used to reach the 120 credit hour minimum.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.FREEEL6.value,
        "number": "FREEELC",
        "title": "Free Elective",
        "description": "Used to reach the 120 credit hour minimum.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPANH2.value,
        "number": "GEPARTH",
        "title": "Arts and Humanities GEP",
        "description": "Used to fulfill the Arts and Humanities GEP requirement.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPANH3.value,
        "number": "GEPARTH",
        "title": "Arts and Humanities GEP",
        "description": "Used to fulfill the Arts and Humanities GEP requirement.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPSOC2.value,
        "number": "GEPSOCS",
        "title": "Social Sciences GEP",
        "description": "Used to fulfill the Social Sciences GEP requirement.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPSOC3.value,
        "number": "GEPSOCS",
        "title": "Social Sciences GEP",
        "description": "Used to fulfill the Social Sciences GEP requirement.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
    },
    {
        "_id": Course.GEPCUL2.value,
        "number": "GEPCULT",
        "title": "Culture GEP",
        "description": "Used to fulfill the Culture GEP requirement.",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": True,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You may be able to use AP credits for this. Consult your advisor or check your degree audit.",
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
        "_id": Major.CMSC.value,
        "name": "Computer Science B.S.",
        "number_credits": 12,
        "default_plan": {
            Course.MATH151.value: {"year": 1, "session": "Fall"},
            Course.GEPLAN1.value: {"year": 1, "session": "Fall"},
            Course.ENGL100.value: {"year": 1, "session": "Fall"},
            Course.CMSC201.value: {"year": 1, "session": "Fall"},
            Course.CMSC202.value: {"year": 1, "session": "Spring"},
            Course.CMSC203.value: {"year": 1, "session": "Spring"},
            Course.MATH152.value: {"year": 1, "session": "Spring"},
            Course.GEPLAN2.value: {"year": 1, "session": "Spring"},
            Course.CMSC331.value: {"year": 2, "session": "Fall"},
            Course.CMSC341.value: {"year": 2, "session": "Fall"},
            Course.SCISEQ1.value: {"year": 2, "session": "Fall"},
            Course.GEPLAN3.value: {"year": 2, "session": "Fall"},
            Course.FREEEL3.value: {"year": 2, "session": "Fall"},
            Course.CMSC313.value: {"year": 2, "session": "Spring"},
            Course.MATH221.value: {"year": 2, "session": "Spring"},
            Course.SCISEQ2.value: {"year": 2, "session": "Spring"},
            Course.SCILAB1.value: {"year": 2, "session": "Spring"}, 
            Course.GEPANH1.value: {"year": 2, "session": "Spring"}, 
            Course.CMSC304.value: {"year": 3, "session": "Fall"},
            Course.CMSC411.value: {"year": 3, "session": "Fall"},
            Course.CMSCEL1.value: {"year": 3, "session": "Fall"},
            Course.STAT355.value: {"year": 3, "session": "Fall"},
            Course.GEPSOC1.value: {"year": 3, "session": "Fall"},
            Course.CMSC421.value: {"year": 3, "session": "Spring"},
            Course.CMSCEL2.value: {"year": 3, "session": "Spring"},
            Course.CMSCTC1.value: {"year": 3, "session": "Spring"},
            Course.GEPANH2.value: {"year": 3, "session": "Spring"}, 
            Course.GEPSOC2.value: {"year": 3, "session": "Spring"},
            Course.CMSC441.value: {"year": 4, "session": "Fall"},
            Course.CMSC447.value: {"year": 4, "session": "Fall"},
            Course.GEPCUL1.value: {"year": 4, "session": "Fall"},
            Course.GEPSOC3.value: {"year": 4, "session": "Fall"},
            Course.GEPANH3.value: {"year": 4, "session": "Fall"},
            Course.CMSCTC2.value: {"year": 4, "session": "Spring"},
            Course.CMSCTC3.value: {"year": 4, "session": "Spring"},
            Course.GEPCUL2.value: {"year": 4, "session": "Spring"},
            Course.FREEEL1.value: {"year": 4, "session": "Spring"}, 
            Course.FREEEL2.value: {"year": 4, "session": "Spring"},          
        }
    },
    {
        "_id": Major.ENME.value,
        "name": "Mechanical Engineering B.S.",
        "number_credits": 19,
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
        "major_id": Major.CMSC.value,
        "custom_plan": {}
    },
    {
        "_id": 1001,
        "email": "cdollo1@umbc.edu",
        "major_id": Major.ENME.value,
        "custom_plan": {}
    },
]
