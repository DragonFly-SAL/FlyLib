/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        "primary": "#dd0426",
        "secondary": "#273043",
        "tertiary": "#9197ae",
        "bg": "#eff6ee"
      }
    },
  },
  plugins: [],
}