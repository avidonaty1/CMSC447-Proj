import { useState, useEffect } from "react";
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
    // State to keep track of selected course for popup details
    const [selectedCourse, setSelectedCourse] = useState(null);

    // State to keep track of alert for excess credit
    const [alertDisplayed, setAlertDisplayed] = useState(false);

    // Set up a droppable container with the given semester id
    const { setNodeRef, isOver } = useDroppable({ id: semester });

    // Clone courses to ensure immutability
    const clonedCourses = cloneDeep(courses);
    // Calculate the total credits for the courses
    const totalCredits = clonedCourses.reduce((sum, course) => sum + course.credit_hours, 0);

    // Convert session_title to uppercase to use for credit limit chacking
    const upperCaseTitle = session_title.toUpperCase();

    // UseEffect to trigger alert if credit limit for session is exceeded
    useEffect(() => {
        if (!alertDisplayed) {
            if (totalCredits > 19 && (upperCaseTitle === "FALL" || upperCaseTitle === "SPRING")) {
                alert(
                    "Warning: Credit limit exceeded. You would need to fill out an excess credit form. Consider rescheduling courses."
                );
                setAlertDisplayed(true);
            } else if (upperCaseTitle === "SUMMER" && totalCredits > 8) {
                alert(
                    "Warning: Credit limit exceeded. You would need to fill out an excess credit form. Consider rescheduling courses."
                );
                setAlertDisplayed(true);
            }
            else if (upperCaseTitle === "WINTER" && totalCredits > 4) {
                alert(
                    "Warning: Credit limit exceeded. You would need to fill out an excess credit form. Consider rescheduling courses."
                );
                setAlertDisplayed(true);
            }
        }
    }, [totalCredits, upperCaseTitle, alertDisplayed]);




    return (
        <>
            <div className="session">
                {session_title !== "PAST COURSEWORK" && (
                    <div className="session-name">{session_title}</div>
                )}
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
                    )}
                </div>

                {/* Display total credits below the course list */}
                <div className="total-credits">
                    Total Credits: {totalCredits}
                </div>
            </div>

            {selectedCourse && (
                <CoursePopUp
                    courseId={Number(selectedCourse.id)}
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
            offered_winter: PropTypes.bool.isRequired,
            offered_summer: PropTypes.bool.isRequired,
            prerequisites: PropTypes.arrayOf(PropTypes.number).isRequired,
            corequisites: PropTypes.arrayOf(PropTypes.number).isRequired,
        })
    ).isRequired,
};

export default Session;