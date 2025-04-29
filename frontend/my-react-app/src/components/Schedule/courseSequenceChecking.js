import axios from "axios";

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
 * NOTE: These functions still need to be unit tested
 */

// Note that a plan is structured like this
/**
 * const emptyNestedPlan = {
          year1: {Fall: [], Winter: [], Spring: [], Summer: []},
          year2: {Fall: [], Winter: [], Spring: [], Summer: []},
          year3: {Fall: [], Winter: [], Spring: [], Summer: []},
          year4: {Fall: [], Winter: [], Spring: [], Summer: []},
        };
 *  
 */

// Return an ordered array of session keys from the plan
const getOrderedSessions = (plan) => {
  const orderedSessions = [];
  // sort year keys to guarantee ascending order
  const yearKeys = Object.keys(plan).sort();
  const sessionOrder = ["Fall", "Winter", "Spring", "Summer"];
  yearKeys.forEach(year => {
    sessionOrder.forEach(session => {
      if (plan[year]?.[session]) {
        orderedSessions.push({ year, session });
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
  // Return empty if target session is invalid
  if (targetIndex === -1) return [];

  const endIndex = includeTarget ? targetIndex + 1 : targetIndex;
  const courseIds = [];

  for (let i = 0; i < endIndex; i++) {
    const { year, session } = orderedSessions[i];
    plan[year][session]?.forEach(course => {
      courseIds.push(Number(course[0]));
    });
  };
  return courseIds;
};

// use this cache to map course IDs to their requirements
const requirementsCache = {};

// selective clearing of cache
function invalidateCacheForCourse(courseId) {
  console.log("Invalidating cache");
  delete requirementsCache[courseId];
}

// total clearing of cache
function clearRequirementsCache() {
  Object.keys(requirementsCache).forEach(key => delete requirementsCache[key]);
}
// Global lock tracking for course requirements
const fetchLocks = {};

/**
 * getCourseRequirements fetches the course requirements while caching
 * the result. This helper function is used in checkDependencyViolation
 * and in validateCourseDrop
 * 
 * @param {number} courseId - The id of the course for which requirements are retrieved
 */
async function getCourseRequirements(courseId) {
  console.log("Getting requirements for the course id", courseId);
  // Check if a fetch is already in progress
  if (fetchLocks[courseId]) {
    console.log("Waiting for lock");
    return fetchLocks[courseId];
  }

  // If requirements have already been fetched, return
  if (requirementsCache[courseId] !== undefined) {
    if (requirementsCache[courseId] === null) {
      console.error("Failed fetch previously recorded");
      return null;
    }
    console.log(`Cache hit for Course ${courseId}:`, requirementsCache[courseId]);
    return requirementsCache[courseId];
  }

  // start the fetch proces and store the Promise in fetchLocks
  const fetchPromise = (async () => {
    try {
      const response = await axios.get(`http://127.0.0.1:5000/api/v2/courses/${courseId}/requirements`);
      // Cache and return the data    
      const data = response.data;
      // Normalize prerequisites and corequisites
      data.prerequisites = data.prerequisites.map(p => Number(p));
      data.corequisites = data.corequisites.map(c => Number(c));
      console.log(`Normalized requirements for Course ${courseId}:`, data);
      requirementsCache[courseId] = data;
      return data;
  
    } catch (err) {
      console.error(`Error fetching requirements for course ${courseId}`, err);
      // return null to indicate failure
      requirementsCache[courseId] = null;
      return null;
    } finally {
      // Remove lock
      console.log("Lock removed");
      delete fetchLocks[courseId];
    }
  })();
  console.log("Lock set");
  fetchLocks[courseId] = fetchPromise;
  return fetchPromise;
}


/**
 * validateCourseDrop uses the getCourseRequirements helper to fetch prerequisites and corequisites
 * for a given course, then check whether they are present.
 * 
 * @param {number} courseId - Id of the course being dropped
 * @param {Array<number>} previousSessionCourseIds - All course IDs from previous sessions
 * @param {Array<number>}} currAndPrevSessionCourseIds - All course IDs up to / including target
 * 
 * @returns {Promise<boolean>} - Resolves true if both requirements are met
 */
async function validateCourseDrop(courseId, previousSessionCourseIds, currAndPrevSessionCourseIds) {
  try {
    // Fetch course requirements from API endpoint
    console.log("This is the course id", courseId);
    const requirements = await getCourseRequirements(courseId);
    if (!requirements) {
      console.error(`Failed to retrieve requirements for course ${courseId}`);
      return false;
    }

    const { prerequisites, corequisites } = requirements;

    // Rule 1: Course A is a prerequisite for Course B
    // Ensure all prerequisites for the course being dropped are present in previous sessions
    for (const reqId of prerequisites) {
      if (!previousSessionCourseIds.includes(Number(reqId))) {
        console.error(`Prerequisite ${reqId} not satisfied for Course ${courseId}`);
        return false;
      }
    }

    // Rule 2: Course C is a corequisite for Course B
    // Ensure all corequisites for the course being dropped are present in the target session or previous
    for (const reqId of corequisites) {
      if (!currAndPrevSessionCourseIds.includes(Number(reqId))) {
        console.error(`Corequisite ${reqId} not satisfied for Course ${courseId}`);
        return false;
      }
    }
    // Rule 1 and 2 satisfied
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
 * @param {number|string} droppedCourseId - The id of the course being moved
 * 
 * @returns {Promise<boolean>} - Resolves to true if a dependency violation is found
 */
async function checkDependencyViolation(updatedPlan, targetYear, targetSession, droppedCourseId) {
  const orderedSessions = getOrderedSessions(updatedPlan);
  const droppedSessionIndex = orderedSessions.findIndex(
    s => s.year === targetYear && s.session === targetSession
  );

  console.log("Dropped Session Details:", { targetYear, targetSession, droppedSessionIndex });
  console.log("Ordered Sessions:", orderedSessions);

  // Iterate over all sessions
  for (let i = 0; i < orderedSessions.length; i++) {
    const { year, session } = orderedSessions[i];
    const courses = updatedPlan[year]?.[session] || [];
    console.log("Current session:", { year, session, index: i, courses });

    for (const course of courses) {
      // Fetch (or retrieve from cache) course requirements
      const requirements = await getCourseRequirements(course[0]);
      if (!requirements) continue;
      const { prerequisites, corequisites } = requirements;
      console.log(`Course ${course[0]} prerequisites:`, prerequisites);
      console.log(`Course ${course[0]} corequisites:`, corequisites);

      // Rule 3: Course A cannot be placed after Course B
      // Check if the dropped course is a prerequisite for this course and verify the order
      if (prerequisites.includes(Number(droppedCourseId)) && i <= droppedSessionIndex) {
        console.error(`Prerequisite rule violated: Course ${course[0]} depends on ${droppedCourseId}`);
        return true;
      }
      // Rule 4: Course C cannot be placed after course B
      if (corequisites.includes(Number(droppedCourseId))) {
        if (i > droppedSessionIndex) {
          console.error(`Corequisite rule violated: Course ${course[0]} depends on ${droppedCourseId}`);
          return true;
        }
        if (i < droppedSessionIndex && !updatedPlan[orderedSessions[droppedSessionIndex].year]?.[orderedSessions[droppedSessionIndex].session]?.some(c => c[0] === droppedCourseId)) {
          console.error("Corequisite must be in same or earlier session");
          return true;
        }
      }
    }
  }
  // No dependency violations found
  return false;
}

export { getCourseIdsUpTo, validateCourseDrop, checkDependencyViolation, invalidateCacheForCourse };





