/**
 * Root layout - Global authentication guard
 * Protects all routes except landing page and callback
 */

import { browser } from '$app/environment';
import { redirect } from '@sveltejs/kit';

export const ssr = false;

export const load = async ({ url }) => {
	// Allow these routes without authentication
	const publicRoutes = ['/', '/callback', '/auth-test'];
	const isPublicRoute = publicRoutes.includes(url.pathname);

	if (browser && !isPublicRoute) {
		// Dynamically import to avoid SSR issues
		const { authStore } = await import('$lib/stores/authStore');

		// Initialize auth and wait for it
		await authStore.initialize();

		// Check authentication
		const isAuth = await authStore.checkAuth();

		if (!isAuth) {
			// Hard route interrupt directly back to the landing page
			throw redirect(307, '/');
		}
	}

	return {};
};
