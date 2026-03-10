import { writable, derived } from 'svelte/store';
import { browser } from '$app/environment';
import yaml from 'js-yaml';

export interface ExampleQuestion {
	id: string;
	title: string;
	question: string;
	description?: string;
}

export interface AppConfig {
	assistant: {
		name: string;
		logo: string;
	};
	welcome: {
		title: string;
		subtitle: string;
		disclaimer: string;
	};
	example_questions: ExampleQuestion[];
	search_messages: {
		thinking: string;
		writing: string;
		complete: string;
		documents_found: string;
	};
	source_types: Record<string, string>;
	ui: Record<string, string>;
	language: {
		default: string;
		available: string[];
	};
}

// Default config (loaded from YAML at build time or runtime)
const defaultConfig: AppConfig = {
	assistant: {
		name: 'Nora',
		logo: '/favicon.png'
	},
	welcome: {
		title: 'Wie kann ich Ihnen helfen?',
		subtitle: 'Stellen Sie mir eine Frage und ich durchsuche Ihre verbundenen Quellen nach umfassenden Antworten.',
		disclaimer: 'Nora durchsucht verbundene Quellen. Quellenangaben bei kritischen Entscheidungen prüfen.'
	},
	example_questions: [
		{ id: 'processes', title: 'Prozesse', question: 'Wie funktioniert unser Onboarding-Prozess?', description: 'Wie funktioniert unser Onboarding-Prozess?' },
		{ id: 'documentation', title: 'Dokumentation', question: 'Wo finde ich die Dokumentation zu unseren Produkten?', description: 'Wo finde ich die Produktdokumentation?' },
		{ id: 'policies', title: 'Richtlinien', question: 'Was sind die aktuellen Richtlinien für Homeoffice?', description: 'Was sind die Homeoffice-Richtlinien?' },
		{ id: 'contacts', title: 'Kontakte', question: 'Wer ist der Ansprechpartner für IT-Support?', description: 'Wer ist Ansprechpartner für IT-Support?' }
	],
	search_messages: {
		thinking: 'Nora denkt nach...',
		writing: 'Antwort wird erstellt...',
		complete: 'Suche abgeschlossen',
		documents_found: '{count} Dokument(e) gefunden'
	},
	source_types: {
		sharepoint: 'SharePoint',
		confluence: 'Confluence',
		wiki: 'Internes Wiki',
		jira: 'Jira',
		web: 'Web',
		elasticsearch: 'Wissensdatenbank',
		document: 'Dokument'
	},
	ui: {
		copy: 'Kopieren',
		regenerate: 'Neu generieren',
		share: 'Teilen',
		new_chat: 'Neuer Chat',
		your_chats: 'Ihre Chats',
		no_chats: 'Noch keine Unterhaltungen',
		no_chats_hint: 'Starten Sie eine neue Unterhaltung',
		continue_session: 'Letzte Sitzung fortsetzen',
		delete_confirm: 'Möchten Sie diese Sitzung wirklich löschen?',
		sources_title: 'Quellen',
		show_all: 'Alle anzeigen',
		show_less: 'Weniger anzeigen',
		today: 'Heute',
		yesterday: 'Gestern',
		last_week: 'Letzte 7 Tage',
		older: 'Älter'
	},
	language: {
		default: 'de',
		available: ['de', 'en']
	}
};

function createConfigStore() {
	const { subscribe, set, update } = writable<AppConfig>(defaultConfig);

	return {
		subscribe,

		async loadConfig() {
			// Only load config in browser (not during SSR)
			if (!browser) return;

			try {
				// Try to load custom config from /config/config.yaml
				const response = await fetch('/config/config.yaml');
				if (response.ok) {
					const yamlText = await response.text();
					const config = yaml.load(yamlText) as Partial<AppConfig>;
					update(current => mergeConfig(current, config));
					return;
				}
			} catch (error) {
				console.log('No custom config.yaml found, using defaults');
			}

			// Fallback: try API endpoint
			try {
				const response = await fetch('/api/config');
				if (response.ok) {
					const config = await response.json();
					update(current => mergeConfig(current, config));
				}
			} catch (error) {
				console.log('No API config found, using defaults');
			}
		},

		reset() {
			set(defaultConfig);
		}
	};
}

// Deep merge helper
function mergeConfig(base: AppConfig, override: Partial<AppConfig>): AppConfig {
	const result = { ...base };

	for (const key in override) {
		const k = key as keyof AppConfig;
		if (override[k] !== undefined) {
			if (typeof override[k] === 'object' && !Array.isArray(override[k])) {
				result[k] = { ...(base[k] as object), ...(override[k] as object) } as any;
			} else {
				result[k] = override[k] as any;
			}
		}
	}

	return result;
}

export const configStore = createConfigStore();

// Derived stores for convenience
export const exampleQuestions = derived(configStore, $config => $config.example_questions);
export const welcomeConfig = derived(configStore, $config => $config.welcome);
export const searchMessages = derived(configStore, $config => $config.search_messages);
export const sourceTypes = derived(configStore, $config => $config.source_types);
export const uiLabels = derived(configStore, $config => $config.ui);
export const assistantConfig = derived(configStore, $config => $config.assistant);
