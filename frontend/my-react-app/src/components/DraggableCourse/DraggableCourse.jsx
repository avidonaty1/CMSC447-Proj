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
 * - course (array, required): A tuple in the format [courseId, courseNumber]
 *   The courseId is used to build the draggable identifier.
 *   The courseNumber is displayed.
 * - semester (string, required): A string representing the session (i.e. "year1-Fall")
 *   used as part of the draggable id.  
 * - onClick (function, required): A callback function invoked when the course is clicked
 * 
 * Return:
 * A div element with drag properties representing the course
 */

const DraggableCourse = ({ course, semester, onClick }) => {
    // Course is expected to be a tuple: [courseId, courseNumber]
    // Create an id in the format: "year-session-courseId"
    const { attributes, listeners, setNodeRef, transform } = useDraggable({
        id: `${semester}-${course[0]}`, 
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
        {/* Display course number */}
        {course[1]}
      </div>
    );
  };
  // PropTypes for type safety
  DraggableCourse.propTypes = {
    course: PropTypes.array.isRequired,
    semester: PropTypes.string.isRequired,
    onClick: PropTypes.func.isRequired,
  };

  export default DraggableCourse;