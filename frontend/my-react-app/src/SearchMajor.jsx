import { useState } from "react"
import Select from "react-select"



function searchMajor(){

    const options = [
        {value: "Computer Science", label: "Computer Science"},
        {value: "Computer Engineering", label: "Computer Engineering"},
        {value: "Mathematics", label: "Mathematics"},
        {value: "Random Major", label: "Random Major"},
        {value: "Computer Science", label: "Computer Science"},
        {value: "Computer Engineering", label: "Computer Engineering"},
        {value: "Mathematics", label: "Mathematics"},
        {value: "Random Major", label: "Random Major"},
        {value: "Computer Science", label: "Computer Science"},
        {value: "Computer Engineering", label: "Computer Engineering"},
        {value: "Mathematics", label: "Mathematics"},
        {value: "Random Major", label: "Random Major"},
    ];

    const [selectedOptions, setSelectedOptions] = useState([]);

    const handleChange = selected => {
        setSelectedOptions(selected);
        console.log("Selected options:", selected)
    };


    return (
        <div class = "selectMajor">

            <label class="select-major-text" for="major">Selected a major: </label>

            <Select
                classNamePrefix= "select-box"
                options ={options}
                isSearchable
                value ={selectedOptions}
                onChange={handleChange}
                placeholder="Choose a major"
            />
        </div>
    )
}

export default searchMajor