
import { DndContext, closestCenter, PointerSensor, useSensor, useSensors} from '@dnd-kit/core';


import Session from "./Session"
import axios from "axios"
import { useState, useEffect } from "react"

function Schedule({ plan, onPlanChange }){

    const sensors = useSensors(
        useSensor(PointerSensor, {
          activationConstraint: {
            distance: 5,
          },
        })
    );
    
    const handleDragEnd = (event) => {
        const { active, over } = event;
      
        console.log("🎯 Drag Event Triggered");
        console.log("Active (dragged):", active.id);
        console.log("Over (dropped onto):", over?.id);
      
        if (!over || active.id === over.id) {
          console.log("❌ Invalid drop or dropped onto self");
          return;
        }
      
        const [fromSemester, courseName] = active.id.split("::");
        const toSemester = over.id;
        const [fromYear, fromSeason] = fromSemester.split("-");
        const [toYear, toSeason] = toSemester.split("-");
      
        console.log(`📦 Moving "${courseName}" from ${fromYear}-${fromSeason} ➡️ ${toYear}-${toSeason}`);
      
        // 🛠 Deep clone the entire plan to avoid mutation
        const updatedPlan = JSON.parse(JSON.stringify(plan));
      
        if (
          !updatedPlan[fromYear] ||
          !updatedPlan[fromYear][fromSeason] ||
          !updatedPlan[toYear] ||
          !updatedPlan[toYear][toSeason]
        ) {
          console.warn("⚠️ Structure mismatch or missing semesters.");
          return;
        }
      
        const fromCourses = updatedPlan[fromYear][fromSeason];
        const toCourses = updatedPlan[toYear][toSeason];
      
        console.log("Before move:");
        console.log("📍 From courses:", fromCourses);
        console.log("📍 To courses:", toCourses);
      
        const courseIndex = fromCourses.indexOf(courseName);
        if (courseIndex === -1) {
          console.warn("⚠️ Course not found in original semester.");
          return;
        }
        fromCourses.splice(courseIndex, 1);
      
        if (!toCourses.includes(courseName)) {
          toCourses.push(courseName);
        }
      
        console.log("After move:");
        console.log("✅ From courses:", fromCourses);
        console.log("✅ To courses:", toCourses);
      
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
                            key={`${year}-${season}-${sessions[season]?.join(',')}`}
                            semester={`${year}-${season}`}
                            session_title={season.toUpperCase()}
                            courses={sessions[season] || []}
                        />
                    ))}
                    </div>
                ))}
                {/* 
                {Object.entries(plan).map(([semesterKey, courses]) => (
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