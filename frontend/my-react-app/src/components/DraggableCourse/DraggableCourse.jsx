import React from "react";
import PropTypes from "prop-types";
import {  useDraggable } from '@dnd-kit/core';
import "./DraggableCourse.css";

/**
 * DraggableCourse Component
 * This component renders an individual course as a draggable item.
 * It uses the dnd-kit useDraggable hook to enable drag functionality.
 *  
 * Props:
 * - course (object, required): A course object with the id, number, credits, 
 *   prequisites and corequistes attributes.
 *   The course.id is used to build the draggable identifier.
 *   The course.number and course.credit_hours are displayed.
 * - semester (string, required): A string representing the session (i.e. "year1-Fall")
 *   used as part of the draggable id.  
 * - onClick (function, required): A callback function invoked when the course is clicked
 * 
 * Return:
 * A div element with drag properties representing the course
 */

const DraggableCourse = ({ course, semester, onClick }) => {
    
    // Create an id in the format: "year-session-courseId"
    const { attributes, listeners, setNodeRef, transform } = useDraggable({
        id: `${semester}-${course.id}`, 
      });
    
    // Apply transformation style when dragging
    const style = transform
      ? { transform: `translate(${transform.x}px, ${transform.y}px)` }
      : undefined;
  
    return (
      <div
        ref={setNodeRef}
        className="course"
        style={style}
        {...listeners}
        {...attributes}
        onClick={onClick}
      >
        {/* Display course number and credits*/}
        <div>{course.number} | Credits: {course.credit_hours}</div>
      </div>
    );
  };

  
  // PropTypes for type safety
  DraggableCourse.propTypes = {
    course: PropTypes.shape({
      id: PropTypes.number.isRequired,
      number: PropTypes.string.isRequired,
      credit_hours: PropTypes.number.isRequired,
      offered_winter: PropTypes.bool.isRequired,
      offered_summer: PropTypes.bool.isRequired,
      prerequisites: PropTypes.arrayOf(PropTypes.number).isRequired,
      corequisites: PropTypes.arrayOf(PropTypes.number).isRequired,
    }).isRequired, 
    semester: PropTypes.string.isRequired,
    onClick: PropTypes.func.isRequired,
  };

  export default DraggableCourse;