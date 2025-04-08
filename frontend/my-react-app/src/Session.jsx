import { useState } from "react";
import CoursePopUp from "./CoursePopUp";

function Session({semester, session_title, courses}){

    console.log(semester)

    const [selectedCourse, setSelectedCourse] = useState(null);

    return(
        <>
            <div className="session">
                <div className="session-name">{session_title}</div>
                <div className="session-courses">
                    {courses.length === 0 ? (
                        <div className="no-courses-added">No courses were added to this session.</div>
                        ) : (
                        courses.map((course, index) => (
                            <div 
                                key={index} 
                                className="course"
                                onClick={() => {
                                    console.log(`Course clicked: ${course}`);
                                    setSelectedCourse(course);
                                }}
                                >
                                    {course}
                                    
                            </div>
                            ))
                        )
                    }
                </div>
            </div>

            {selectedCourse && (
                <CoursePopUp
                    courseName={selectedCourse}
                    onClose={() => setSelectedCourse(null)}
                />
            )}
        </>
    )
}

export default Session