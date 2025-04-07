import Session from "./Session"
import axios from "axios"
import { useState, useEffect } from "react"

function Schedule({plan}){

    console.log("📦 Received plan:", plan);

    if (!plan) {
        return <p>Choose a major to see its schedule.</p>;
    }


    return (

        <>

            <div className="schedule">
                {Object.entries(plan).map(([year, sessions]) => (
                    <div className="schedule-year" key={year}>

                    {/* That's where we include the year title */}
                    {/* <h3>{year.replace("_", " ").toUpperCase()}</h3> */}

                    {["fall", "winter", "spring", "summer"].map((season) => (
                        <Session
                            semester={`${year}-${season}`}
                            session_title={season.toUpperCase()}
                            courses={sessions[season] || []}
                        />
                    ))}
                    </div>
                ))}
            </div>
        </>
    )
}

export default Schedule