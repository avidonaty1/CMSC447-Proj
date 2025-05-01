import React, { useMemo } from "react";
import PropTypes from "prop-types";
import { cloneDeep } from "lodash";
import Session from "../Session/Session.jsx";
import "./Year.css";
/**
 * Year Component
 * This component represents a single academic year in the schedule
 * It receives the year key (i.e. year1) and an object of sessions, where 
 * each key is a session name (i.e. "Fall") and the value is an array of 
 * course objects
 * 
 * Props:
 * - yearKey (string, required): The identifier of the year (i.e. year1)
 * - sessions (object, required): An object mapping session names to arrays
 *   of course objects
 * 
 * Return:
 * A container that renders a header for the year 
 * and a list of Session components
 */
const Year = ({ yearKey, sessions }) => {
  // want yearKey to display as YEAR 1 for standard years and 
  // differently for year 0
  const displayYear =
    yearKey === "year0" ? "PAST COURSEWORK" : `${yearKey.slice(0, 4)} ${yearKey.slice(4)}`.toUpperCase();

  // Create a deep clone to ensure immutability
  const memoizedSessions = useMemo(() => cloneDeep(sessions), [sessions]);
  return (
    <div className={`schedule-year ${yearKey === "year0" ? "past-coursework-year" : ""} `}>
      <h3 className="schedule-year-title">{displayYear}</h3>
      <div className={`schedule-sessions ${yearKey === "year0" ? "past-coursework-sessions" : ""}`}>
        {yearKey === "year0" ? (
          <Session
            semester={`${yearKey}-PastCoursework`}
            session_title="PAST COURSEWORK"
            courses={cloneDeep(Object.values(memoizedSessions).flat())}
          />
        ) : (
          Object.entries(memoizedSessions).map(([sessionKey, courses]) => (
            <Session
              key={sessionKey}
              semester={`${yearKey}-${sessionKey}`}
              session_title={sessionKey.toUpperCase()}
              courses={cloneDeep(courses)}
            />
          ))
        )}
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