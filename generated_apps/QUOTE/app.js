const quotes = [
    "The best way to predict the future is to invent it." - Alan Kay,
    "Life is what happens when you're busy making other plans." - John Lennon,
    "Get busy living or get busy dying." - Stephen King,
    "You only live once, but if you do it right, once is enough." - Mae West,
    "In the end, we will remember not the words of our enemies, but the silence of our friends." - Martin Luther King Jr.,
    "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment." - Ralph Waldo Emerson
];

function generateQuote() {
    const quoteElement = document.getElementById('quote');
    const randomIndex = Math.floor(Math.random() * quotes.length);
    quoteElement.textContent = quotes[randomIndex];
}

document.getElementById('generate-quote').addEventListener('click', generateQuote);