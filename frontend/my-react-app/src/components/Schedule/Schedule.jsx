import React from "react";
import PropTypes from "prop-types";
import { DndContext, closestCenter, PointerSensor, useSensor, useSensors } from "@dnd-kit/core";
import { cloneDeep } from "lodash";
import Year from "../Year/Year.jsx";
import "./Schedule.css";
import {
  getCourseIdsUpTo,
  validateCourseDrop,
  checkDependencyViolation,
  invalidateCacheForCourse
} from "./courseSequenceChecking.js";

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
 *   keys for a session. Each session contains an array of course tuples
 *   [courseId, courseNumber]. 
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

   
  // Handle drag-and-drop event for DraggableCourse
  // must be async to use in context of prerequisite validation
  const handleDragEnd = async (event) => {
    const { active, over } = event;

    console.log("🎯 Drag Event Triggered");
    console.log("Active (dragged):", active.id);
    console.log("Over (dropped onto):", over?.id);

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
    // Normalize courseId to ensure it's an integer
    const normalizedCourseId = Number(courseId);
    if (isNaN(normalizedCourseId)) {
      console.error("❌ Invalid course ID (not a number:", courseId);
      return;
    }
    console.log("Normalized course ID:", normalizedCourseId, typeof normalizedCourseId);
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
    // Deep clone the current plan so we can modify it
    const updatedPlan = cloneDeep(plan);
    invalidateCacheForCourse(normalizedCourseId);

    // Verify that source and target sessions exist in the plan
    if (!updatedPlan[fromYear] || !updatedPlan[fromYear][fromSession]) {
      console.error("❌ Source session not found in plan");
      return;
    }
    if (!updatedPlan[toYear] || !updatedPlan[toYear][toSession]) {
      console.error("❌ Target session not found in plan");
      return;
    }

    // Find index of dragged course (course tuple) in the source session
    const sourceCourses = updatedPlan[fromYear][fromSession];
    console.log("Source courses before update:", sourceCourses);
    const sourceIndex = sourceCourses.findIndex(
      (course) => Number(course[0]) === normalizedCourseId
    );
    console.log("Source courses after update:", sourceCourses);
    if (sourceIndex === -1) {
      console.error("❌ Course not found in source session");
      return;
    }

    // Remove course from its source session
    const [movedCourse] = sourceCourses.splice(sourceIndex, 1);
    movedCourse[0] = Number(movedCourse[0]);
    console.log("Normalized Move Course ID", movedCourse[0], typeof movedCourse[0]);

    // Before updating the plan, check that prerequisites and corequisites are present
    const previousSessionIds = getCourseIdsUpTo(updatedPlan, toYear, toSession, false);
    console.log("Previous Sessions IDs:", previousSessionIds);
    const currAndPrevSessionIds = getCourseIdsUpTo(updatedPlan, toYear, toSession, true);
    console.log("Current and previous session IDS:", currAndPrevSessionIds);

    console.log("Validating course drop for ", normalizedCourseId);
    const validDrop = await validateCourseDrop(normalizedCourseId, previousSessionIds, currAndPrevSessionIds);
    if (!validDrop) {
      alert("Moving this course would violate one or more prerequisites or corequisites.")
      console.log("validate course drop failed");
      return;
    }
    console.log("Checking dependencies");
    const dependencyViolated = await checkDependencyViolation(updatedPlan, toYear, toSession, normalizedCourseId);
    if (dependencyViolated) {
      alert("Moving this course would violate one or more prerequisites or corequisites.")
      console.log("check dependency violation failed");
      return;
    }
    
    // Append course to target session if both checks pass
    updatedPlan[toYear][toSession].push(movedCourse);
    // Update plan state with new arrangement
    onPlanChange(updatedPlan);
  };

  // If plan is null or empty, display a prompt to choose a major
  if (!plan || Object.keys(plan).length === 0) {
    return <p>Choose a major to see its schedule.</p>;
  }

  console.log("📦 Received plan:", plan);

  return (

    <DndContext sensors={sensors}
      collisionDetection={closestCenter}
      onDragEnd={handleDragEnd}>
      <div className="schedule">
        {/*
        Iterate over each year in the plan.
        Object.entries(plan) returns an array of [yearKey, sessions] pairs.
        For each year, render a Year component:
        - the key prop is set to yearKey for React's internal use
        - yearKey and sessions are passed a props*/}
        {Object.entries(plan).map(([yearKey, sessions]) => (
          <Year key={yearKey} yearKey={yearKey} sessions={sessions} />
        ))}
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