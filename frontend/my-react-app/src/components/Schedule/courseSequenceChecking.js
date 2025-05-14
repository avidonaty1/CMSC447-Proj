import { cloneDeep } from "lodash";

/**
 * These helper functions are used for course requirement checking
 * in the Schedule component so that dragged/dropped courses
 * do not violate the course sequence of prerequisites and corequisites.
 * 
 * Course A is a prerequisite for Course B. Course C is a corequisite for Course B. 
 * Course A cannot be placed after course B. 
 * Course B cannot be placed before or level with Course A. 
 * Course C cannot be placed after Course B. 
 * Course B cannot be placed before Course C. 
 * 
 * NOTE: Manual testing shows good for these versions 
 */

// Return an ordered array of session keys from the plan
const getOrderedSessions = (plan) => {
  const clonedPlan = cloneDeep(plan);
  const orderedSessions = [];
  // sort year keys to guarantee ascending order
  const yearKeys = Object.keys(clonedPlan).sort();
  const sessionOrder = ["PastCoursework", "Fall", "Winter", "Spring", "Summer"];
  yearKeys.forEach(year => {
    sessionOrder.forEach(session => {
      if (clonedPlan[year]?.[session]) {
        orderedSessions.push({ year, session });
      }
    });
  });
  return orderedSessions;
};


// Get all courses from sessions that come before (or up to) a target session
// If includeTarget is false, only sessions strictly before
const getCoursesUpTo = (plan, targetYear, targetSession, includeTarget = false) => {
  const clonedPlan = cloneDeep(plan);
  const orderedSessions = getOrderedSessions(clonedPlan);
  const targetIndex = orderedSessions.findIndex(
    s => s.year === targetYear && s.session === targetSession
  );
  // Return empty if target session is invalid
  if (targetIndex === -1) return [];

  const endIndex = includeTarget ? targetIndex + 1 : targetIndex;
  const courses = [];

  for (let i = 0; i < endIndex; i++) {
    const { year, session } = orderedSessions[i];
    clonedPlan[year][session]?.forEach(course => {
      courses.push(cloneDeep(course));
    });
  };
  return courses;
};


/**
 * validateCourseDrop checks whether corequisites and prerequisites for the
 * dropped course are present in the correct sequence.
 * It also checks if a course can be added to winter or summer (if applicable).
 * 
 * @param {number} course - course being dropped
 * @param {Array<course>} previousSessionCourses - All courses from previous sessions
 * @param {Array<course>} currAndPrevSessionCourses - All courses up to / including target
 * @param {string} toSession - The target session (i.e. FALL)
 * @param {object} updatedPlan - The plan after the removal of the course
 * 
 * @returns {Promise<boolean>} - Resolves true if both requirements are met
 */
async function validateCourseDrop(movedCourse, previousSessionCourses, currAndPrevSessionCourses, toSession, updatedPlan) {
  try {
    // deconstruct the relevant properties from MovedCourse
    const { prerequisites = [], corequisites = [], offered_winter, offered_summer } = movedCourse;

    // Handle past coursework
    if (toSession === "PASTCOURSEWORK") {
      const pastCoursework = updatedPlan["year0"]?.["PastCoursework"] || [];
      // Prerequisites must already be in year0
      for (const reqId of prerequisites) {
        if (!pastCoursework.some((course) => course.id === reqId)) {
          console.error(`Prerequisite ${reqId} for Course ${movedCourse.id} must also be in PastCoursework.`);
          return false;
        }
      }
      // Corequisites must already be in year0
      for (const reqId of corequisites) {
        if (!pastCoursework.some((course) => course.id === reqId)) {
          console.error(`Corequisite ${reqId} for Course ${movedCourse.id} must also be in PastCoursework.`);
          return false;
        }
      }
    } else {
      // Rule 1: Course A is a prerequisite for Course B
      // Ensure all prerequisites for the course being dropped are present in previous sessions
      for (const reqId of prerequisites) {
        if (!previousSessionCourses.some((course => course.id === reqId))) {
          console.error(`Prerequisite ${reqId} not satisfied for Course ${movedCourse.id}`);
          return false;
        }
      }
      // Rule 2: Course C is a corequisite for Course B
      // Ensure all corequisites for the course being dropped are present in the target session or previous
      for (const reqId of corequisites) {
        if (!currAndPrevSessionCourses.some((course) => course.id === reqId)) {
          console.error(`Corequisite ${reqId} not satisfied for Course ${movedCourse.id}`);
          return false;
        }
      }
    }
    // Rule 1 and 2 satisfied

    // Additional check: is the course offered in summer or winter
    if (toSession === "SUMMER" && !offered_summer) {
      console.error("Course not offered in summer");
      return false;
    }
    if (toSession === "WINTER" && !offered_winter) {
      console.error("Course not offered in winter");
      return false;
    }


    return true;
  } catch (err) {
    console.error("Error validating course drop:", err);
    return false;
  }
}


/**
 * checkRequirementViolation examines sessions before the target session
 * to ensure none of the courses already scheduled there depend on the dropped course
 * 
 * @param {object} updatedPlan - The plan after the removal of the course
 * @param {string} targetYear - Target year for the dropped course
 * @param {string} targetSession - Target session for the dropped course
 * @param {course} droppedCourse - Course being dropped
 * 
 * @returns {Promise<boolean>} - Resolves to true if a dependency violation is found
 */
async function checkDependencyViolation(updatedPlan, targetYear, targetSession, droppedCourse) {
  const clonedPlan = cloneDeep(updatedPlan);
  const orderedSessions = getOrderedSessions(clonedPlan);
  const targetIndex = orderedSessions.findIndex(
    (s) => s.year === targetYear && s.session === targetSession
  );
  if (targetIndex === -1) return false;

  // Skip validation for PastCoursework
  if (targetSession === "PASTCOURSEWORK") {
    console.log("No dependency violation checks needed for past coursework.");
    return false;
  }
  
  // Iterate over sessions up to the one where the course is dropped (inclusive)
  for (let i = 0; i <= targetIndex; i++) {
    const { year, session } = orderedSessions[i];
    const courses = clonedPlan[year]?.[session] || [];

    for (const course of courses) {
      const { prerequisites = [], corequisites = [] } = course;
      console.log("Prerequisites for dropped course:", prerequisites);
      console.log("Corequisites for dropped course:", corequisites);
      // Rule 3: Course A cannot be placed after Course B
      // Check if the dropped course is a prerequisite for this course and verify the order
      if (prerequisites.includes(droppedCourse.id) && i <= targetIndex) {
        console.error(`Prerequisite rule violated: Course ${course.id} depends on ${droppedCourse.id}`);
        return true;
      }
      // Rule 4: Course C cannot be placed after course B
      if (corequisites.includes(droppedCourse.id)) {
        if (i > targetIndex) {
          console.error(`Corequisite rule violated: Course ${course.id} depends on ${droppedCourse.id}`);
          return true;
        }
        if (i < targetIndex && !clonedPlan[orderedSessions[targetIndex].year]?.[orderedSessions[targetIndex].session]?.some(
          (c) => c.id === droppedCourse.id)) {
          console.error("Corequisite must be in same or earlier session");
          return true;
        }
      }
    }
  }
  // No dependency violations found
  return false;
}

export { getCoursesUpTo, validateCourseDrop, checkDependencyViolation };





