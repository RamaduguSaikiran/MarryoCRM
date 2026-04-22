/** @type {import('tailwindcss').Config} */
export default {
  content: [
    './src/**/*.{html,js,svelte,ts}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        // Using hsl(var(--X-hsl) / <alpha-value>) format enables opacity modifiers
        // e.g. bg-background/95, text-muted-foreground/70, border-border/50, etc.
        border: 'hsl(var(--border-hsl) / <alpha-value>)',
        input: 'hsl(var(--input-hsl) / <alpha-value>)',
        ring: 'hsl(var(--ring-hsl) / <alpha-value>)',
        background: 'hsl(var(--background-hsl) / <alpha-value>)',
        foreground: 'hsl(var(--foreground-hsl) / <alpha-value>)',
        primary: {
          DEFAULT: 'hsl(var(--primary-hsl) / <alpha-value>)',
          foreground: 'hsl(var(--primary-foreground-hsl) / <alpha-value>)',
        },
        secondary: {
          DEFAULT: 'hsl(var(--secondary-hsl) / <alpha-value>)',
          foreground: 'hsl(var(--secondary-foreground-hsl) / <alpha-value>)',
        },
        destructive: {
          DEFAULT: 'hsl(var(--destructive-hsl) / <alpha-value>)',
        },
        muted: {
          DEFAULT: 'hsl(var(--muted-hsl) / <alpha-value>)',
          foreground: 'hsl(var(--muted-foreground-hsl) / <alpha-value>)',
        },
        accent: {
          DEFAULT: 'hsl(var(--accent-hsl) / <alpha-value>)',
          foreground: 'hsl(var(--accent-foreground-hsl) / <alpha-value>)',
        },
        popover: {
          DEFAULT: 'hsl(var(--popover-hsl) / <alpha-value>)',
          foreground: 'hsl(var(--popover-foreground-hsl) / <alpha-value>)',
        },
        card: {
          DEFAULT: 'hsl(var(--card-hsl) / <alpha-value>)',
          foreground: 'hsl(var(--card-foreground-hsl) / <alpha-value>)',
        },
        sidebar: {
          DEFAULT: 'hsl(var(--sidebar-hsl) / <alpha-value>)',
          foreground: 'hsl(var(--sidebar-foreground-hsl) / <alpha-value>)',
          primary: 'hsl(var(--sidebar-primary-hsl) / <alpha-value>)',
          'primary-foreground': 'hsl(var(--sidebar-primary-foreground-hsl) / <alpha-value>)',
          accent: 'hsl(var(--sidebar-accent-hsl) / <alpha-value>)',
          'accent-foreground': 'hsl(var(--sidebar-accent-foreground-hsl) / <alpha-value>)',
          border: 'hsl(var(--sidebar-border-hsl) / <alpha-value>)',
          ring: 'hsl(var(--sidebar-ring-hsl) / <alpha-value>)',
        },
        chart: {
          1: 'var(--chart-1)',
          2: 'var(--chart-2)',
          3: 'var(--chart-3)',
          4: 'var(--chart-4)',
          5: 'var(--chart-5)',
        },
      },
      borderRadius: {
        lg: 'var(--radius)',
        md: 'calc(var(--radius) - 2px)',
        sm: 'calc(var(--radius) - 4px)',
      },
      fontFamily: {
        sans: ['Inter', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
        serif: ['Cormorant Garamond', 'Georgia', 'Times New Roman', 'serif'],
        mono: ['SF Mono', 'Fira Code', 'Consolas', 'monospace'],
      },
    },
  },
  plugins: [],
}
