import { browser } from '$app/environment';
import { init, register } from 'svelte-i18n';

// Register locales using static imports (works with SSR)
register('de', () => import('./locales/de.json'));
register('en', () => import('./locales/en.json'));

// Get stored locale preference or default to German
function getInitialLocale(): string {
	if (browser) {
		const stored = localStorage.getItem('locale');
		if (stored && ['de', 'en'].includes(stored)) {
			return stored;
		}
	}
	return 'de'; // Default to German
}

// Initialize i18n
init({
	fallbackLocale: 'de',
	initialLocale: getInitialLocale(),
});

export { t, locale, locales } from 'svelte-i18n';
