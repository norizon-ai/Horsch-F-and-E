/**
 * Azure Entra External ID (CIAM) Authentication Store
 *
 * Manages user authentication state using MSAL.js.
 * Provides login, logout, token management, and user info.
 * Uses Email OTP flow via Entra External ID.
 */

import { writable, derived } from 'svelte/store';
import { browser } from '$app/environment';
import {
	PUBLIC_AZURE_CLIENT_ID,
	PUBLIC_AZURE_AUTHORITY
} from '$env/static/public';

import type { PublicClientApplication, AccountInfo, AuthenticationResult } from '@azure/msal-browser';

interface AuthUser {
	email: string;
	name: string;
	sub: string;
}

interface AuthState {
	isAuthenticated: boolean;
	isLoading: boolean;
	user: AuthUser | null;
	error: string | null;
}

const initialState: AuthState = {
	isAuthenticated: false,
	isLoading: true,
	user: null,
	error: null
};

// Default scopes for CIAM — openid/profile/email are added automatically by MSAL
const loginScopes = ['openid', 'profile', 'email', 'offline_access'];

function createAuthStore() {
	const { subscribe, update } = writable<AuthState>(initialState);
	let msalInstance: PublicClientApplication | null = null;
	let initPromise: Promise<void> | null = null;

	function accountToUser(account: AccountInfo): AuthUser {
		return {
			email: account.username || '',
			name: account.name || '',
			sub: account.localAccountId || account.homeAccountId || ''
		};
	}

	function initialize(): Promise<void> {
		if (!browser) return Promise.resolve();

		if (initPromise) {
			return initPromise;
		}

		initPromise = (async () => {
			try {
				update(state => ({ ...state, isLoading: true, error: null }));

				const { PublicClientApplication: MSAL } = await import('@azure/msal-browser');

				msalInstance = new MSAL({
					auth: {
						clientId: PUBLIC_AZURE_CLIENT_ID || '',
						authority: PUBLIC_AZURE_AUTHORITY || '',
						redirectUri: window.location.origin + '/callback',
						postLogoutRedirectUri: window.location.origin,
						knownAuthorities: ['norizonauth.ciamlogin.com']
					},
					cache: {
						cacheLocation: 'localStorage'
					}
				});

				await msalInstance.initialize();

				// Handle redirect response (returns null if not coming from a redirect)
				let response: AuthenticationResult | null = null;
				try {
					response = await msalInstance.handleRedirectPromise();
					if (response) {
						console.log('Redirect response handled, account:', response.account?.username);
					}
				} catch (error) {
					// Stale interaction state — not a real failure.
					// Fall through to check cached accounts.
					console.warn('handleRedirectPromise error:', (error as any)?.errorCode);
				}

				const accounts = msalInstance.getAllAccounts();
				if (accounts.length > 0) {
					const account = response?.account || accounts[0];
					msalInstance.setActiveAccount(account);
					update(state => ({
						...state,
						isAuthenticated: true,
						user: accountToUser(account),
						isLoading: false
					}));
				} else {
					update(state => ({
						...state,
						isAuthenticated: false,
						user: null,
						isLoading: false
					}));
				}
			} catch (error) {
				console.error('Auth initialization error:', error);
				update(state => ({
					...state,
					error: error instanceof Error ? error.message : 'Authentication initialization failed',
					isLoading: false
				}));
			}
		})();
		return initPromise;
	}

	async function login() {
		if (!PUBLIC_AZURE_CLIENT_ID || !PUBLIC_AZURE_AUTHORITY) {
			console.error('Azure AD not configured. ClientId:', PUBLIC_AZURE_CLIENT_ID, 'Authority:', PUBLIC_AZURE_AUTHORITY);
			alert('Authentication is not configured.');
			return;
		}

		if (!msalInstance) {
			console.error('MSAL client not initialized');
			return;
		}

		try {
			await msalInstance.loginRedirect({
				scopes: loginScopes
			});
		} catch (error) {
			console.error('Login error:', error);
			update(state => ({
				...state,
				error: error instanceof Error ? error.message : 'Login failed'
			}));
		}
	}

	async function logout() {
		if (!msalInstance) {
			console.error('MSAL client not initialized');
			return;
		}

		try {
			update(state => ({
				...state,
				isAuthenticated: false,
				user: null
			}));

			await msalInstance.logoutRedirect({
				postLogoutRedirectUri: window.location.origin
			});
		} catch (error) {
			console.error('Logout error:', error);
			update(state => ({
				...state,
				error: error instanceof Error ? error.message : 'Logout failed'
			}));
		}
	}

	async function getAccessToken(): Promise<string | null> {
		if (!msalInstance) {
			console.error('MSAL client not initialized');
			return null;
		}

		const account = msalInstance.getActiveAccount() || msalInstance.getAllAccounts()[0];
		if (!account) {
			console.error('No active account');
			return null;
		}

		try {
			// First try without forceRefresh (uses cached token if still valid)
			const result = await msalInstance.acquireTokenSilent({
				scopes: loginScopes,
				account
			});
			// CIAM with OIDC scopes returns an opaque access token.
			// Use the ID token (a proper JWT) for backend verification.
			return result.idToken;
		} catch (error) {
			console.warn('Silent token acquisition failed, attempting refresh...', (error as any)?.errorCode);
			try {
				// Force a token refresh using the refresh token
				const result = await msalInstance.acquireTokenSilent({
					scopes: loginScopes,
					account,
					forceRefresh: true
				});
				return result.idToken;
			} catch (refreshError) {
				console.error('Token refresh failed, redirecting to login:', (refreshError as any)?.errorCode);
				try {
					await msalInstance.acquireTokenRedirect({
						scopes: loginScopes,
						account
					});
				} catch (redirectError) {
					console.error('Token redirect error:', redirectError);
				}
				return null;
			}
		}
	}

	async function checkAuth(): Promise<boolean> {
		if (!msalInstance) return false;
		return msalInstance.getAllAccounts().length > 0;
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

// Derived stores — same interface as before
export const isAuthenticated = derived(authStore, $auth => $auth.isAuthenticated);
export const currentUser = derived(authStore, $auth => $auth.user);
export const authLoading = derived(authStore, $auth => $auth.isLoading);
