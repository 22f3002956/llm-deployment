document.getElementById('convert-btn').addEventListener('click', function() {
    const markdownInput = document.getElementById('markdown-input').value;
    const output = document.getElementById('output');
    output.innerHTML = marked(markdownInput);
});

// Load the marked library
const script = document.createElement('script');
script.src = 'https://cdnjs.cloudflare.com/ajax/libs/marked/2.1.3/marked.min.js';
document.head.appendChild(script);