import { useState } from "react";
import PropTypes from "prop-types";
import { useDroppable } from "@dnd-kit/core";
import { cloneDeep } from "lodash";
import DraggableCourse from "../DraggableCourse/DraggableCourse.jsx";
import CoursePopUp from "../CoursePopup/CoursePopUp.jsx";
import "./Session.css";

/**
 * Session component
 * This component represents a session of the four year plan
 * It establishes a droppable area using the dnd-kit useDroppable hook
 * and renders its courses via the DraggableCourse component.
 * Clicking on a course opens a CoursePopUp
 * 
 * Props:
 * - semester (string, required): Identifier for the session
 * - session_title (string, required): Title of the session
 * - courses (array, required): An array of course objects
 * 
 * Return:
 * A section containing the session name and a droppable area that lists all its courses
 */

const Session = ({ semester, session_title, courses }) => {
    // state to keep track of selected course for popup details
    const [selectedCourse, setSelectedCourse] = useState(null);

    // Set up a droppable container with the given semester id
    const { setNodeRef, isOver } = useDroppable({ id: semester });

    // Clone courses to ensure immutability
    const clonedCourses = cloneDeep(courses);

    return (
        <>
            <div className="session">
                <div className="session-name ${session_title}" >{session_title}</div>
                <div
                    ref={setNodeRef}
                    className={`session-courses ${isOver ? 'droppable-over' : ''}`}>

                    {Array.isArray(clonedCourses) && clonedCourses.length === 0 ? (
                        <div className="no-courses-added">No courses were added to this session. <br /> <br /> Add or drag a course</div>
                    ) : (
                        clonedCourses.map((course, index) => (
                            <DraggableCourse
                                key={index}
                                course={course}
                                semester={semester}
                                index={index}
                                onClick={() => setSelectedCourse(cloneDeep(course))}
                            />
                        ))
                    )
                    }
                </div>
            </div>

            {selectedCourse && (
                <CoursePopUp
                    courseId={selectedCourse.id}
                    onClose={() => setSelectedCourse(null)}
                />
            )}
        </>
    );
};
// PropTypes for type safety
Session.propTypes = {
    semester: PropTypes.string.isRequired,
    session_title: PropTypes.string.isRequired,
    courses: PropTypes.arrayOf(
        PropTypes.shape({
            id: PropTypes.number.isRequired,
            number: PropTypes.string.isRequired,
            credit_hours: PropTypes.number.isRequired,
            prerequisites: PropTypes.arrayOf(PropTypes.number).isRequired,
            corequisites: PropTypes.arrayOf(PropTypes.number).isRequired,
        })
    ).isRequired,
};

export default Session;