import { useState } from "react";
import CoursePopUp from "./CoursePopUp";
import { useDroppable, useDraggable } from '@dnd-kit/core';


function DraggableCourse({ course, semester, index, onClick }) {
    const { attributes, listeners, setNodeRef, transform } = useDraggable({
        id: `${semester}::${course}`, // Example: year_1-fall|CMSC 201
      });

    //   console.log("🧱 Course being rendered:", course);

      
  
    const style = transform
      ? { transform: `translate(${transform.x}px, ${transform.y}px)` }
      : undefined;
  
    return (
      <div
        ref={setNodeRef}
        className="course"
        style={style}
        {...listeners}
        {...attributes}
        onClick={onClick}
      >
        {course}
      </div>
    );
  }
  


function Session({semester, session_title, courses}){

    // console.log(semester)

    const [selectedCourse, setSelectedCourse] = useState(null);

    const { setNodeRef, isOver } = useDroppable({ id: semester });


    return(
        <>
            <div className="session">
                <div className="session-name">{session_title}</div>
                <div
                    ref={setNodeRef}
                    className={`session-courses ${isOver ? 'droppable-over' : ''}`}
                    >
                    {courses.length === 0 ? (
                        <div className="no-courses-added">No courses were added to this session.</div>
                        ) : (
                        courses.map((course, index) => (
                            // <div 
                            //     key={index} 
                            //     className="course"
                            //     onClick={() => {
                            //         console.log(`Course clicked: ${course}`);
                            //         setSelectedCourse(course);
                            //     }}
                            //     >
                            //         {course}
                                    
                            // </div>

                            <DraggableCourse
                                
                                key={index}
                                course={course}
                                semester={semester}
                                index={index}
                                onClick={() => setSelectedCourse(course)}
                            />
                            ))
                        )
                    }
                </div>
            </div>

            {selectedCourse && (
                <CoursePopUp
                    courseName={selectedCourse}
                    onClose={() => setSelectedCourse(null)}
                />
            )}
        </>
    )
}

export default Session