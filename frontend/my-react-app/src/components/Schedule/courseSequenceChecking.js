import axios from "axios";

/**
 * These helper functions are used for course requirement checking
 * in the Schedule component so that dragged/dropped courses
 * do not violate the course sequence of prerequisites and corequisites.
 * 
 * NOTE: These functions need to be tested further as there are some
 * flaws noted in manual testing
 */

// Return an ordered array of session keys from the plan
const getOrderedSessions = (plan) => {
    const orderedSessions = [];
    // sort year keys to guarantee ascending order
    const yearKeys = Object.keys(plan).sort();
    const sessionOrder = ["Fall", "Winter", "Spring", "Summer"];
    yearKeys.forEach(year => {
      sessionOrder.forEach(session => {
        if (plan[year][session] !== undefined) {
          orderedSessions.push({year, session});
        }
      });
    });
    return orderedSessions;
  };


  // Get all course IDs from sessions that come before (or up to) a target session
  // If includeTarget is false, only sessions strictly before
  const getCourseIdsUpTo = (plan, targetYear, targetSession, includeTarget = false) => {
    const orderedSessions = getOrderedSessions(plan);
    const targetIndex = orderedSessions.findIndex(
      s => s.year === targetYear && s.session === targetSession
    );
    if (targetIndex === -1) return [];
    const endIndex = includeTarget ? targetIndex + 1 : targetIndex;
    const courseIds = [];
    for (let i = 0; i < endIndex; i++) {
      const { year, session } = orderedSessions[i];
      plan[year][session].forEach(course => {
        courseIds.push(Number(course[0]));
      });
    };
    return courseIds;
  };

  // use this cache to map course IDs to their requirements
  const requirementsCache = {};


  /**
   * getCourseRequirements fetches the course requirements while caching
   * the result. This helper function is used in checkDependencyViolation
   * and in validateCourseDrop
   * 
   * @param {number} courseId - The id of the course for which requirements are retrieved
   */
   async function getCourseRequirements(courseId) {
    // If requirements have already been fetched, return
    if (requirementsCache[courseId]){
        return requirementsCache[courseId];
    }

    try {
      // const response = await axios.get(`http://127.0.0.1:5000/api/v2/courses/${courseId}/requirements`);
      const response = await axios.get(`/api/v2/courses/${courseId}/requirements`);

      // Cache and return the data
      requirementsCache[courseId] = response.data;
      return response.data;
    } catch (err) {
      console.error(`Error fetching requirements for course ${courseId}`, err);
      // return null to indicate failure
      requirementsCache[courseId] = null;
      return null;
    }
   }


  /**
   * validateCourseDrop uses the getCourseRequirements helper to fetch prerequisites and corequisites
   * for a given course, then check whether they are present.
   * 
   * @param {number} courseId - Id of the course being dropped
   * @param {Array<number>} previousSessionCourseIds - All course IDs from previous sessions
   * @param {Array{number}} currAndPrevSessionCourseIds - All course IDs up to / including target
   * 
   * @returns {Promise<boolean} - Resolves true if both requirements are met
   */
  async function validateCourseDrop(courseId, previousSessionCourseIds, currAndPrevSessionCourseIds) {
    try {
      // Fetch course requirements from API endpoint
      const requirements = await getCourseRequirements(courseId);
      if (!requirements) {
        console.error(`Failed to retrieve requirements for course ${courseId}`);
        return false;
      }
      const {prerequisites, corequisites } = requirements;

      // Check that prerequisites and corequisites are met
      const prerequisitesMet = prerequisites.every(reqId =>
        previousSessionCourseIds.includes(reqId)
      );
      const corequisitesMet = corequisites.every(reqId =>
        currAndPrevSessionCourseIds.includes(reqId)
      );

      if (!prerequisitesMet) {
        alert("Prequisites for this course are not met in previous sessions.");
        return false;
      }
      if (!corequisitesMet) {
        alert("Corequisites for this course are not met in current or previous sessions.");
        return false;
      }
      // Otherwise, it is ok to drop the course
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
   * @param {object} updatedPlan - The plan afte rthe removal of the course
   * @param {string} targetYear - Target year for the dropped course
   * @param {string} targetSession - Target session for the dropped course
   * @param {number|string} droppedCourseId - The id of the course being moved
   * 
   * @returns {Promise<boolean} - Resolves to true if a dependency violation is found
   */
  async function checkDependencyViolation(updatedPlan, targetYear, targetSession, droppedCourseId) {
    const orderedSessions = getOrderedSessions(updatedPlan);
    const targetIndex = orderedSessions.findIndex(
      (s) => s.year === targetYear && s.session === targetSession
    );
    if (targetIndex === -1) return false;

    // Iterate over sessions that come before the target session
    for (let i = 0; i < targetIndex; i++) {
      const { year, session } = orderedSessions[i];
      for (let courseTuple of updatedPlan[year][session]) {
        // Fetch (or retrieve from cache) course requirements
        const requirements = await getCourseRequirements(courseTuple[0]);
        if (requirements && requirements.prerequisites.includes(Number(droppedCourseId))) {
          return true;
        }
      }
    }
    return false;
  }
 
  export {getCourseIdsUpTo, validateCourseDrop, checkDependencyViolation};





