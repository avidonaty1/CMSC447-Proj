import Session from "./Session"

function Schedule(){

    return (

        <div className="schedule">
            <div class= "schedule-year">
                <Session></Session>
                <Session></Session>
                
            </div>
            <div class= "schedule-year">
                <Session></Session>
                <Session></Session>
            </div>
            <div class= "schedule-year">
                <Session></Session>
                <Session></Session>
            </div>
            <div class= "schedule-year">
                <Session></Session>
                <Session></Session>
            </div>
        
        </div>
        
    )
}

export default Schedule