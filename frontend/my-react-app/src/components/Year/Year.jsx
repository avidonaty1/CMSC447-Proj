import React from "react";
import PropTypes from "prop-types";
import Session from "../Session/Session.jsx";
import "./Year.css";
/**
 * Year Component
 * This component represents a single academic year in the schedule
 * It receives the year key (i.e. year1) and an object of sessions, where 
 * each key is a session name (i.e. "Fall") and the value is an array of 
 * course tuples [[courseId, courseNumber], ...]
 * 
 * Props:
 * - yearKey (string, required): The identifier of the year (i.e. year1)
 * - sessions (object, required): An object mapping session names to arrays
 *   of course tuples
 * 
 * Return:
 * A container that renders a header for the year 
 * and a list of Session components
 */
const Year = ({ yearKey, sessions }) => {
  // want yearKey to display as YEAR 1
  const displayYear = `${yearKey.slice(0,4)} ${yearKey.slice(4)}`.toUpperCase();

    return (
        <div className="schedule-year">
        <h3>{displayYear}</h3>
        <div className="schedule-sessions">
          {Object.entries(sessions).map(([sessionKey, courses]) => (
            <Session
              key={sessionKey}
              semester={`${yearKey}-${sessionKey}`}
              session_title={sessionKey.toUpperCase()}
              courses={courses}
            />
          ))}
        </div>
      </div>
    );
};

// PropTypes for type safety
Year.propTypes = {
    yearKey: PropTypes.string.isRequired,
    sessions: PropTypes.object.isRequired,
};

export default Year;