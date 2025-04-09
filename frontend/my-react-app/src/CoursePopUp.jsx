import { useEffect, useState } from 'react';
import axios from 'axios';


function CoursePopUp({courseName, onClose }){

    const [courseDetails, setCourseDetails] = useState(null);
    const [error, setError] = useState(null);


    useEffect(() => {
        axios
          .get(`http://127.0.0.1:5000/api/course/${encodeURIComponent(courseName)}`)
          .then((response) => {
            setCourseDetails(response.data);
          })
          .catch((error) => {
            setError("Could not load course details");
            console.error("Error fetching course:", error);
          });
      }, [courseName]);

    return(

        <div className="pop-up-window">
            <div className="pop-up-window-content">
                <button className="close-pop-up" onClick={onClose}> X </button>

                {/* <h2>{courseDetails.name}</h2>
                <p><strong>Credits:</strong> {courseDetails.number_of_credits}</p>
                <p><strong>Description:</strong> {courseDetails.description}</p>
                <p><strong>Prerequisites:</strong> {courseDetails.prerequisites.join(', ') || 'None'}</p> */}


                {error && <p className="error-message">{error}</p>}
                {!courseDetails && !error && <p>Loading...</p>}

                {courseDetails && (
                    <>
                    <h2>{courseDetails.name}</h2>
                    <p><strong>Credits:</strong> {courseDetails.number_of_credits}</p>
                    <p><strong>Description:</strong> {courseDetails.description}</p>
                    <p><strong>Prerequisites:</strong> {courseDetails.prerequisites.join(', ') || 'None'}</p>
                    </>
                )}

            </div>
        </div>

        

    );

}

export default CoursePopUp;