with open('submit-form-simple.php', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "\ = \->real_escape_string(\['firstName']);",
    "\ = isset(\['firstName']) ? \->real_escape_string(\['firstName']) : '';"
)

with open('submit-form-simple.php', 'w', encoding='utf-8') as f:
    f.write(content)
