<script lang="ts">
	import { t } from 'svelte-i18n';
	import type { PostAction, Protocol } from '$lib/types';

	let {
		action = null,
		protocol = null,
		onComplete,
		onBack
	}: {
		action?: PostAction | null;
		protocol?: Protocol | null;
		onComplete?: () => void;
		onBack?: () => void;
	} = $props();

	// Generate pre-filled prompt based on action and protocol
	function getPromptTemplate(): string {
		if (!protocol || !action) return '';

		const attendeeList = protocol.attendees.join(', ');
		const actionItemsList = protocol.actionItems
			.map((item, i) => `${i + 1}. ${item.text}${item.assignee ? ` (@${item.assignee})` : ''}${item.dueDate ? ` - Fällig: ${item.dueDate}` : ''}`)
			.join('\n');

		switch (action) {
			case 'email':
				return `Betreff: Protokoll - ${protocol.title}

Hallo zusammen,

anbei das Protokoll unseres Meetings vom ${protocol.date}.

Zusammenfassung:
${protocol.executiveSummary}

Offene Aufgaben:
${actionItemsList}

Das vollständige Protokoll finden Sie im Confluence: [Link einfügen]

Bei Fragen stehe ich gerne zur Verfügung.

Beste Grüße`;

			case 'meeting':
				return `Betreff: Folgetermin - ${protocol.title}

Einladung zum Folgemeeting

Teilnehmer: ${attendeeList}

Agenda:
1. Review der offenen Aufgaben
${protocol.actionItems.map((item, i) => `   ${i + 1}. ${item.text}`).join('\n')}

2. Nächste Schritte besprechen

Vorgeschlagene Termine:
- [Termin 1]
- [Termin 2]

Bitte um Rückmeldung bis [Datum].`;

			case 'status': {
				const completedCount = protocol.actionItems.filter(i => i.completed).length;
				const totalCount = protocol.actionItems.length;

				return `Status-Update: ${protocol.title}

Meeting vom: ${protocol.date}
Teilnehmer: ${attendeeList}

Fortschritt: ${completedCount}/${totalCount} Aufgaben erledigt

Aktuelle Aufgaben:
${protocol.actionItems
	.filter(i => !i.completed)
	.map(item => `- [ ] ${item.text}${item.assignee ? ` (@${item.assignee})` : ''}`)
	.join('\n')}

Nächste Schritte:
${protocol.nextSteps?.map(step => `- ${step}`).join('\n') || '- [Zu definieren]'}`;
			}

			case 'chat':
				return `Basierend auf dem Meeting "${protocol.title}" vom ${protocol.date}:

${protocol.executiveSummary}

Wie kann ich Ihnen bei den nächsten Schritten helfen?`;

			default:
				return '';
		}
	}

	let promptText = $state(getPromptTemplate());

	// Update prompt when action or protocol changes
	$effect(() => {
		if (action && protocol) {
			promptText = getPromptTemplate();
		}
	});

	function getActionInfo(): { title: string; icon: string; buttonLabel: string } {
		switch (action) {
			case 'email':
				return {
					title: $t('workflow.meeting.followUp.email.title'),
					icon: 'mail',
					buttonLabel: $t('workflow.meeting.followUp.email.button')
				};
			case 'meeting':
				return {
					title: $t('workflow.meeting.followUp.meeting.title'),
					icon: 'calendar',
					buttonLabel: $t('workflow.meeting.followUp.meeting.button')
				};
			case 'status':
				return {
					title: $t('workflow.meeting.followUp.status.title'),
					icon: 'bell',
					buttonLabel: $t('workflow.meeting.followUp.status.button')
				};
			case 'chat':
				return {
					title: $t('workflow.meeting.followUp.chat.title'),
					icon: 'message',
					buttonLabel: $t('workflow.meeting.followUp.chat.button')
				};
			default:
				return {
					title: '',
					icon: 'file',
					buttonLabel: ''
				};
		}
	}

	let actionInfo = $derived(getActionInfo());

	function handleSubmit() {
		// In a real implementation, this would:
		// - For email: open email client or send via API
		// - For meeting: create calendar event
		// - For status: post to Slack/Teams
		// - For chat: redirect to chat with pre-filled message

		console.log('Submitting follow-up:', { action, promptText });
		onComplete?.();
	}

	function copyToClipboard() {
		navigator.clipboard.writeText(promptText);
	}
</script>

<div class="follow-up-editor">
	<div class="header">
		<button class="back-btn" on:click={() => onBack?.()}>
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<line x1="19" y1="12" x2="5" y2="12" />
				<polyline points="12 19 5 12 12 5" />
			</svg>
		</button>
		<div class="header-content">
			<div class="action-icon">
				{#if actionInfo.icon === 'mail'}
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" />
						<polyline points="22,6 12,13 2,6" />
					</svg>
				{:else if actionInfo.icon === 'calendar'}
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<rect x="3" y="4" width="18" height="18" rx="2" ry="2" />
						<line x1="16" y1="2" x2="16" y2="6" />
						<line x1="8" y1="2" x2="8" y2="6" />
						<line x1="3" y1="10" x2="21" y2="10" />
					</svg>
				{:else if actionInfo.icon === 'bell'}
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9" />
						<path d="M13.73 21a2 2 0 0 1-3.46 0" />
					</svg>
				{:else if actionInfo.icon === 'message'}
					<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
						<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" />
					</svg>
				{/if}
			</div>
			<h2>{actionInfo.title}</h2>
		</div>
	</div>

	<p class="subtitle">{$t('workflow.meeting.followUp.subtitle')}</p>

	<div class="editor-container">
		<div class="editor-toolbar">
			<span class="toolbar-label">{$t('workflow.meeting.followUp.preview')}</span>
			<button class="copy-btn" on:click={copyToClipboard}>
				<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
					<rect x="9" y="9" width="13" height="13" rx="2" ry="2" />
					<path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1" />
				</svg>
				{$t('common.copy')}
			</button>
		</div>
		<textarea
			bind:value={promptText}
			rows="16"
			placeholder={$t('workflow.meeting.followUp.placeholder')}
		></textarea>
	</div>

	<div class="actions">
		<button class="btn-secondary" on:click={() => onBack?.()}>
			{$t('common.cancel')}
		</button>
		<button class="btn-primary" on:click={handleSubmit}>
			{actionInfo.buttonLabel}
			<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
				<line x1="22" y1="2" x2="11" y2="13" />
				<polygon points="22 2 15 22 11 13 2 9 22 2" />
			</svg>
		</button>
	</div>
</div>

<style>
	.follow-up-editor {
		width: 100%;
		max-width: 800px;
	}

	.header {
		display: flex;
		align-items: center;
		gap: 16px;
		margin-bottom: 8px;
	}

	.back-btn {
		width: 44px;
		height: 44px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: transparent;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 8px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.back-btn:hover {
		background: var(--slate-50, #f8fafc);
		border-color: var(--slate-300, #cbd5e1);
	}

	.back-btn svg {
		width: 20px;
		height: 20px;
		color: var(--slate-600, #475569);
	}

	.header-content {
		display: flex;
		align-items: center;
		gap: 12px;
	}

	.action-icon {
		width: 44px;
		height: 44px;
		background: var(--blue-100, #dbeafe);
		border-radius: 10px;
		display: flex;
		align-items: center;
		justify-content: center;
	}

	.action-icon svg {
		width: 22px;
		height: 22px;
		color: var(--blue-600, #2563eb);
	}

	h2 {
		font-size: 20px;
		font-weight: 700;
		color: var(--slate-900, #0f172a);
	}

	.subtitle {
		font-size: 15px;
		color: var(--slate-600, #475569);
		margin-bottom: 24px;
		margin-left: 56px;
	}

	.editor-container {
		background: white;
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		overflow: hidden;
		margin-bottom: 24px;
		box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
	}

	.editor-toolbar {
		display: flex;
		justify-content: space-between;
		align-items: center;
		padding: 12px 16px;
		background: var(--slate-50, #f8fafc);
		border-bottom: 1px solid var(--slate-200, #e2e8f0);
	}

	.toolbar-label {
		font-size: 12px;
		font-weight: 600;
		color: var(--slate-500, #64748b);
		text-transform: uppercase;
		letter-spacing: 0.5px;
	}

	.copy-btn {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 6px 12px;
		background: white;
		border: 1px solid var(--slate-300, #cbd5e1);
		border-radius: 6px;
		font-size: 13px;
		font-weight: 500;
		color: var(--slate-700, #334155);
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.copy-btn:hover {
		background: var(--slate-50, #f8fafc);
		border-color: var(--slate-400, #94a3b8);
	}

	.copy-btn svg {
		width: 14px;
		height: 14px;
	}

	textarea {
		width: 100%;
		padding: 16px;
		border: none;
		font-size: 14px;
		font-family: 'Menlo', 'Monaco', 'Courier New', monospace;
		line-height: 1.6;
		color: var(--slate-700, #334155);
		resize: vertical;
		min-height: 300px;
	}

	textarea:focus {
		outline: none;
	}

	textarea::placeholder {
		color: var(--slate-400, #94a3b8);
	}

	.actions {
		display: flex;
		gap: 12px;
	}

	.btn-primary,
	.btn-secondary {
		display: flex;
		align-items: center;
		justify-content: center;
		gap: 8px;
		padding: 12px 24px;
		font-size: 15px;
		font-weight: 600;
		border-radius: 6px;
		cursor: pointer;
		transition: all 0.15s ease;
	}

	.btn-primary {
		flex: 1;
		background: var(--blue-500, #3b82f6);
		color: white;
		border: none;
		box-shadow: 0 1px 2px rgba(15, 23, 42, 0.05);
	}

	.btn-primary:hover {
		background: var(--blue-600, #2563eb);
		box-shadow: 0 4px 12px rgba(15, 23, 42, 0.08);
	}

	.btn-primary svg {
		width: 18px;
		height: 18px;
	}

	.btn-secondary {
		background: white;
		color: var(--slate-700, #334155);
		border: 1px solid var(--slate-300, #cbd5e1);
	}

	.btn-secondary:hover {
		background: var(--slate-50, #f8fafc);
		border-color: var(--slate-400, #94a3b8);
	}

	@media (max-width: 480px) {
		.header {
			flex-direction: column;
			align-items: flex-start;
		}

		.subtitle {
			margin-left: 0;
		}

		.actions {
			flex-direction: column-reverse;
		}
	}
</style>
