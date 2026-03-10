/**
 * Sanitize snippet HTML to only allow <em> tags from Elasticsearch highlighting.
 * This prevents XSS while enabling keyword highlighting.
 *
 * Process:
 * 1. Replace <em> and </em> with safe placeholders
 * 2. Escape all remaining HTML entities
 * 3. Restore <em> tags from placeholders
 */
export function sanitizeSnippet(snippet: string | undefined): string {
	if (!snippet) return '';

	// Use null bytes as placeholders (cannot appear in normal text)
	const placeholder_open = '\x00EM_OPEN\x00';
	const placeholder_close = '\x00EM_CLOSE\x00';

	let safe = snippet
		.replace(/<em>/gi, placeholder_open)
		.replace(/<\/em>/gi, placeholder_close);

	// Escape all remaining HTML
	safe = safe
		.replace(/&/g, '&amp;')
		.replace(/</g, '&lt;')
		.replace(/>/g, '&gt;')
		.replace(/"/g, '&quot;')
		.replace(/'/g, '&#039;');

	// Restore <em> tags
	safe = safe
		.replace(new RegExp(placeholder_open, 'g'), '<em>')
		.replace(new RegExp(placeholder_close, 'g'), '</em>');

	return safe;
}
