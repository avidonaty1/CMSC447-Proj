import { useEffect, useState } from "react";
import axios from "axios";
import PropTypes from "prop-types";
// see index.css for styling

/**
 * CoursePopUp Component
 * This component renders an individual course as a draggable item.
 * It fetches courses from the API endpoint '/api/v2/courses/<int:course_id>'
 *  
 * Props:
 * - courseId: The numeric course id to fetch details for
 * - onClose: A callback function to close the popup
 * 
 * Return:
 * A modal overlay with:
 * - a close button in the top right
 * - An error message if there's an error fetching course details
 * - A loading indicator while the data is being fetched
 * - When loaded, displays course information 
 */

const CoursePopUp = ({ courseId, onClose }) => {
  // State to keep track of course details
  const [courseDetails, setCourseDetails] = useState(null);
  // State for error handling
  const [error, setError] = useState(null);

  console.log("Fetching course info for:", courseId);

  // Fetches the course info from the API endpoint
  // and populates the courseDetals state
  // .get(`/api/v2/courses/${courseId}`)
  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000/api/v2/courses/${courseId}`)
      .then((response) => {
        setCourseDetails(response.data);
      })
      .catch((error) => {
        setError("Error: Could not load course details.");
        console.error("Error fetching course:", error);
      });
  }, [courseId]);

  return (

    <div className="pop-up-window">
      <div className="pop-up-window-content">
        <button className="close-pop-up" onClick={onClose}> X </button>
        {error && <p className="error-message">{error}</p>}
        {/* If no error, display loading message */}
        {!courseDetails && !error && <p>Loading course details...</p>}
        {/* Once courseDetails are fetched, display them */}
        {courseDetails && (
          <>
            <h2>{courseDetails.number}</h2>
            <p><strong>Title:</strong> {courseDetails.title}</p>
            <p><strong>Credits:</strong> {courseDetails.credit_hours}</p>
            <p><strong>Description:</strong> {courseDetails.description}</p>
            <p><strong>Fills Up Quickly:</strong> {courseDetails.fills_up_quickly}</p>
            <p><strong>May be Offered in Winter:</strong>{" "}
            {courseDetails.offered_winter ? "Yes" : "No"}</p>
            <p><strong>May be Offered in Summer:</strong>{" "}
            {courseDetails.offered_summer ? "Yes" : "No"}</p>
            <p><strong>Prerequisites:</strong> {courseDetails.prerequisites.join(', ') || 'None'}</p>
            <p><strong>Corequisites:</strong> {courseDetails.corequisites.join(', ') || 'None'}</p>
            <p><strong>Advisor Notes:</strong> {courseDetails.advisor_notes}</p>
          </>
        )}
      </div>
    </div>
  );
};

CoursePopUp.propTypes = {
  courseId: PropTypes.number.isRequired,
  onClose: PropTypes.func.isRequired,
};

export default CoursePopUp;