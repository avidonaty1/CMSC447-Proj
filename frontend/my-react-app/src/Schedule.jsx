
import { DndContext, closestCenter, PointerSensor, useSensor, useSensors} from '@dnd-kit/core';


import Session from "./Session"
import axios from "axios"
import { useState, useEffect } from "react"

function Schedule({plan}){

    const sensors = useSensors(
        useSensor(PointerSensor, {
          activationConstraint: {
            distance: 5,
          },
        })
    );
    
    const handleDragEnd = (event) => {
        const { active, over } = event;
        if (!over || active.id === over.id) return;
    
        const [sourceSemester, courseName] = active.id.split('|');
        const destinationSemester = over.id;
    
        const updatedPlan = { ...plan };
    
        const courseIndex = updatedPlan[sourceSemester].indexOf(courseName);
        if (courseIndex > -1) {
        updatedPlan[sourceSemester].splice(courseIndex, 1);
        }
    
        updatedPlan[destinationSemester].push(courseName);
    
        onPlanChange(updatedPlan);
    };
      




    console.log("📦 Received plan:", plan);

    if (!plan) {
        return <p>Choose a major to see its schedule.</p>;
    }


    return (

        <DndContext sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd}>
            {/* sensors={sensors} collisionDetection={closestCenter} onDragEnd={handleDragEnd} */}


            <div className="schedule">
                {Object.entries(plan).map(([year, sessions]) => (
                    <div className="schedule-year" key={year}>

                    {["fall", "winter", "spring", "summer"].map((season) => (
                        <Session
                            semester={`${year}-${season}`}
                            session_title={season.toUpperCase()}
                            courses={sessions[season] || []}
                        />
                    ))}
                    </div>
                ))}

                {/* {Object.entries(plan).map(([semesterKey, courses]) => (
                    <Session
                        key={semesterKey}
                        semester={semesterKey}
                        session_title={semesterKey.split('-')[1]?.toUpperCase()}
                        courses={courses}
                    />
                ))} */}
            </div>
        </DndContext>
    )
}

export default Schedule