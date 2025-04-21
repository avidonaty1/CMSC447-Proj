import { useState } from "react";
import axios from "axios";

function Login({ onLogin }) {
    const [email, setEmail] = useState("");
    const [error, setError] = useState("");

    // Handles the "Continue as Guest" button click
    const handleGuestLogin = () => {
        // Set the studentId to 0 in App
        onLogin(0);
    };

    // Handles the "Confirm" button click
    const handleLogin = async () => {
        try {
            // Validate that email (or at lest text) is entered before sending request
            if (!email) {
                setError("Email is required");
                return;
            }

            // Fetch student ID based on email
            const response = await axios.get(`/api/v2/students/email/${email}`);
            const studentId = response.data.student_id;

            // Pass the studentId to the App
            onLogin(studentId);
        } catch (err) {
            console.error("Error logging in:", err);
            setError("Invalid email or unable to fetch student information.");
        }
    };

    return (
        <div className="login-page">
            <h1>Welcome to the UMBC course planner tool</h1>
            <button onClick={handleGuestLogin}>Continue as Guest</button>
            <div className="login-form">
                <input
                    type="email"
                    placholder="Enter email to log in"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <button onClick={handleLogin}>Confirm</button>
            </div>
            {error && <p className="error-message">{error}</p>}
        </div>
    );
}

export default Login;