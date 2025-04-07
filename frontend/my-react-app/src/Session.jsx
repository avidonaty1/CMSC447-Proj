function Session({semester, session_title, courses}){

    console.log(semester)

    return(
        <>
            <div className="session">
                <div className="session-name">{session_title}</div>
                <div className="session-courses">
                {courses.length === 0 ? (
                    <div className="no-courses-added">No courses were added to this session.</div>
                    ) : (
                    courses.map((course, index) => (
                        <div key={index} className="course">
                        {course}
                        </div>
                    ))
                    )}
                </div>
            </div>
        </>
    )
}

export default Session