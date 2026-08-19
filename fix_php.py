with open('submit-form-simple.php', 'r', encoding='utf-8') as f:
    content = f.read()

target = '''// Validate required fields
if (!isset(['firstName']) || empty(trim(['firstName']))) {
    http_response_code(400);
    echo json_encode(['error' => 'First name is required']);
    exit();
}'''

replacement = '''// Validate required fields
 = isset(['form_type']) ? ['form_type'] : (isset(['service']) ? ['service'] : 'General Inquiry');

if ( !== 'Newsletter') {
    if (!isset(['firstName']) || empty(trim(['firstName']))) {
        http_response_code(400);
        echo json_encode(['error' => 'First name is required']);
        exit();
    }
}'''

content = content.replace(target, replacement)

with open('submit-form-simple.php', 'w', encoding='utf-8') as f:
    f.write(content)
