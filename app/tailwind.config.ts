import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        azure: {
          50: "#EFF6FF",
          100: "#DBEAFE",
          200: "#BFDBFE",
          300: "#93C5FD",
          400: "#60A5FA",
          500: "#3B82F6", // Primary shade
          600: "#2563EB",
          700: "#1D4ED8", // Darker shade for hover states
          800: "#1E40AF",
          900: "#1E3A8A",
        },
        // Secondary color: A warm, inviting orange reminiscent of reading lamps
        amber: {
          50: "#FFFBEB",
          100: "#FEF3C7",
          200: "#FDE68A",
          300: "#FCD34D",
          400: "#FBBF24",
          500: "#F59E0B", // Primary shade
          600: "#D97706", // Darker shade for hover states
          700: "#B45309",
          800: "#92400E",
          900: "#78350F",
        },
        // Accent color: A vibrant green for highlights and accents
        emerald: {
          50: "#ECFDF5",
          100: "#D1FAE5",
          200: "#A7F3D0",
          300: "#6EE7B7",
          400: "#34D399",
          500: "#10B981", // Primary shade
          600: "#059669", // Darker shade for hover states
          700: "#047857",
          800: "#065F46",
          900: "#064E3B",
        },
        // Neutral color: A warm gray for text and backgrounds
        stone: {
          50: "#FAFAF9",
          100: "#F5F5F4",
          200: "#E7E5E4",
          300: "#D6D3D1",
          400: "#A8A29E",
          500: "#78716C", // Primary shade for text
          600: "#57534E",
          700: "#44403C", // Darker shade for headings
          800: "#292524",
          900: "#1C1917",
        },
        // Background color: A soft, warm white
        cream: {
          50: "#FFFCF7", // Lightest shade for backgrounds
          100: "#FFFBF2",
          200: "#FFF8E6",
          300: "#FFF4D5",
          400: "#FFEFBE",
        },
      },
    },
  },
  plugins: [],
};
export default config;
