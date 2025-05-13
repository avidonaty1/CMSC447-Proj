import { useState, useEffect } from "react";
import { Routes, Route, Navigate, useNavigate } from "react-router-dom";
import axios from "axios";
import { cloneDeep } from "lodash";
// Components
import Header from "./Header.jsx";
import Footer from "./Footer.jsx";
import Schedule from "./components/Schedule/Schedule.jsx";
import Instructions from "./Instructions.jsx";
import SearchMajor from "./components/SearchMajor/SearchMajor.jsx";
import Login from "./components/LoginPage/Login.jsx";
// import Print from "./Print.jsx"; // Ensure this import is correct
// import pawImage from "./assets/umbc-official-paw-variations.eps.jpg";
// import Paws from "./Paws.jsx";


function App() {
  // State to store the studentId (or 0 if Guest)
  const [studentId, setStudentId] = useState(() => {
    const saved = localStorage.getItem("studentId");
    return saved !== null ? parseInt(saved, 10) : null;
  });
  

  // State to store the selected major from dropdown
  const [selectedMajor, setSelectedMajor] = useState(null);

  // State to store fetched major details
  const [majorPlan, setMajorPlan] = useState(null);

  // State to handle errors
  const [error, setError] = useState(null);

  // Handle login (guest or as student with an account / email registered)
  const navigate = useNavigate();

  const handleLogin = (id) => {
    setStudentId(id);
    localStorage.setItem("studentId", id);
    setSelectedMajor(null);
    setMajorPlan(null);
    navigate("/app");
  };

  // handle student logout
  const handleLogout = () => {
    setStudentId(null);
    localStorage.removeItem("studentId");
    setSelectedMajor(null);
    setMajorPlan(null);
    navigate("/login");
  };
  


  // Fetch the student's major after login
  useEffect(() => {
    const fetchStudentPlan = async () => {
      try {
        if (studentId === 0 || studentId === null || !selectedMajor) return;
  
        const response = await axios.get(`http://127.0.0.1:5000/api/v2/students/${studentId}/plan`);
        setMajorPlan(response.data.custom_plan);
        setError(null);
        console.log("Fetched student's plan:", response.data.custom_plan);
      } catch (error) {
        console.error("Error fetching student's plan", error);
        setError("Failed to fetch student's plan.");
      }
    };
  
    fetchStudentPlan();
  }, [studentId, selectedMajor]); // 👈 wait until major is loaded too
  


  // Fetch student's custom plan after login
  useEffect(() => {
    const fetchStudentPlan = async () => {
      try {
        // Skip if logged in as Guest
        if (studentId === 0 || studentId === null) return;
        // Fetch student's major from API
        const response = await axios.get(`http://127.0.0.1:5000/api/v2/students/${studentId}/plan`);
        // const response = await axios.get(`api/v2/students/${studentId}/plan`);
        setMajorPlan(cloneDeep(response.data.custom_plan));
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
          year0: { PastCoursework: []},
          year1: { Fall: [], Winter: [], Spring: [], Summer: [] },
          year2: { Fall: [], Winter: [], Spring: [], Summer: [] },
          year3: { Fall: [], Winter: [], Spring: [], Summer: [] },
          year4: { Fall: [], Winter: [], Spring: [], Summer: [] },
        };

        try {
          const response = await axios.post(`http://127.0.0.1:5000/api/v2/students/${studentId}/plan`, { custom_plan: emptyNestedPlan});
          // const response = await axios.post(`/api/v2/students/${studentId}/plan`, {
          //   custom_plan: cloneDeep(emptyNestedPlan),
          // });

          console.log("Student's plan reset to empty nested plan:", response.data)
        } catch (error) {
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
        const response = await axios.post(`http://127.0.0.1:5000/api/v2/students/${studentId}/major`, { major_id: major._id });
        // const response = await axios.post(`/api/v2/students/${studentId}/major`, { major_id: major._id });

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

    // Deep clone to protect against mutation
    const clonedNewPlan = cloneDeep(newPlan);

    // Always update the local state with merging and deep cloning
    setMajorPlan((prev) => ({
      ...cloneDeep(prev), 
      default_plan: clonedNewPlan,
    }));

    // Update backend if user is a student
    if (studentId > 0) {
      try {
        const response = await axios.post(`http://127.0.0.1:5000/api/v2/students/${studentId}/plan`, { 
          custom_plan: clonedNewPlan 
        });
        // const response = await axios.post(`/api/v2/students/${studentId}/plan`, {
        //   custom_plan: clonedNewPlan,
        // });

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

        const response = await axios.get(`http://127.0.0.1:5000/api/v2/majors/${majorId}/plan`);
        // const response = await axios.get(`/api/v2/majors/${majorId}/plan`);
        setMajorPlan(cloneDeep(response.data));
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

      <Routes>
        <Route
          path="/login"
          element={<Login onLogin={handleLogin} />}
        />

        <Route
          path="/app"
          element={
            studentId !== null ? (
              <div className="app-container">
                <Header />
                <button onClick={handleLogout}>Logout</button>
                <Instructions />
                <SearchMajor onMajorSelect={handleMajorSelect} />
                {error && <p className="error-message">{error}</p>}
                {selectedMajor && majorPlan && (
                  <Schedule
                    plan={majorPlan?.default_plan || {}}
                    onPlanChange={handlePlanChange}
                  />
                )}
                <Footer />
              </div>
            ) : (
              <Navigate to="/login" />
            )
          }
        />

        {/* Fallback route */}
        <Route path="*" element={<Navigate to={studentId ? "/app" : "/login"} />} />
      </Routes>


    </>
  );
}

export default App;
