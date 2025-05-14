import React from "react"; // This is needed for tests
import { useState, useEffect } from "react";
import axios from "axios";
import PropTypes from "prop-types";
import './SearchMajor.css'

/**
 * SearchMajor Component
 * 
 * This component allows users to search and select a major to add to the plan
 * It fetches data from the `/api/v2/majors` endpoint and displays the list in a dropdown menu
 * 
 * Props:
 * - onMajorSelect: A callback function to handle the selected major
 *  (Receives the selected major object as an argument)
 */

const SearchMajor = ({ onMajorSelect }) => {
  // State to manage the list of majors
  const [majors, setMajors] = useState([]);

  // State for error handling
  const [error, setError] = useState(null);

  // State for loading indicator
  const [loading, setLoading] = useState(true);

  /**
   * Fetch the list of majors from the API on component mount
   */
  useEffect(() => {
    const fetchMajors = async () => {
      try {
        // Fetch data from Flask API and then update state with fetched data
        // const response = await axios.get("http://127.0.0.1:5000/api/v2/majors");
        const response = await axios.get("/api/v2/majors");

        setMajors(response.data.majors);
        console.log("Majors fetched:", response.data);
        setLoading(false);
      } catch (err) {
        console.error("Error fetching majors:", err);
        setError(`Failed to load majors. Error: ${err.message}`);
        setLoading(false);
      }
    };
    fetchMajors();
  }, []);


  /**
   * Handle dropdown selection and trigger the onMajorSelect callback
   * @param {Event} event - The change from the dropdown menu
   */
  const handleChange = (event) => {
    // Extract the selected major ID from the dropdown
    const selectedMajorId = event.target.value;

    // If the user selects the default option, 
    // reset the current major by calling the callback with null
    if (!selectedMajorId) {
      onMajorSelect(null);
      return;
    }
    // otherwise, search for the selected major within the majors array
    const selectedMajor = majors.find(
      (major) => major._id === parseInt(selectedMajorId, 10)
    );
    if (selectedMajor) {
      onMajorSelect(selectedMajor);
    }
  };

  // Conditional rendering for loading and error states
  if (loading) {
    return <p>Loading majors...</p>;
  }

  if (error) {
    return <p className="error-message">{error}</p>;
  }

  return (
    <div className="select-major">
      <label className="select-major-text" htmlFor="major-dropdown">Select a major:</label>
      {/* Dropdown menu to allow the user to select a major" */}
      <select id="major-dropdown" onChange={handleChange} aria-labelledby="major-dropdown">
        <option value="">--Choose a Major--</option>

        {/* Dynamically render options based on the majors array */}
        {majors.map((major) => (
          <option key={major._id} value={major._id}>
            {major.name}
          </option>
        ))}
      </select>
    </div>
  );
};

export default SearchMajor;

/**
 * PropTypes for SearchMajor Component (enforces type safety) 
 */
SearchMajor.propTypes = {
  onMajorSelect: PropTypes.func.isRequired,
};

