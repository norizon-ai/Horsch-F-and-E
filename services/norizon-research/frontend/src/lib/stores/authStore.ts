/**
 * Auth0 Authentication Store
 *
 * Manages user authentication state using Auth0 SPA SDK.
 * Provides login, logout, token management, and user info.
 */

import { writable, derived } from 'svelte/store';
import { browser } from '$app/environment';
import {
	PUBLIC_AUTH0_DOMAIN,
	PUBLIC_AUTH0_CLIENT_ID,
	PUBLIC_AUTH0_AUDIENCE
} from '$env/static/public';

// Type imports only (won't be bundled during SSR)
import type { Auth0Client, User } from '@auth0/auth0-spa-js';

interface AuthState {
	isAuthenticated: boolean;
	isLoading: boolean;
	user: User | null;
	error: string | null;
}

const initialState: AuthState = {
	isAuthenticated: false,
	isLoading: true,
	user: null,
	error: null
};

// Create the auth store
function createAuthStore() {
	const { subscribe, set, update } = writable<AuthState>(initialState);
	let auth0Client: Auth0Client | null = null;
	let initPromise: Promise<void> | null = null;

	// Auth0 configuration from environment variables
	const auth0Config = {
		domain: PUBLIC_AUTH0_DOMAIN || '',
		clientId: PUBLIC_AUTH0_CLIENT_ID || '',
		authorizationParams: {
			redirect_uri: browser ? window.location.origin + '/callback' : '',
			audience: PUBLIC_AUTH0_AUDIENCE || ''
		},
		// Use localStorage to persist tokens across page reloads
		// Without this, tokens are stored in memory and lost on reload
		cacheLocation: 'localstorage' as const,
		// Use refresh tokens to maintain sessions
		useRefreshTokens: true
	};

	/**
	 * Initialize Auth0 client and check authentication status
	 */
	function initialize(): Promise<void> {
		if (!browser) return Promise.resolve();

		if (initPromise) {
			return initPromise;
		}

		initPromise = (async () => {
			try {
				console.log('📍 authStore.initialize() starting');
				console.log('📍 Auth0 config:', {
					domain: auth0Config.domain,
					clientId: auth0Config.clientId?.substring(0, 10) + '...',
					audience: auth0Config.authorizationParams.audience
				});

				update(state => ({ ...state, isLoading: true, error: null }));

				// Dynamically import Auth0 client (browser-only)
				const { createAuth0Client } = await import('@auth0/auth0-spa-js');

				// Create Auth0 client
				auth0Client = await createAuth0Client(auth0Config);
				console.log('✅ Auth0 client created');

				// Check if we're returning from Auth0 callback
				const query = window.location.search;
				console.log('📍 URL query:', query);

				if (query.includes('code=') && query.includes('state=')) {
					console.log('📍 Handling Auth0 callback...');
					try {
						const result = await auth0Client.handleRedirectCallback();
						console.log('✅ Callback handled successfully:', result);
						// Clean up URL
						window.history.replaceState({}, document.title, window.location.pathname);
					} catch (error) {
						console.error('❌ Error handling redirect callback:', error);
						update(state => ({
							...state,
							error: 'Authentication failed. Please try again.',
							isLoading: false
						}));
						return;
					}
				}

				// Check authentication status
				const isAuthenticated = await auth0Client.isAuthenticated();
				console.log('📍 isAuthenticated:', isAuthenticated);

				if (isAuthenticated) {
					const user = await auth0Client.getUser();
					console.log('✅ User authenticated:', user?.email);
					update(state => ({
						...state,
						isAuthenticated: true,
						user: user || null,
						isLoading: false
					}));
				} else {
					console.log('❌ User not authenticated');
					update(state => ({
						...state,
						isAuthenticated: false,
						user: null,
						isLoading: false
					}));
				}
			} catch (error) {
				console.error('❌ Auth initialization error:', error);
				update(state => ({
					...state,
					error: error instanceof Error ? error.message : 'Authentication initialization failed',
					isLoading: false
				}));
			}
		})();
		return initPromise;
	}

	/**
	 * Login with Auth0 (redirect to Auth0 login page)
	 */
	async function login() {
		// Check if Auth0 is configured
		if (!auth0Config.domain || !auth0Config.clientId) {
			console.error('❌ Auth0 not configured. Domain:', auth0Config.domain, 'ClientId:', auth0Config.clientId);
			console.error('❌ Environment variables:', {
				domain: PUBLIC_AUTH0_DOMAIN,
				clientId: PUBLIC_AUTH0_CLIENT_ID,
				audience: PUBLIC_AUTH0_AUDIENCE
			});
			alert('Authentication is not configured. Domain: ' + auth0Config.domain + ', Client ID: ' + auth0Config.clientId);
			return;
		}

		if (!auth0Client) {
			console.error('❌ Auth0 client not initialized');
			return;
		}

		try {
			await auth0Client.loginWithRedirect({
				authorizationParams: {
					redirect_uri: window.location.origin + '/callback'
				}
			});
		} catch (error) {
			console.error('❌ Login error:', error);
			update(state => ({
				...state,
				error: error instanceof Error ? error.message : 'Login failed'
			}));
		}
	}

	/**
	 * Logout from Auth0
	 */
	async function logout() {
		if (!auth0Client) {
			console.error('❌ Auth0 client not initialized');
			return;
		}

		try {
			// Update store state immediately to avoid UI flicker
			update(state => ({
				...state,
				isAuthenticated: false,
				user: null
			}));

			await auth0Client.logout({
				logoutParams: {
					returnTo: window.location.origin
				}
			});
		} catch (error) {
			console.error('❌ Logout error:', error);
			update(state => ({
				...state,
				error: error instanceof Error ? error.message : 'Logout failed'
			}));
		}
	}

	/**
	 * Get access token for API calls
	 */
	async function getAccessToken(): Promise<string | null> {
		if (!auth0Client) {
			console.error('❌ Auth0 client not initialized');
			return null;
		}

		try {
			const token = await auth0Client.getTokenSilently();
			return token;
		} catch (error) {
			console.error('❌ Error getting access token:', error);
			return null;
		}
	}

	/**
	 * Check if user is authenticated (async version)
	 */
	async function checkAuth(): Promise<boolean> {
		if (!auth0Client) return false;

		try {
			return await auth0Client.isAuthenticated();
		} catch (error) {
			console.error('❌ Error checking auth:', error);
			return false;
		}
	}

	return {
		subscribe,
		initialize,
		login,
		logout,
		getAccessToken,
		checkAuth
	};
}

export const authStore = createAuthStore();

// Derived store for easy access to auth state
export const isAuthenticated = derived(authStore, $auth => $auth.isAuthenticated);
export const currentUser = derived(authStore, $auth => $auth.user);
export const authLoading = derived(authStore, $auth => $auth.isLoading);
