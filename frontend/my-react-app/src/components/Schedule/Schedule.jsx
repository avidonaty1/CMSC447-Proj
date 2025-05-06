import React, { useMemo } from "react";
import PropTypes from "prop-types";
import { DndContext, closestCenter, PointerSensor, useSensor, useSensors } from "@dnd-kit/core";
import { cloneDeep } from "lodash";
import Year from "../Year/Year.jsx";
import "./Schedule.css";
import {
  getCoursesUpTo,
  validateCourseDrop,
  checkDependencyViolation
} from "./courseSequenceChecking.js";
import { use } from "react";

/**
 * Schdedule Component
 * 
 * This component renders a schedule view for a graduation plan.
 * Drag and drop courses to move them between sessions.
 * When a drop is attempted, the component validates that the course's 
 * prerequisites and corequisites are met:
 * - Prerequisites must be in sessions that come before the target session
 * - Corequisites must be in the target session or a previous session
 * 
 * Props:
 * - plan (object, required): A nested object containing the plan
 *   for a major. There are keys for each year, and each year contains
 *   keys for a session. Each session contains an array of course dictionaries
 *   {"id": int,
+     "number": string,
+     "credit_hours": int,
      "offered_winter": bool,
      "offered_summer": bool,
+     "prerequisites": [],
+     "corequisites": []
+    } 
 * - onPlanChange(function, required): A callback function that is called
 *   with the updated Plan object whenever a course is moved.
 *   
 * Return:
 * The component return a DnDContext that wraps the schedule layout.
 * If the plan is not provided or empty, a message is displayed
 * prompting the user to choose a major.
 */

const Schedule = ({ plan, onPlanChange }) => {
  // Configure sensors for drag and drop functionality
  const sensors = useSensors(
    useSensor(PointerSensor, {
      activationConstraint: {
        // Start dragging after 5 px movement
        distance: 5,
      },
    })
  );

  // Memoize the plan to ensure immutability
  const memoizedPlan = useMemo(() => cloneDeep(plan), [plan]);

  // Memoize Year components
  const memoizedYears = useMemo(() => {
    return Object.entries(memoizedPlan).map(([yearKey, sessions]) => (
      <Year key={yearKey} yearKey={yearKey} sessions={cloneDeep(sessions)} />
    ));
  }, [memoizedPlan]);

  // Handle drag-and-drop event for DraggableCourse
  // must be async to use in context of prerequisite validation
  const handleDragEnd = async (event) => {
    const { active, over } = event;

    // console.log("🎯 Drag Event Triggered");
    // console.log("Active (dragged):", active.id);
    // console.log("Over (dropped onto):", over?.id);

    console.log("Dropped on:", over?.id); // should log like "year1-FALL"


    // Ensure target is valid and not the same as the source
    if (!over || active.id === over.id) {
      console.error("❌ Invalid drop or dropped onto self");
      return;
    }

    // Draggable course id have this format:
    // "yearKey-sessionKey-courseId"
    const activeParts = active.id.split("-");
    if (activeParts.length < 3) {
      console.error("❌ Active id does not have format: year-session-course");
      return;
    }

    const [fromYear, fromSession, courseId] = activeParts;

    // Drop target should be in format: "yearKey-sessionKey"
    // So that it drops into a session
    const toParts = over.id.split("-");
    if (toParts.length < 2) {
      console.error("❌ Over id does not have format: year-session");
      return;
    }

    const [toYear, toSession] = toParts;

    console.log(`📦 Moving "${active.id}" from ${fromYear}-${fromSession} ➡️ ${toYear}-${toSession}`);
    // Update the plan by moving the course to the new position
    // Deep clone the current plan to prevent mutation of the original object
    const updatedPlan = cloneDeep(memoizedPlan);

    // Verify that source and target sessions exist in the plan
    if (!updatedPlan[fromYear] || !updatedPlan[fromYear][fromSession]) {
      console.error("❌ Source session not found in plan");
      return;
    }
    if (!updatedPlan[toYear] || !updatedPlan[toYear][toSession]) {
      console.error("❌ Target session not found in plan");
      return;
    }

    // Find index of dragged course  in the source session
    const sourceCourses = updatedPlan[fromYear][fromSession];
    const sourceIndex = sourceCourses.findIndex(
      (course) => String(course.id) === courseId
    );
    if (sourceIndex === -1) {
      console.error("❌ Course not found in source session");
      return;
    }

    // Deep clone the moved course 
    const movedCourse = cloneDeep(sourceCourses[sourceIndex]);
    sourceCourses.splice(sourceIndex, 1);

    // Before updating the plan, check that prerequisites and corequisites are present
    // Deep clone possible dependent courses
    const previousSessionCourses = cloneDeep(getCoursesUpTo(memoizedPlan, toYear, toSession, false));
    const currAndPrevSessionCourses = cloneDeep(getCoursesUpTo(memoizedPlan, toYear, toSession, true));
    const targetSession = toSession.toUpperCase();

    const validDrop = await validateCourseDrop(
      movedCourse,
      previousSessionCourses,
      currAndPrevSessionCourses,
      targetSession,
      updatedPlan);

    if (!validDrop) {
      if (targetSession === "SUMMER" && !movedCourse.offered_summer) {
        alert("Course not offered in summer. Please reschedule");
      } else if (targetSession === "WINTER" && !movedCourse.offered_winter) {
        alert("Course not offered in winter. Please reschedule");
      } else {
        alert("Moving this course would violate one or more prerequisites or corequisites.")
      }
      return;
    }
    const dependencyViolated = await checkDependencyViolation(updatedPlan, toYear, toSession, movedCourse);
    if (dependencyViolated) {
      alert("Moving this course would violate one or more prerequisites or corequisites.")
      return;
    }

    // Append course to target session if both checks pass
    updatedPlan[toYear][toSession].push(cloneDeep(movedCourse));
    // Update plan state with new arrangement
    onPlanChange(cloneDeep(updatedPlan));
  };

  // If plan is null or empty, display a prompt to choose a major
  if (!plan || Object.keys(plan).length === 0) {
    return <p>Choose a major to see its schedule.</p>;
  }



  console.log("📦 Received plan:", plan);

  // handleAddYear
  // add an extra year to the plan
  const handleAddYear = () => {
    // Clone the existing plan
    const updatedPlan = JSON.parse(JSON.stringify(plan));
  
    // Determine the next year key: find the highest "yearX"
    const currentYears = Object.keys(updatedPlan);
    const yearNumbers = currentYears
      .map((key) => parseInt(key.replace("year", ""), 10))
      .filter((num) => !isNaN(num));
    const maxYear = Math.max(...yearNumbers);
    const nextYear = `year${maxYear + 1}`;
  
    // Define an empty structure for the new year
    updatedPlan[nextYear] = {
      Fall: [],
      Winter: [],
      Spring: [],
      Summer: []
    };
  
    // Update state (and backend if student)
    onPlanChange(updatedPlan);
  };
  

  return (

    <DndContext sensors={sensors}
      collisionDetection={closestCenter}
      onDragEnd={handleDragEnd}>
      <div className="schedule">
        {memoizedYears}

        <div className="add-year-container">
        <button onClick={handleAddYear} className="add-year-button">
          + Add year
        </button>

        </div>
      </div>
    </DndContext>
  );
};

// PropTypes for type safety
Schedule.propTypes = {
  plan: PropTypes.object.isRequired,
  onPlanChange: PropTypes.func.isRequired,
};

export default Schedule;