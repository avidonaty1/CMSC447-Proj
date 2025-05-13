
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
    CMPE_COMM = 3


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
    CHEM101 = 145
    CHEM102 = 146
    CHEM102L = 147
    ENME220 = 148
    MATH251 = 149
    ENME221 = 150
    MATH225 = 151
    ENME204 = 152
    ENME217 = 153
    CMPE306 = 154
    ENME320 = 155
    ENME303 = 156
    ENME301 = 157
    ENME304 = 158
    ENME321 = 159
    ENME360 = 160
    ENME332L = 161
    ENME403 = 162
    ENME432L = 163
    ENMETEC = 164
    ENMESCI = 165
    ENMEDES = 166
    ENME482L = 167
    ENME444 = 168
    PHYS122 = 169
    CMPE310 = 170
    CMPE311 = 171
    CMPE314 = 172
    CMPE320 = 173
    CMPE349 = 174
    CMPE450 = 175
    CMPE451 = 176
    CMPE323 = 177
    CMPE330 = 178
    CMPETC1 = 179
    CMPETC2 = 180
    CMPETC3 = 181
    CMPE212 = 182


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
        "credit_hours": 3,
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
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Prerequisite is CMSC313 OR (CMPE212 and CMPE310)",
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
        "prerequisites": [Course.CMSC341.value],
        "corequisites": [],
        "advisor_notes": """Second prerequisite is either CMSC313 or (CMPE212 and CMPE310). 
        Recommended to NOT take this at the same time as CMSC441.""",
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
        "number": "AH GEP ",
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
        "number": "SS GEP ",
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
        "title": "C GEP  ",
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
        "number": "LANG101",
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
        "number": "LANG102",
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
        "number": "LANG201",
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
        "number": "AH GEP ",
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
        "number": "AH GEP ",
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
        "number": "SS GEP ",
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
        "number": "SS GEP ",
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
        "number": "C GEP  ",
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
        "_id": Course.CHEM101.value,
        "number": "CHEM101",
        "title": "Principles of Chemistry I",
        "description": """An introduction to chemistry for science majors and other students who require a thorough grounding 
        in the principles of chemistry. Topics treated include the atomic-molecular theory of matter, stoichiometry, states of 
        matter, chemical nomenclature, energetics of chemical and physical processes, solutions, periodic properties, VSEPR, 
        molecular orbital theory and chemistry of familiar elements. 
        Note: Credit may not be obtained for both CHEM 101 and CHEM 123.""",
        "credit_hours": 4,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "You must take MATH106 as a prerequisite, or more likely MATH151 (or test out of MATH).",
    },
    {
        "_id": Course.CHEM102.value,
        "number": "CHEM102",
        "title": "Principles of Chemistry II",
        "description": """Principles of chemical and physical equilibrium, liquids and solids, elementary thermodynamics, 
        electron and proton transfer reactions, electrochemistry, chemical kinetics and a further study of the periodic 
        properties of the elements. (Fall/Spring/Summer)""",
        "credit_hours": 4,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CHEM101.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CHEM102L.value,
        "number": "CHEM102L",
        "title": "Introductory Chemistry Lab I",
        "description": """Companion course to CHEM 102, intended for all students who require two or more years of 
        chemistry. (Fall/Spring/Summer)""",
        "credit_hours": 2,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CHEM101.value],
        "corequisites": [Course.CHEM102.value],
        "advisor_notes": "None",
    },
    {
        "_id": Course.MATH225.value,
        "number": "MATH225",
        "title": "Introduction to Differential Equations",
        "description": """Topics of this course include solutions of first- and second order linear differential equations, 
        non-linear exact and separable equations, integrating factors, homogeneous equations, higher-order linear equations, 
        initial and boundary value problems, solutions as functions of the equation parameters, Laplace transforms, power 
        series solutions for Bessel and Legendre equations, difference equations and numerical methods.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.MATH152.value],
        "corequisites": [],
        "advisor_notes": "Recommended to take MATH251 first.",
    },
    {
        "_id": Course.MATH251.value,
        "number": "MATH251",
        "title": "Multivariable Calculus",
        "description": """Topics of this course include parametric and polar functions, vectors, lines, planes and surfaces 
        in three dimensions, vector functions and their derivatives, partial derivatives, gradients, directional derivatives, 
        maxima, minima, and Lagrange multipliers, multiple integrals, area, volume, surface area, integration in different 
        coordinate systems, line integral, and the Green’s, Stokes, and divergence theorems. """,
        "credit_hours": 4,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.MATH151.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.PHYS122.value,
        "number": "PHYS122",
        "title": "Introductory Physics II",
        "description": """This is the second-semester introductory calculus-based physics course. Topics include thermodynamics, 
        electricity, DC circuits, and magnetism. This course consists of lectures and discussions. (Fall/Spring)""",
        "credit_hours": 4,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.PHYS121.value],
        "corequisites": [Course.MATH152.value],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMPE306.value,
        "number": "CMPE306",
        "title": "Introductory Circuit Theory",
        "description": """This course introduces the fundamental linear passive elements of resistance, capacitance, inductance 
        and the physical basis for their current voltage characteristics. It covers the basic analysis of circuits with these 
        linear passive elements including Kirchoff’s laws, node and mesh analysis and a solution of the resulting circuit 
        differential equations for transient and steady-state responses. The frequency domain description of circuit analysis 
        is introduced. The operational amplifier and circuits using these components is covered. The basics of magnetic induction 
        and transformers in linear circuits are discussed. The course includes a laboratory in which the student designs and makes 
        measurements on simple test circuits using both real components and PSPICE simulation.""",
        "credit_hours": 4,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.PHYS122.value],
        "corequisites": [Course.MATH225.value],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME204.value,
        "number": "ENME204",
        "title": "Introduction to Engineering Design with CAD",
        "description": """Sophomores are introduced to engineering design using the science and tools (CAD) of prior 
        courses. The course will cover design specifications, design analysis, performance predictions, design, changes, 
        final design and operation specifications. Students will be required to make written and oral presentations and 
        produce a design report.""",
        "credit_hours": 3,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENES101.value, Course.ENGL100.value, Course.ENME220.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME217.value,
        "number": "ENME217",
        "title": "Engineering Thermodynamics",
        "description": """Properties, characteristics and fundamental equations of state of materials, work and heat transfer. 
        First and second laws of thermodynamics, thermodynamic power and refrigeration cycles, gas/vapor mixtures and psychrometrics.""",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENME110.value, Course.MATH152.value, Course.PHYS121.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME220.value,
        "number": "ENME220",
        "title": "Mechanics of Materials",
        "description": """Mechanics of Materials is a fundamental course on the mechanical behavior of deformable bodies under 
        axial loads, torsion, flexure, and combined loads. The concepts of stress, strain, and material properties are introduced 
        and used to relate external forces with the resulting internal forces and deformation of a body. Practical applications 
        involving the design of mechanical and structural elements under various load conditions are emphasized.""",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENME110.value, Course.MATH152.value, Course.PHYS121.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME221.value,
        "number": "ENME221",
        "title": "Dynamics",
        "description": """Study of objects in motion. Objects are approximated first as particles and then as rigid bodies. 
        In both cases, the kinematic relationships are derived first. Kinetics is studied from three perspectives: force-acceleration, 
        work energy and impulse-momentum.""",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENME110.value, Course.MATH152.value, Course.PHYS121.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME301.value,
        "number": "ENME301",
        "title": "The Structure and Properties of Engineering Materials",
        "description": """The nature and properties of engineering materials as related to their use in all phases of mechanical 
        engineering will be studied. Materials covered include metals, ceramics and glasses, polymer and composites.""",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CHEM102.value, Course.CHEM102L.value, Course.ENME220.value, Course.PHYS122.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME303.value,
        "number": "ENME303",
        "title": "Computational Methods for Engineers",
        "description": """This course is an introduction to programming using MATLAB, elements of linear algebra, computational methods, 
        and their application to solving engineering and specific problems through computational programming.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENME220.value, Course.ENME221.value, Course.MATH225.value, Course.MATH251.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME304.value,
        "number": "ENME304",
        "title": "Machine Design",
        "description": """In-depth design course that is a follow-up to ENME 204. The focus here is on designing machine components. 
        Emphasis is on kinematics, working stresses, repeated loadings, fatigue and heating effects. The course requires completion 
        of a design project and the use of such computational tools as CAD and engineering codes.""",
        "credit_hours": 3,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.ENME204.value],
        "corequisites": [],
        "advisor_notes": "Major component of the course is a group project.",
    },
    {
        "_id": Course.ENME320.value,
        "number": "ENME320",
        "title": "Fluid Mechanics",
        "description": """Fluid flow concepts and basic equations, effects of viscosity and compressibility, dimensional analysis 
        and laws of similarity, flow through pipes and over-immersed bodies, and principles of flow measurement.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENME217.value, Course.ENME220.value, Course.ENME221.value, Course.MATH225.value, Course.MATH251.value],
        "corequisites": [],
        "advisor_notes": "Some students find this course very difficult.",
    },
    {
        "_id": Course.ENME321.value,
        "number": "ENME321",
        "title": "Transfer Processes",
        "description": """Conduction by steady state and transient heat flow; laminar and turbulent flow; free and forced convection; 
        radiation, evaporation and condensation of vapors; and transfer of mass, heat and momentum.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENME320.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME332L.value,
        "number": "ENME332L",
        "title": "Solid Mechanics and Materials Laboratory",
        "description": """TA laboratory course in testing mechanical properties of materials. Emphasis will be on experimental 
        techniques in solid mechanics, strain gages, strain gage rosettes, photoelasticity, acoustic emissions, metallurgical and 
        electron microscopy.""",
        "credit_hours": 3,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENGL100.value, Course.ENME220.value, Course.ENME301.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME360.value,
        "number": "ENME360",
        "title": "Vibrations",
        "description": """Dynamic characteristics of machinery with emphasis on systems with single and multiple degrees of freedom.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENME220.value, Course.ENME221.value, Course.ENME303.value, Course.MATH225.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME403.value,
        "number": "ENME403",
        "title": "Automatic Controls",
        "description": """Hydraulic, electrical, mechanical and pneumatic automatic control systems; open and closed loops; 
        steady-state and transient operations; stability criteria; linear and non-linear systems; and Laplace transforms.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.CMPE306.value],
        "corequisites": [Course.ENME360.value],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME432L.value,
        "number": "ENME432L",
        "title": "Fluids/Energy Laboratory",
        "description": """Measurement of fluid properties, fluid forces and observation of flow phenomenon; demonstration of 
        flow measurement techniques; and measurement of heat-transfer properties: conduction, convection and radiation; and 
        condensation and evaporation measurements.""",
        "credit_hours": 2,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENGL100.value, Course.ENME320.value, Course.ENME321.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENME444.value,
        "number": "ENME444",
        "title": "Mechanical Engineering Systems Design",
        "description": """This course allows students completing the Mechanical Engineering curriculum to engage in a complete 
        system design experience, integrating the various technical concepts they have learned in prior courses and is the last 
        in a sequence of design courses that are an integral component of the undergraduate program. The course imparts a foundation 
        in team leadership and project management and emphasizes entrepreneurial skills necessary to function in any organization, 
        regardless of size. Engineers in industry solve problems that simultaneously resolve budgetary, time, technical and sometimes 
        social, ethical and environmental constraints. Students will enjoy an experience that closely matches this environment.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.ENME360.value],
        "corequisites": [],
        "advisor_notes": "You must take all 300-level ENME required courses first. This is the capstone project course.",
    },
    {
        "_id": Course.ENME482L.value,
        "number": "ENME482L",
        "title": "Vibrations/Controls Laboratory",
        "description": """Methods and instrumentation for determining the vibration properties of mechanical systems. 
        Various methods of spectral and modal analysis. Open-and closed-loop control experiments.""",
        "credit_hours": 2,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [Course.ENME360.value, Course.ENME403.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.ENMEDES.value,
        "number": "ENMEDES",
        "title": "Mechanical Engineering 400-level Design Elective",
        "description": """Check the course catalog and degree audit for acceptable courses.""",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Prerequisites will vary: generally at least one 300-level ENME course.",
    },
    {
        "_id": Course.ENMETEC.value,
        "number": "ENMETEC",
        "title": "Mechanical Engineering 400-level Technical Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. ENME Design Electives
        may also be used to fulfill this requirement.""",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Prerequisites will vary: generally at least one 200-level ENME course.",
    },
    {
        "_id": Course.ENMESCI.value,
        "number": "ENMESCI",
        "title": "Mechanical Engineering science/Technical Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. ENME Design or Technical
        Electives may also be used to fulfill this requirement.""",
        "credit_hours": 3,
        "fills_up_quickly": RARELY,
        "offered_winter": False,
        "offered_summer": True,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Prerequisites will vary. Courses may be outside the ENME discipline.",
    },
    {
        "_id": Course.CMPE310.value,
        "number": "CMPE310",
        "title": "Systems Design and Programming",
        "description": """This course provides computer engineering students with system design software and hardware experience. 
        This course covers hardware features that support advanced process and memory management in modern architectures such as 
        the Pentium. The details of the entire chipset for 8086 are covered, including topics related to the register architecture, 
        machine language, clock generator, bus controller and memory, I/O and interrupt interface. Other details of a complete 
        computer system are discussed, including I/O bus protocols and support chips, memory chips, interrupt handler hardware 
        and external support chips for disk storage, video and direct memory access. This course includes a laboratory that 
        focuses on assembly language programming and board design software.""",
        "credit_hours": 4,
        "fills_up_quickly": ALWAYS,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [],
        "corequisites": [Course.CMSC203.value],
        "advisor_notes": "Prerequisite is CMPE Gateway. See course catalog for more details.",
    },
    {
        "_id": Course.CMPE311.value,
        "number": "CMPE311",
        "title": "C Programming and Embedded Systems",
        "description": """In this course, students learn about hardware and software aspects of embedded systems. Students 
        learn C programming language through use in an embedded platform. The course builds on CMPE 310, introducing advanced 
        topics including communication interfaces, advanced IO devices and other peripherals, multitasking, firmware, real-time 
        operating systems/embedded operating systems and device drivers. The course will provide a hands-on experience in 
        designing and programming an embedded system using a microcontroller-based development platform.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.CMPE310.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMPE314.value,
        "number": "CMPE314",
        "title": "Principles of Electronic Circuits",
        "description": """A brief overview of semi-conductor devices and technology. The basic physical operation of PN-junction 
        diodes, junction field effect transistors, MOSFETs and bipolar transistors. The corresponding small signal AC models. 
        Basic transistor circuit configurations (CE, CC CB, CS, CD, CG). DC bias. Small signal analysis. Simple multi-transistor 
        circuits: diffamp, operational amplifier and current mirror frequency response. In addition to the lectures, there is 
        a laboratory associated with the course. You must have passed the Computer Engineering Gateway to get into this class.""",
        "credit_hours": 4,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.CMPE306.value, Course.MATH225.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMPE320.value,
        "number": "CMPE320",
        "title": "Probability, Statistics, and Random Processes",
        "description": """This course presents the fundamental concepts of probability, statistics and random processes from a 
        computer and electrical engineering perspective, emphasizing applications in communications, signal processing, and 
        machine learning. Students will learn basic methods to analyze and model the probabilistic behavior of engineering 
        systems and to analyze experimental data associated with such systems. A brief use-driven introduction of multivariate 
        calculus concepts will be provided. (Spring)""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.MATH152.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMPE349.value,
        "number": "CMPE349",
        "title": "Introduction to Professional Practice",
        "description": """This course covers a wide range of professional practice topics, including basic systems engineering 
        practices, basic project management, introduction to entrepreneurship, and professional ethics. The classroom environment 
        simulates the professional/entrepreneurial workplace. Students are required to develop and write various technical documents, 
        including project plans, specifications, and other professional documents. Professional practice experience includes 
        real-world workplace ethics and behaviors. Note: Completion of the Computer Engineering Gateway required. This class is 
        intended to be taken the semester before enrolling in CMPE 450.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.CMPE212.value, Course.CMSC201.value, Course.MATH151.value, Course.ENES101.value, Course.ENGL100.value,
                          Course.PHYS121.value, Course.PHYS122.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMPE450.value,
        "number": "CMPE450",
        "title": "Capstone I",
        "description": """This is the first half of a two-semester capstone experience, taken in consecutive Fall and Spring semesters. 
        Students to engage in a complete project design experience over two semesters, integrating the technical concepts learned in 
        prior courses. Entrepreneurship, team leadership and project management skills are emphasized. Students function in a 
        classroom environment that closely simulates professional and entrepreneurial practice including budgetary, time, technical 
        and sometimes social, ethical and environmental constraints. (Fall)""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.CMPE314.value, Course.CMPE349.value, Course.CMSC341.value],
        "corequisites": [Course.CMPE311.value],
        "advisor_notes": "See course catalog for additional prerequisite information.",
    },
    {
        "_id": Course.CMPE451.value,
        "number": "CMPE451",
        "title": "Capstone II",
        "description": """This is the second half of a two-semester capstone experience, taken in consecutive Fall and Spring 
        semesters. Students to engage in a complete project design experience over two semesters, integrating the technical 
        concepts learned in prior courses. Entrepreneurship, team leadership and project management skills are emphasized. 
        Students function in a classroom environment that closely simulates professional and entrepreneurial practice including 
        budgetary, time, technical and sometimes social, ethical and environmental constraints.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.CMPE311.value, Course.CMPE450.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMPE323.value,
        "number": "CMPE323",
        "title": "Signal and Systems Theory",
        "description": """This course covers basic linear signal and system theory from both continuous-time and discrete-time 
        perspectives, covering linear, time-invariant systems, impulse response, Fourier Series and Transforms including the 
        Discrete Fourier Transform and Fast Fourier Transform, transfer functions, discrete and continuous time filters, 
        Laplace transforms and Z transforms. The course includes discussion and lab sections that focus on the use of MATLAB 
        to solve and visualize problems that apply the theory discussed in lecture. Note: Completion of the Computer 
        Engineering Gateway required. (Fall)""",
        "credit_hours": 4,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.PHYS121.value, Course.PHYS122.value, Course.CMPE212.value, Course.CMSC201.value, Course.MATH151.value,
                          Course.CMPE306.value, Course.ENES101.value, Course.MATH225.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMPE330.value,
        "number": "CMPE330",
        "title": "Electromagnetic Waves and Transmission",
        "description": """This course provides an introduction to waves, transmission lines, and electromagnetics with the focus 
        on computer engineering and communications applications. The physical limits on Kirchoff’s Laws are discussed, along with 
        the following topics: a review of phasor and vector quantities; transmission lines in the time domain and the frequency 
        domain; electrostatics, magnetostatics, and the calculation of the capacitance and inductance in transmission lines;  
        time-varying electromagnetic fields; the integral, differential, and phasor forms of Maxwell’s equations; plane waves 
        and polarization effects, including transmission and reflection from surfaces; and an introduction to waveguides. 
        Note: Completion of the Computer Engineering Gateway required.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [Course.PHYS121.value, Course.PHYS122.value, Course.CMPE212.value, Course.CMSC201.value, Course.MATH151.value,
                          Course.CMPE306.value, Course.ENES101.value, Course.MATH225.value],
        "corequisites": [],
        "advisor_notes": "None",
    },
    {
        "_id": Course.CMPETC1.value,
        "number": "CMPETC1",
        "title": "Computer Engineering Technical Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. Options will depend on track.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Prerequisites will vary; generally requires at least one 300 level CMPE course.",
    },
    {
        "_id": Course.CMPETC2.value,
        "number": "CMPETC2",
        "title": "Computer Engineering Technical Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. Options will depend on track.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Prerequisites will vary; generally requires at least one 300 level CMPE course.",
    },
    {
        "_id": Course.CMPETC3.value,
        "number": "CMPETC3",
        "title": "Computer Engineering Technical Elective",
        "description": """Check the course catalog and degree audit for acceptable courses. Options will depend on track.""",
        "credit_hours": 3,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [],
        "corequisites": [],
        "advisor_notes": "Prerequisites will vary; generally requires at least one 300 level CMPE course.",
    },
    {
        "_id": Course.CMPE212.value,
        "number": "CMPE212",
        "title": "Principles of Digital Design",
        "description": """This course introduces students to the science of digital design. The topics covered include 
        Boolean algebra; logic theorems; logic circuits and methods for their simplification, including Karnaugh maps 
        and the Quine-McCluskey algorithm; combinational design; electrical characteristics of gates, timing, races and 
        hazards; sequential circuits, their specification via state machines and minimization; principles of register 
        transfer notation; exposure to hardware description language(s); and synthesis tools. This course 
        includes a laboratory.""",
        "credit_hours": 4,
        "fills_up_quickly": SOMETIMES,
        "offered_winter": False,
        "offered_summer": False,
        "prerequisites": [],
        "corequisites": [],
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
        "_id": Major.CMSC.value,
        "name": "Computer Science B.S.",
        "number_credits": 122,
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
        "number_credits": 127,
        "default_plan": {
            Course.CHEM101.value: {"year": 1, "session": "Fall"},
            Course.MATH151.value: {"year": 1, "session": "Fall"},
            Course.ENES101.value: {"year": 1, "session": "Fall"},
            Course.ENGL100.value: {"year": 1, "session": "Fall"},
            Course.GEPANH1.value: {"year": 1, "session": "Fall"},
            Course.CHEM102.value: {"year": 1, "session": "Spring"},
            Course.CHEM102L.value: {"year": 1, "session": "Spring"},
            Course.PHYS121.value: {"year": 1, "session": "Spring"},
            Course.MATH152.value: {"year": 1, "session": "Spring"},
            Course.ENME110.value: {"year": 1, "session": "Spring"},
            Course.ENME220.value: {"year": 2, "session": "Fall"},
            Course.STAT355.value: {"year": 2, "session": "Fall"},
            Course.MATH251.value: {"year": 2, "session": "Fall"},
            Course.PHYS122.value: {"year": 2, "session": "Fall"},
            Course.GEPLAN1.value: {"year": 2, "session": "Fall"},
            Course.ENME221.value: {"year": 2, "session": "Spring"},
            Course.MATH225.value: {"year": 2, "session": "Spring"},
            Course.ENME204.value: {"year": 2, "session": "Spring"},
            Course.ENME217.value: {"year": 2, "session": "Spring"},
            Course.GEPANH2.value: {"year": 2, "session": "Spring"},
            Course.GEPLAN2.value: {"year": 2, "session": "Spring"}, 
            Course.CMPE306.value: {"year": 3, "session": "Fall"},
            Course.ENME320.value: {"year": 3, "session": "Fall"},
            Course.ENME303.value: {"year": 3, "session": "Fall"},
            Course.ENME301.value: {"year": 3, "session": "Fall"},
            Course.GEPSOC1.value: {"year": 3, "session": "Fall"},
            Course.ENME304.value: {"year": 3, "session": "Spring"},
            Course.ENME321.value: {"year": 3, "session": "Spring"},
            Course.ENME360.value: {"year": 3, "session": "Spring"},
            Course.ENME332L.value: {"year": 3, "session": "Spring"}, 
            Course.GEPLAN3.value: {"year": 3, "session": "Spring"},
            Course.ENME403.value: {"year": 4, "session": "Fall"},
            Course.ENME432L.value: {"year": 4, "session": "Fall"},
            Course.ENMETEC.value: {"year": 4, "session": "Fall"},
            Course.ENMESCI.value: {"year": 4, "session": "Fall"},
            Course.GEPANH3.value: {"year": 4, "session": "Fall"},
            Course.GEPSOC2.value: {"year": 4, "session": "Fall"},
            Course.ENME482L.value: {"year": 4, "session": "Spring"},
            Course.ENME444.value: {"year": 4, "session": "Spring"},
            Course.ENMEDES.value: {"year": 4, "session": "Spring"},
            Course.GEPSOC3.value: {"year": 4, "session": "Spring"}, 
            Course.GEPCUL1.value: {"year": 4, "session": "Spring"},          
        }
    },
        {
        "_id": Major.CMPE_COMM.value,
        "name": "Computer Engineering B.S., Communications Track",
        "number_credits": 128,
        "default_plan": {
            Course.MATH151.value: {"year": 1, "session": "Fall"},
            Course.GEPLAN1.value: {"year": 1, "session": "Fall"},
            Course.ENGL100.value: {"year": 1, "session": "Fall"},
            Course.CMSC201.value: {"year": 1, "session": "Fall"},
            Course.PHYS121.value: {"year": 1, "session": "Fall"},
            Course.CMSC202.value: {"year": 1, "session": "Spring"},
            Course.CMPE212.value: {"year": 1, "session": "Spring"},
            Course.MATH152.value: {"year": 1, "session": "Spring"},
            Course.ENES101.value: {"year": 1, "session": "Spring"},
            Course.GEPLAN2.value: {"year": 1, "session": "Spring"},
            Course.MATH251.value: {"year": 2, "session": "Fall"},
            Course.CMSC203.value: {"year": 2, "session": "Fall"},
            Course.PHYS122.value: {"year": 2, "session": "Fall"},
            Course.GEPANH1.value: {"year": 2, "session": "Fall"},
            Course.GEPSOC1.value: {"year": 2, "session": "Fall"},
            Course.CMPE306.value: {"year": 2, "session": "Spring"},
            Course.MATH225.value: {"year": 2, "session": "Spring"},
            Course.CMPE310.value: {"year": 2, "session": "Spring"},
            Course.CMSC341.value: {"year": 2, "session": "Spring"}, 
            Course.CMPE314.value: {"year": 3, "session": "Fall"},
            Course.CMPE311.value: {"year": 3, "session": "Fall"},
            Course.CMPE323.value: {"year": 3, "session": "Fall"},
            Course.MATH221.value: {"year": 3, "session": "Fall"},
            Course.SCISEQ1.value: {"year": 3, "session": "Fall"},
            Course.CMPE320.value: {"year": 3, "session": "Spring"},
            Course.CMPE330.value: {"year": 3, "session": "Spring"},
            Course.CMPE349.value: {"year": 3, "session": "Spring"},
            Course.GEPANH2.value: {"year": 3, "session": "Spring"}, 
            Course.GEPCUL1.value: {"year": 3, "session": "Spring"},
            Course.CMSC411.value: {"year": 4, "session": "Fall"},
            Course.CMPE450.value: {"year": 4, "session": "Fall"},
            Course.CMPETC1.value: {"year": 4, "session": "Fall"},
            Course.CMPETC2.value: {"year": 4, "session": "Fall"},
            Course.GEPANH3.value: {"year": 4, "session": "Fall"},
            Course.GEPSOC2.value: {"year": 4, "session": "Fall"},
            Course.CMSC421.value: {"year": 4, "session": "Spring"},
            Course.CMPE451.value: {"year": 4, "session": "Spring"},
            Course.CMPETC3.value: {"year": 4, "session": "Spring"},
            Course.GEPLAN3.value: {"year": 4, "session": "Spring"}, 
            Course.GEPSOC3.value: {"year": 4, "session": "Spring"},          
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
]
