/**
 * Authentication Guard Utility
 *
 * Protects routes by checking authentication status.
 * Redirects to landing page if not authenticated.
 */

import { authStore } from '$lib/stores/authStore';
import { goto } from '$app/navigation';
import { get } from 'svelte/store';

/**
 * Check if user is authenticated, redirect to landing if not
 */
export async function requireAuth() {
	const auth = get(authStore);

	// Wait for auth to finish loading
	if (auth.isLoading) {
		// Wait for initialization
		await new Promise((resolve) => {
			const unsubscribe = authStore.subscribe((state) => {
				if (!state.isLoading) {
					unsubscribe();
					resolve(true);
				}
			});
		});
	}

	// Check if authenticated
	const isAuth = await authStore.checkAuth();

	if (!isAuth) {
		// Redirect to landing page
		goto('/');
		return false;
	}

	return true;
}
