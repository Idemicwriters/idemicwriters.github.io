<?php
if($_SERVER["REQUEST_METHOD"] == "POST"){
    // Get form data
    $name = $_POST['name'];
    $email = $_POST['email'];
    $message = $_POST['message'];
    
    // Email details
    $to = "kiamba2munyao@gmail.com"; 
    $subject = "Message from $name via Idemic Writers website";
    $body = "Name: $name\nEmail: $email\n\n$message";

    // Send email
    if(mail($to, $subject, $body)){
        echo "Thank you! Your message has been sent.";
    } else{
        echo "Oops! Something went wrong. Please try again later.";
    }
}
?>
