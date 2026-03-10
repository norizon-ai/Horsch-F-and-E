/**
 * Workflow route authentication guard
 */

import { requireAuth } from '$lib/utils/authGuard';
import { browser } from '$app/environment';

export const load = async () => {
	if (browser) {
		await requireAuth();
	}
};
