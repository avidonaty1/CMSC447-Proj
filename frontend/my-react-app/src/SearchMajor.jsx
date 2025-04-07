import { useState, useEffect } from "react";
import Select from "react-select";
import axios from "axios";

function SearchMajor({selectedMajor, setSelectedMajor}) {
  const [majors, setMajors] = useState([]);
//   const [selectedMajor, setSelectedMajor] = useState(null); // Use this internally

  useEffect(() => {
    axios
      .get('http://127.0.0.1:5000/api/majors')
      .then((response) => {
        const majorOptions = response.data.map(major => ({
          value: major._id,
          label: major.name,
        }));
        setMajors(majorOptions);
      })
      .catch((error) => {
        console.error("There was an error fetching the majors:", error);
      });
  }, []);

  const handleChange = (selectedOption) => {
    setSelectedMajor(selectedOption); // No more props involved
  };

  return (
    <div className="selectMajor">
      <label className="select-major-text" htmlFor="major">
        Select a major:
      </label>

      <Select
        classNamePrefix="select-box"
        options={majors}
        value={selectedMajor}
        isSearchable
        onChange={handleChange}
        placeholder="Choose a major"
      />
    </div>
  );
}

export default SearchMajor;
