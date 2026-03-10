/**
 * Protocol viewer layout - Authentication guard
 */

import { browser } from '$app/environment';
import { goto } from '$app/navigation';

export const load = async ({ url }) => {
	if (browser) {
		// Dynamically import to avoid SSR issues
		const { authStore } = await import('$lib/stores/authStore');

		// Check authentication
		const isAuth = await authStore.checkAuth();

		if (!isAuth) {
			// Redirect to landing page
			goto('/');
			return;
		}
	}

	return {};
};
