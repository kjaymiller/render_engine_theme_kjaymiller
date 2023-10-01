// tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
    content: ['docs/output/**/*.{html, js}'],
    plugins: [require('@tailwindcss/typography')]
  }