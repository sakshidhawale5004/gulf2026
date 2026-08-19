<?php
require 'config.php';

header('Content-Type: application/json');

$input = file_get_contents('php://input');
$data = json_decode($input, true);

// Get Stripe Secret Key from environment
$stripe_secret_key = STRIPE_SECRET_KEY;

// Validate input
if (!isset($data['firstName'], $data['email'], $data['amount'])) {
    http_response_code(400);
    echo json_encode(['error' => 'Missing required fields']);
    exit();
}

// Validate email
$email = filter_var($data['email'], FILTER_SANITIZE_EMAIL);
if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
    http_response_code(400);
    echo json_encode(['error' => 'Invalid email']);
    exit();
}

// Save to database first
try {
    $conn = getDBConnection();
    if ($conn) {
        $firstName = $conn->real_escape_string($data['firstName']);
        $lastName = isset($data['lastName']) ? $conn->real_escape_string($data['lastName']) : '';
        $phone = isset($data['phone']) ? $conn->real_escape_string($data['phone']) : '';
        $company = isset($data['company']) ? $conn->real_escape_string($data['company']) : '';
        $country = isset($data['country']) ? $conn->real_escape_string($data['country']) : '';
        $transactionType = isset($data['transactionType']) ? $conn->real_escape_string($data['transactionType']) : '';
        $message = isset($data['message']) ? $conn->real_escape_string($data['message']) : '';
        $amount = (int)$data['amount'];
        
        // Get IP address
        $ip = isset($_SERVER['HTTP_CF_CONNECTING_IP']) ? $_SERVER['HTTP_CF_CONNECTING_IP'] : $_SERVER['REMOTE_ADDR'];
        $ip = $conn->real_escape_string($ip);
        
        // Store in form_responses table with payment status
        $sql = "INSERT INTO form_responses (form_type, first_name, last_name, email, phone, company, service, country, message, ip_address, amount, payment_status)
                VALUES ('Payment', '$firstName', '$lastName', '$email', '$phone', '$company', '$transactionType', '$country', '$message', '$ip', '$amount', 'pending')";
        
        $conn->query($sql);
        $conn->close();
    }
} catch (Exception $e) {
    // Continue anyway
}

// Create Stripe Checkout Session
$ch = curl_init('https://api.stripe.com/v1/checkout/sessions');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_USERPWD, $stripe_secret_key . ':');
$stripe_data = [
    'payment_method_types' => ['card'],
    'line_items' => [
        [
            'price_data' => [
                'currency' => 'usd',
                'product_data' => [
                    'name' => 'GCC Benchmark Search',
                ],
                'unit_amount' => 75000, // $750.00
            ],
            'quantity' => 1,
        ],
    ],
    'mode' => 'payment',
    'success_url' => 'https://gulftp.com/index.html?payment=success',
    'cancel_url' => 'https://gulftp.com/book-search.html?payment=cancel',
];
// http_build_query works nicely for Stripe's expected x-www-form-urlencoded structure
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($stripe_data));
$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$session = json_decode($response, true);

if ($httpcode != 200 || !isset($session['id'])) {
    http_response_code(500);
    echo json_encode(['error' => 'Failed to create Stripe session', 'details' => $session]);
    exit();
}

// Return Stripe session ID and public key for client-side redirection
echo json_encode([
    'success' => true,
    'stripePublicKey' => STRIPE_PUBLISHABLE_KEY,
    'sessionId' => $session['id']
]);
?>
