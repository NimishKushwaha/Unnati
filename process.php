<?php
error_reporting(E_ALL);
ini_set('display_errors', 1);

// Connect to the database
$host = 'localhost';
$user = 'root';
$password = 'sandesh'; // Change this to your actual database password
$database = 'unnatidata';

$conn = new mysqli($host, $user, $password, $database);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Handle Signup Form Submission
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['submit-signup'])) {
    $username = $_POST['username'];
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Hash the password before storing it in the database
    $hashed_password = password_hash($password, PASSWORD_DEFAULT);

    // Insert user data into the database
    $sql = "INSERT INTO users (username, email, password) VALUES (?, ?, ?)";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("sss", $username, $email, $hashed_password);

    if ($stmt->execute()) {
        // Signup successful
        header('Location: index.html#sign-in-form'); // Redirect to the login section on the same page
        exit();
    } else {
        // Handle signup error
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Handle Login Form Submission
if ($_SERVER["REQUEST_METHOD"] == "POST" && isset($_POST['sign-in-btn'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];

    // Check user credentials
    $stmt = $conn->prepare("SELECT * FROM users WHERE username = ?");
    $stmt->bind_param("s", $username);
    $stmt->execute();
    $result = $stmt->get_result();

    if ($result->num_rows == 1) {
        $row = $result->fetch_assoc();
        // Verify the password
        if (password_verify($password, $row['password'])) {
            // User authentication successful
            header('Location: home.html'); // Redirect to the dashboard or any desired page after successful login
            exit();
        } else {
            // Handle incorrect password
            echo "Invalid password";
        }
    } else {
        // Handle non-existent username
        echo "User not found";
    }

    $stmt->close();
}

$conn->close();
?>
