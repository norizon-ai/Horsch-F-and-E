<script lang="ts">
	import { t } from "svelte-i18n";
	import type { ChatContext, ChatContextAction } from "$lib/types";
	import { Badge } from "$lib/components/ui/badge";
	import { Button } from "$lib/components/ui/button";
	import { Card, CardContent } from "$lib/components/ui/card";
	import { Separator } from "$lib/components/ui/separator";

	let {
		context,
		onDismiss = undefined as (() => void) | undefined,
		onSelectPrompt = undefined as ((prompt: string) => void) | undefined,
		ondismiss = undefined as (() => void) | undefined,
		onselectPrompt = undefined as ((prompt: string) => void) | undefined,
	}: {
		context: ChatContext;
		onDismiss?: (() => void) | undefined;
		onSelectPrompt?: ((prompt: string) => void) | undefined;
		ondismiss?: (() => void) | undefined;
		onselectPrompt?: ((prompt: string) => void) | undefined;
	} = $props();

	let expanded = $state(false);

	function getSuggestedPrompts(
		action: ChatContextAction,
	): Array<{ label: string; prompt: string }> {
		const prompts: Record<
			ChatContextAction,
			Array<{ label: string; prompt: string }>
		> = {
			email: [
				{
					label: "Follow-up email",
					prompt: "Write a follow-up email summarizing the key action items from this meeting for the attendees.",
				},
				{
					label: "Summary for stakeholders",
					prompt: "Draft a brief email summary of this meeting for stakeholders who were not present.",
				},
			],
			status: [
				{
					label: "Slack update",
					prompt: "Create a concise Slack status update about this meeting highlighting the main decisions and next steps.",
				},
				{
					label: "Team announcement",
					prompt: "Write a brief team announcement summarizing the key outcomes of this meeting.",
				},
			],
			chat: [
				{
					label: "Key decisions",
					prompt: "What were the main decisions made in this meeting?",
				},
				{
					label: "Action items",
					prompt: "List all action items from this meeting with their assigned owners and due dates.",
				},
			],
			meeting: [
				{
					label: "Follow-up needed",
					prompt: "What follow-up meetings are needed based on the discussions in this meeting?",
				},
				{
					label: "Agenda for next meeting",
					prompt: "Based on this meeting, suggest an agenda for the next follow-up meeting.",
				},
			],
		};
		return prompts[action] || prompts.chat;
	}

	let suggestedPrompts = $derived(getSuggestedPrompts(context.action));
	let actionItemCount = $derived(context.protocol?.actionItems?.length || 0);
	let truncatedSummary = $derived((() => {
		if (context.protocol?.executiveSummary) {
			return (
				context.protocol.executiveSummary.slice(0, 150) +
				(context.protocol.executiveSummary.length > 150 ? "..." : "")
			);
		}
		return "";
	})());
</script>

<Card
	class="mb-5 bg-gradient-to-br from-blue-50 to-orange-50 border-blue-200"
>
	<CardContent class="p-4">
		<!-- Header -->
		<div class="flex items-center justify-between gap-3">
			<div class="flex items-center gap-3 flex-1 min-w-0">
				<div
					class="w-9 h-9 bg-blue-100 rounded-lg flex items-center justify-center shrink-0"
				>
					<svg
						class="w-5 h-5 text-blue-600"
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<path
							d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"
						/>
						<polyline points="14,2 14,8 20,8" />
						<line x1="16" y1="13" x2="8" y2="13" />
						<line x1="16" y1="17" x2="8" y2="17" />
						<polyline points="10,9 9,9 8,9" />
					</svg>
				</div>
				<div class="flex flex-col min-w-0">
					<span class="text-[11px] font-medium text-blue-600 uppercase tracking-wide"
						>{$t("chat.context.loaded")}</span
					>
					<span class="text-sm font-semibold text-slate-900 truncate"
						>{context.protocol?.title || "Meeting Protocol"}</span
					>
				</div>
			</div>
			<div class="flex items-center gap-1 shrink-0">
				<Button
					variant="ghost"
					size="icon"
					class="h-7 w-7 text-slate-500 hover:bg-white hover:text-slate-700 [&_svg]:size-4"
					onclick={() => (expanded = !expanded)}
					aria-expanded={expanded}
				>
					<svg
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
						class="transition-transform duration-200 {expanded ? 'rotate-180' : ''}"
					>
						<polyline points="6,9 12,15 18,9" />
					</svg>
				</Button>
				<Button
					variant="ghost"
					size="icon"
					class="h-7 w-7 text-slate-500 hover:bg-white hover:text-slate-700 [&_svg]:size-4"
					onclick={() => { onDismiss?.(); ondismiss?.(); }}
					aria-label="Dismiss"
				>
					<svg
						viewBox="0 0 24 24"
						fill="none"
						stroke="currentColor"
						stroke-width="2"
					>
						<line x1="18" y1="6" x2="6" y2="18" />
						<line x1="6" y1="6" x2="18" y2="18" />
					</svg>
				</Button>
			</div>
		</div>

		<!-- Expanded details -->
		{#if expanded && context.protocol}
			<Separator class="my-3 bg-blue-200" />
			<div class="mb-2">
				<span
					class="block text-[11px] font-medium text-slate-500 uppercase tracking-wide mb-1"
					>{$t("chat.context.summary")}</span
				>
				<p class="text-[13px] text-slate-700 leading-normal m-0">
					{truncatedSummary}
				</p>
			</div>
			{#if actionItemCount > 0}
				<div class="flex gap-2 flex-wrap">
					<Badge
						variant="outline"
						class="text-xs text-slate-600 bg-white rounded-full border-slate-200 px-2.5 py-1"
						>{actionItemCount}
						{$t("chat.context.actionItems")}</Badge
					>
					{#if context.protocol.attendees?.length > 0}
						<Badge
							variant="outline"
							class="text-xs text-slate-600 bg-white rounded-full border-slate-200 px-2.5 py-1"
							>{context.protocol.attendees.length} attendees</Badge
						>
					{/if}
				</div>
			{/if}
		{/if}

		<!-- Suggested prompts -->
		<Separator class="my-3 bg-blue-200" />
		<div>
			<span class="block text-xs text-slate-500 mb-2"
				>{$t("chat.context.tryAsking")}</span
			>
			<div class="flex gap-2 flex-wrap">
				{#each suggestedPrompts as { label, prompt }}
					<Button
						variant="outline"
						size="sm"
						class="rounded-full text-[13px] text-blue-700 bg-white border-blue-200 hover:bg-blue-50 hover:border-blue-300"
						onclick={() => { onSelectPrompt?.(prompt); onselectPrompt?.(prompt); }}
					>
						{label}
					</Button>
				{/each}
			</div>
		</div>
	</CardContent>
</Card>
