import { useState, useEffect } from "react"
import Header from "./Header.jsx"
import Footer from "./Footer.jsx"
import Schedule from "./Schedule.jsx"
import Session from "./Session.jsx"
import Instructions from "./Instructions.jsx"
import SearchMajor from "./SearchMajor.jsx"
import axios from "axios"


function App() {

  const [selectedMajor, setSelectedMajor] = useState(null);
  const [majorDetails, setMajorDetails] = useState(null);
  
  useEffect(() => {
    if (selectedMajor) {
      axios
        .get(`http://127.0.0.1:5000/api/major_details/${selectedMajor.value}`)
        .then(response => {
          setMajorDetails(response.data); // <-- Store it!
          console.log("Major data:", response.data);
          // You can update your scheduler or content based on the major's data here
        })
        .catch(error => console.error("Error fetching major details:", error));
    }
  }, [selectedMajor]);
  
  return (

    <>
      <Header />
      <Instructions/>
      <SearchMajor selectedMajor={selectedMajor} setSelectedMajor={setSelectedMajor} />
      
      <h2 className="title-of-scheduler"> Personal {selectedMajor?.label} 4 Year Plan</h2>
      <Schedule plan = {majorDetails?.plan}/>
      {/* <Schedule /> */}
      <footer></footer>
    </>
    
  );
}

export default App
