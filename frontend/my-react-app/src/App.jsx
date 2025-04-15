import { useState, useEffect } from "react";
import axios from "axios";

// Components
import Header from "./Header.jsx";
import Footer from "./Footer.jsx";
import Schedule from "./components/Schedule/Schedule.jsx";
import Instructions from "./Instructions.jsx";
import SearchMajor from "./components/SearchMajor/SearchMajor.jsx";
import Login from "./components/LoginPage/Login.jsx";

function App() {
  // State to store the studentId (or 0 if Guest)
  const [studentId, setStudentId] = useState(null);

  // State to store the selected major from dropdown
  const [selectedMajor, setSelectedMajor] = useState(null);

  // State to store fetched major details
  const [majorPlan, setMajorPlan] = useState(null);

  // State to handle errors
  const [error, setError] = useState(null);

  // Handle login (guest or as student with an account / email registered)
  const handleLogin = (id) => {
    setStudentId(id);
    setSelectedMajor(null);
    setMajorPlan(null);
  }

  // Fetch the student's major after login
  useEffect(() => {
    const fetchStudentMajor = async () => {
      try {
        // Skip if logged in as Guest
        if (studentId === 0 || studentId === null) return;

        // Fetch student's major from API
        const response = await axios.get(`/api/v2/students/${studentId}/major`);
        setSelectedMajor(response.data.major_id);
        setError(null);
        console.log("Fetched student's major:", response.data.major_id);
      } catch (error) {
        console.error("Error fetching student's major", error);
        setError("Failed to fetch student's major.");
      }
    };
    fetchStudentMajor();
  }, [studentId]);


  // Fetch student's custom plan after login
  useEffect(() => {
    const fetchStudentPlan = async () => {
      try {
        // Skip if logged in as Guest
        if (studentId === 0 || studentId === null) return;
        // Fetch student's major from API
        const response = await axios.get(`/api/v2/students/${studentId}/plan`);
        setMajorPlan(response.data.custom_plan);
        setError(null);
        console.log("Fetched student's plan:", response.data.custom_plan);
      } catch (error) {
        console.error("Error fetching student's plan", error);
        setError("Failed to fetch student's plan.");
      }
    };
    fetchStudentPlan();
  }, [studentId]);


  // When major is selected from dropdown, set the state
  const handleMajorSelect = async (major) => {
    if (!major) {
      setSelectedMajor(null);
      setMajorPlan(null);
      console.log("Major reset. Blank out plan.");

      if (studentId > 0) {
        const emptyNestedPlan = {
          year1: {Fall: [], Winter: [], Spring: [], Summer: []},
          year2: {Fall: [], Winter: [], Spring: [], Summer: []},
          year3: {Fall: [], Winter: [], Spring: [], Summer: []},
          year4: {Fall: [], Winter: [], Spring: [], Summer: []},
        };

        try {
          const response = await axios.post(`/api/v2/students/${studentId}/plan`, { custom_plan: emptyNestedPlan});
          console.log("Student's plan reset to empty nested plan:", response.data)
        } catch (error){
          console.error("Error resetting student's plan:", error);
          setError("Failed to reset student's plan");
        }
      }
      return;
    }

    console.log("Selected Major:", major);
    // Update the local state whether it is student or guest
    setSelectedMajor(major._id);
    
    if (studentId > 0) {
      // Update backend if user is a student
      try {
        const response = await axios.post(`/api/v2/students/${studentId}/major`, { major_id: major._id });
        setSelectedMajor(major._id);
        console.log("Student's major updated successfully:", response.data);
      } catch (error) {
        console.error("Error updating student's major:", error);
        setError("Failed to update student's major.");
      }
    }

  };


  // Update plan on backend for students, or locally for guests, while merging
  const handlePlanChange = async (newPlan) => {
    console.log("Updating plan:", newPlan);

    // Always update the local state with merging
    setMajorPlan((prev) => ({ ...prev, default_plan: newPlan }));

    // Update backend if user is a student
    if (studentId > 0) {
      try {
        const response = await axios.post(`/api/v2/students/${studentId}/plan`, { custom_plan: newPlan });

        console.log("Student's plan updated successfully:", response.data);
      } catch (error) {
        console.error("Error updating student's plan:", error);
        setError("Failed to update student's plan.");
      }
    }
  };

  // Fetch the default plan if a new major is selected
  useEffect(() => {
    const fetchMajorPlan = async () => {
      try {
        // if no major is selected, exit early
        if (!selectedMajor) return;

        const majorId = typeof selectedMajor === "object" ? selectedMajor._id : selectedMajor;

        // Fetch data from API endpoint
        console.log("Fetching plan for major:", selectedMajor);

        const response = await axios.get(`/api/v2/majors/${majorId}/plan`);
        setMajorPlan(response.data);
        setError(null);
        console.log("Fetched default plan");
      } catch (error) {
        console.error("Error fetching default plan for major", error);
        setError("Failed to fetch default plan for major. Please try again later.")
      }
    };

    fetchMajorPlan();
  }, [selectedMajor]);


  return (
    <>
      <div className="app-container">
        {/* Show Login if no studentId is set */}
        {studentId === null ? (
          <Login onLogin={handleLogin} />
        ) : (
          <>
            <Header />
            <Instructions />

            <SearchMajor onMajorSelect={handleMajorSelect} />

            {/* Error Message */}
            {error && <p className="error-message">{error}</p>}

            {/* Render Schedule with drag-and-drop context */}
            {selectedMajor && majorPlan && (
              <>
                <h2 className="title-of-scheduler"> Personal {selectedMajor.name} 4 Year Plan</h2>
                <Schedule
                  // fallback in case defaultPlan is missing or malformed
                  plan={majorPlan?.default_plan || {}}
                  onPlanChange={handlePlanChange}
                />
              </>
            )}
            <Footer />
          </>
        )}
      </div>
    </>
  );
}

export default App;
