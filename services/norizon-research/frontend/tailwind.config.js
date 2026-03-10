import tailwindcssAnimate from 'tailwindcss-animate';

/** @type {import('tailwindcss').Config} */
export default {
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				// Legacy norizon colors (for backwards compatibility)
				norizon: {
					orange: {
						light: '#ff8a65',
						DEFAULT: '#ff6b35',
						dark: '#e55a2b'
					},
					blue: {
						light: '#60a5fa',
						DEFAULT: '#3b82f6',
						dark: '#1e40af'
					},
					gray: {
						50: '#f9fafb',
						100: '#f3f4f6',
						200: '#e5e7eb',
						300: '#d1d5db',
						400: '#9ca3af',
						500: '#6b7280',
						600: '#4b5563',
						700: '#374151',
						800: '#1f2937',
						900: '#111827'
					}
				},
				// New Nora design system colors
				'nora-orange': {
					50: '#FFF7ED',
					100: '#FFEDD5',
					200: '#FED7AA',
					300: '#FDBA74',
					400: '#FB923C',
					500: '#F97316',
					600: '#EA580C',
					700: '#C2410C',
					800: '#9A3412',
					900: '#7C2D12'
				},
				'nora-blue': {
					50: '#EFF6FF',
					100: '#DBEAFE',
					200: '#BFDBFE',
					300: '#93C5FD',
					400: '#60A5FA',
					500: '#3B82F6',
					600: '#2563EB',
					700: '#1D4ED8',
					800: '#1E40AF',
					900: '#1E3A8A'
				},
				'nora-slate': {
					50: '#F8FAFC',
					100: '#F1F5F9',
					200: '#E2E8F0',
					300: '#CBD5E1',
					400: '#94A3B8',
					500: '#64748B',
					600: '#475569',
					700: '#334155',
					800: '#1E293B',
					900: '#0F172A'
				},
				'nora-green': {
					100: '#DCFCE7',
					500: '#22C55E'
				},
				'deep-blue': '#1E3A5F',
				// shadcn semantic color tokens
				border: 'hsl(var(--border) / <alpha-value>)',
				input: 'hsl(var(--input) / <alpha-value>)',
				ring: 'hsl(var(--ring) / <alpha-value>)',
				background: 'hsl(var(--background) / <alpha-value>)',
				foreground: 'hsl(var(--foreground) / <alpha-value>)',
				primary: {
					DEFAULT: 'hsl(var(--primary) / <alpha-value>)',
					foreground: 'hsl(var(--primary-foreground) / <alpha-value>)'
				},
				secondary: {
					DEFAULT: 'hsl(var(--secondary) / <alpha-value>)',
					foreground: 'hsl(var(--secondary-foreground) / <alpha-value>)'
				},
				destructive: {
					DEFAULT: 'hsl(var(--destructive) / <alpha-value>)',
					foreground: 'hsl(var(--destructive-foreground) / <alpha-value>)'
				},
				muted: {
					DEFAULT: 'hsl(var(--muted) / <alpha-value>)',
					foreground: 'hsl(var(--muted-foreground) / <alpha-value>)'
				},
				accent: {
					DEFAULT: 'hsl(var(--accent) / <alpha-value>)',
					foreground: 'hsl(var(--accent-foreground) / <alpha-value>)'
				},
				popover: {
					DEFAULT: 'hsl(var(--popover) / <alpha-value>)',
					foreground: 'hsl(var(--popover-foreground) / <alpha-value>)'
				},
				card: {
					DEFAULT: 'hsl(var(--card) / <alpha-value>)',
					foreground: 'hsl(var(--card-foreground) / <alpha-value>)'
				}
			},
			fontFamily: {
				sans: ['DM Sans', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'sans-serif'],
				serif: ['Fraunces', 'Georgia', 'serif']
			},
			borderRadius: {
				'nora-sm': '6px',
				'nora-md': '10px',
				'nora-lg': '16px',
				// shadcn border-radius tokens
				lg: 'var(--radius)',
				md: 'calc(var(--radius) - 2px)',
				sm: 'calc(var(--radius) - 4px)'
			},
			boxShadow: {
				'nora-sm': '0 1px 2px rgba(15, 23, 42, 0.05)',
				'nora-md': '0 4px 12px rgba(15, 23, 42, 0.08)',
				'nora-lg': '0 12px 32px rgba(15, 23, 42, 0.12)'
			},
			animation: {
				'pulse-slow': 'pulse 3s cubic-bezier(0.4, 0, 0.6, 1) infinite',
				'fade-in': 'fadeIn 0.3s ease-in-out',
				'spin-slow': 'spin 2s linear infinite',
				shimmer: 'shimmer 2s infinite ease-in-out',
				typing: 'typing 1.4s infinite ease-in-out'
			},
			keyframes: {
				fadeIn: {
					'0%': { opacity: '0', transform: 'translateY(10px)' },
					'100%': { opacity: '1', transform: 'translateY(0)' }
				},
				shimmer: {
					'0%': { 'background-position': '-200% 0' },
					'100%': { 'background-position': '200% 0' }
				},
				typing: {
					'0%, 60%, 100%': { transform: 'translateY(0)' },
					'30%': { transform: 'translateY(-4px)' }
				}
			}
		}
	},
	plugins: [tailwindcssAnimate]
};
