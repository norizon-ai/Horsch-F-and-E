import type { Source } from '$lib/types';

export interface GroupedSource {
	id: string;
	title: string;
	url: string;
	sourceType?: Source['sourceType'];
	lastUpdated?: string;
	sections: SourceSection[];
	maxRelevance: number;
	sectionCount: number;
}

export interface SourceSection {
	id: string;
	snippet: string;
	relevance: number;
}

/**
 * Groups multiple source chunks from the same document together.
 * Sources are grouped by URL (or ID if no URL).
 * Within each group, sections are sorted by relevance.
 * Groups are sorted by max relevance across their sections.
 */
export function groupSourcesByUrl(sources: Source[]): GroupedSource[] {
	const grouped = new Map<string, GroupedSource>();

	sources.forEach((source) => {
		const key = source.url || source.id;

		if (!grouped.has(key)) {
			grouped.set(key, {
				id: source.id,
				title: source.title,
				url: source.url,
				sourceType: source.sourceType,
				lastUpdated: source.lastUpdated,
				sections: [],
				maxRelevance: 0,
				sectionCount: 0
			});
		}

		const group = grouped.get(key)!;
		group.sections.push({
			id: source.id,
			snippet: source.snippet,
			relevance: source.relevance || 0
		});
		group.maxRelevance = Math.max(group.maxRelevance, source.relevance || 0);
		group.sectionCount = group.sections.length;
	});

	// Sort sections by relevance within each group
	grouped.forEach((group) => {
		group.sections.sort((a, b) => b.relevance - a.relevance);
	});

	// Sort groups by max relevance
	return Array.from(grouped.values()).sort((a, b) => b.maxRelevance - a.maxRelevance);
}
