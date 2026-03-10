<script lang="ts">
	import { t } from "svelte-i18n";
	import { workflowStore } from "$lib/stores/workflowStore";
	import type { Protocol, ActionItem, CustomSection } from "$lib/types";

	export let protocol: Protocol | null = null;
	export let editable = true;

	// Format date for display
	function formatDate(dateStr: string): string {
		if (!dateStr) return "";
		try {
			const date = new Date(dateStr);
			return date.toLocaleDateString("en-US", {
				weekday: "long",
				year: "numeric",
				month: "long",
				day: "numeric",
			});
		} catch {
			return dateStr;
		}
	}

	// Save changes to store
	function saveToStore() {
		if (protocol) {
			workflowStore.setProtocol(protocol);
		}
	}

	// Title change
	function handleTitleChange(e: Event) {
		if (!protocol) return;
		protocol.title = (e.target as HTMLInputElement).value;
		saveToStore();
	}

	// Date change
	function handleDateChange(e: Event) {
		if (!protocol) return;
		protocol.date = (e.target as HTMLInputElement).value;
		saveToStore();
	}

	// Summary change
	function handleSummaryChange(e: Event) {
		if (!protocol) return;
		protocol.executiveSummary = (e.target as HTMLTextAreaElement).value;
		saveToStore();
	}

	// Attendee management
	function updateAttendee(index: number, value: string) {
		if (!protocol) return;
		protocol.attendees[index] = value;
		protocol.attendees = [...protocol.attendees]; // trigger reactivity
		saveToStore();
	}

	function removeAttendee(index: number) {
		if (!protocol) return;
		protocol.attendees = protocol.attendees.filter((_, i) => i !== index);
		saveToStore();
	}

	function addAttendee() {
		if (!protocol) return;
		protocol.attendees = [...protocol.attendees, ""];
		setTimeout(() => {
			const inputs = document.querySelectorAll(".attendee-input");
			const lastInput = inputs[inputs.length - 1] as HTMLInputElement;
			if (lastInput) lastInput.focus();
		}, 0);
	}

	function handleAttendeeKeydown(e: KeyboardEvent, index: number) {
		if (e.key === "Backspace" && protocol?.attendees[index] === "") {
			e.preventDefault();
			removeAttendee(index);
		} else if (e.key === "Enter") {
			e.preventDefault();
			addAttendee();
		}
	}

	function handleAttendeeBlur(e: Event, index: number) {
		updateAttendee(index, (e.target as HTMLInputElement).value);
	}

	// Action item management
	function toggleActionItem(index: number) {
		if (!protocol || !protocol.actionItems[index]) return;
		protocol.actionItems[index].completed =
			!protocol.actionItems[index].completed;
		protocol.actionItems = [...protocol.actionItems];
		saveToStore();
	}

	function updateActionItemText(index: number, value: string) {
		if (!protocol) return;
		protocol.actionItems[index].text = value;
		protocol.actionItems = [...protocol.actionItems];
		saveToStore();
	}

	function updateActionItemAssignee(index: number, value: string) {
		if (!protocol) return;
		protocol.actionItems[index].assignee = value;
		protocol.actionItems = [...protocol.actionItems];
		saveToStore();
	}

	function updateActionItemDueDate(index: number, value: string) {
		if (!protocol) return;
		protocol.actionItems[index].dueDate = value;
		protocol.actionItems = [...protocol.actionItems];
		saveToStore();
	}

	function handleActionItemTextBlur(e: Event, index: number) {
		updateActionItemText(index, (e.target as HTMLInputElement).value);
	}

	function handleActionItemAssigneeBlur(e: Event, index: number) {
		updateActionItemAssignee(index, (e.target as HTMLInputElement).value);
	}

	function handleActionItemDueDateBlur(e: Event, index: number) {
		updateActionItemDueDate(index, (e.target as HTMLInputElement).value);
	}

	function addActionItem() {
		if (!protocol) return;
		protocol.actionItems = [
			...protocol.actionItems,
			{
				id: `action-${Date.now()}`,
				text: "",
				completed: false,
			},
		];
		setTimeout(() => {
			const inputs = document.querySelectorAll(".action-text-input");
			const lastInput = inputs[inputs.length - 1] as HTMLInputElement;
			if (lastInput) lastInput.focus();
		}, 0);
	}

	function removeActionItem(index: number) {
		if (!protocol) return;
		protocol.actionItems = protocol.actionItems.filter(
			(_, i) => i !== index,
		);
		saveToStore();
	}

	// Decisions management
	function updateDecision(index: number, value: string) {
		if (!protocol || !protocol.decisions) return;
		protocol.decisions[index] = value;
		protocol.decisions = [...protocol.decisions];
		saveToStore();
	}

	function removeDecision(index: number) {
		if (!protocol || !protocol.decisions) return;
		protocol.decisions = protocol.decisions.filter((_, i) => i !== index);
		saveToStore();
	}

	function addDecision() {
		if (!protocol) return;
		protocol.decisions = [...(protocol.decisions || []), ""];
		setTimeout(() => {
			const inputs = document.querySelectorAll(".decision-input");
			const lastInput = inputs[inputs.length - 1] as HTMLInputElement;
			if (lastInput) lastInput.focus();
		}, 0);
	}

	function handleDecisionKeydown(e: KeyboardEvent, index: number) {
		if (e.key === "Backspace" && protocol?.decisions?.[index] === "") {
			e.preventDefault();
			removeDecision(index);
		} else if (e.key === "Enter") {
			e.preventDefault();
			addDecision();
		}
	}

	function handleDecisionBlur(e: Event, index: number) {
		updateDecision(index, (e.target as HTMLInputElement).value);
	}

	// Next Steps management
	function updateNextStep(index: number, value: string) {
		if (!protocol || !protocol.nextSteps) return;
		protocol.nextSteps[index] = value;
		protocol.nextSteps = [...protocol.nextSteps];
		saveToStore();
	}

	function removeNextStep(index: number) {
		if (!protocol || !protocol.nextSteps) return;
		protocol.nextSteps = protocol.nextSteps.filter((_, i) => i !== index);
		saveToStore();
	}

	function addNextStep() {
		if (!protocol) return;
		protocol.nextSteps = [...(protocol.nextSteps || []), ""];
		setTimeout(() => {
			const inputs = document.querySelectorAll(".next-step-input");
			const lastInput = inputs[inputs.length - 1] as HTMLInputElement;
			if (lastInput) lastInput.focus();
		}, 0);
	}

	function handleNextStepKeydown(e: KeyboardEvent, index: number) {
		if (e.key === "Backspace" && protocol?.nextSteps?.[index] === "") {
			e.preventDefault();
			removeNextStep(index);
		} else if (e.key === "Enter") {
			e.preventDefault();
			addNextStep();
		}
	}

	function handleNextStepBlur(e: Event, index: number) {
		updateNextStep(index, (e.target as HTMLInputElement).value);
	}

	// Custom sections management
	function updateCustomSectionText(sectionIndex: number, value: string) {
		if (!protocol || !protocol.customSections) return;
		protocol.customSections[sectionIndex].content = value;
		protocol.customSections = [...protocol.customSections];
		saveToStore();
	}

	function updateCustomSectionListItem(
		sectionIndex: number,
		itemIndex: number,
		value: string,
	) {
		if (!protocol || !protocol.customSections) return;
		const section = protocol.customSections[sectionIndex];
		if (section.type !== "list" || !Array.isArray(section.content)) return;
		section.content[itemIndex] = value;
		protocol.customSections = [...protocol.customSections];
		saveToStore();
	}

	function addCustomSectionListItem(sectionIndex: number) {
		if (!protocol || !protocol.customSections) return;
		const section = protocol.customSections[sectionIndex];
		if (section.type !== "list" || !Array.isArray(section.content)) return;
		section.content = [...(section.content as string[]), ""];
		protocol.customSections = [...protocol.customSections];
		setTimeout(() => {
			const inputs = document.querySelectorAll(
				`.custom-section-${sectionIndex} .custom-list-input`,
			);
			const lastInput = inputs[inputs.length - 1] as HTMLInputElement;
			if (lastInput) lastInput.focus();
		}, 0);
	}

	function removeCustomSectionListItem(
		sectionIndex: number,
		itemIndex: number,
	) {
		if (!protocol || !protocol.customSections) return;
		const section = protocol.customSections[sectionIndex];
		if (section.type !== "list" || !Array.isArray(section.content)) return;
		section.content = (section.content as string[]).filter(
			(_, i) => i !== itemIndex,
		);
		protocol.customSections = [...protocol.customSections];
		saveToStore();
	}

	function handleCustomSectionKeydown(
		e: KeyboardEvent,
		sectionIndex: number,
		itemIndex: number,
	) {
		if (!protocol || !protocol.customSections) return;
		const section = protocol.customSections[sectionIndex];
		if (section.type !== "list" || !Array.isArray(section.content)) return;

		if (e.key === "Backspace" && section.content[itemIndex] === "") {
			e.preventDefault();
			removeCustomSectionListItem(sectionIndex, itemIndex);
		} else if (e.key === "Enter") {
			e.preventDefault();
			addCustomSectionListItem(sectionIndex);
		}
	}

	function handleCustomSectionTextBlur(e: Event, sectionIndex: number) {
		updateCustomSectionText(
			sectionIndex,
			(e.target as HTMLTextAreaElement).value,
		);
	}

	function handleCustomSectionListBlur(
		e: Event,
		sectionIndex: number,
		itemIndex: number,
	) {
		updateCustomSectionListItem(
			sectionIndex,
			itemIndex,
			(e.target as HTMLInputElement).value,
		);
	}

	// Transcript
	let isEditingTranscript = false;

	function handleTranscriptChange(e: Event) {
		if (!protocol) return;
		protocol.fullTranscript = (e.target as HTMLTextAreaElement).value;
		saveToStore();
	}

	// Auto-grow textarea
	function autoGrow(e: Event) {
		const el = e.target as HTMLTextAreaElement;
		el.style.height = "auto";
		el.style.height = el.scrollHeight + "px";
	}

	// Hover edit state
	let hoveredSectionId: string | null = null;
	let editingSectionId: string | null = null;

	function handleSectionHover(sectionId: string | null) {
		if (!editable) return;
		hoveredSectionId = sectionId;
	}

	function handleSectionEdit(sectionId: string) {
		if (!editable) return;
		editingSectionId = sectionId;
	}

	function handleSectionSave(sectionId: string) {
		editingSectionId = null;
		saveToStore();
	}

	function handleSectionCancel() {
		editingSectionId = null;
	}
</script>

<div class="preview-sidebar">
	{#if protocol}
		<div class="sidebar-content">
			<!-- Page Header -->
			<div class="page-header">
				<div class="header-main">
					<div class="icon-stack">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
							class="confluence-icon"
						>
							<path
								d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"
							/>
							<polyline points="7.5 4.21 12 6.81 16.5 4.21" />
							<polyline points="7.5 19.79 7.5 14.63 12 12.01" />
							<polyline points="16.5 19.79 16.5 14.63 12 12.01" />
							<line x1="12" y1="2.19" x2="12" y2="6.81" />
							<line x1="12" y1="12.01" x2="12" y2="21.81" />
						</svg>
					</div>
					<div class="title-area">
						<span class="context-path">Norizon / Engineering</span>
						{#if editable}
							<input
								type="text"
								class="page-title-input"
								value={protocol.title || ""}
								on:blur={handleTitleChange}
								on:change={handleTitleChange}
								placeholder="Meeting title..."
							/>
						{:else}
							<h1 class="page-title">{protocol.title}</h1>
						{/if}
					</div>
				</div>
			</div>

			<!-- Metadata Section -->
			<div class="metadata-grid">
				<div class="metadata-row">
					<label class="metadata-label"
						>{$t("workflow.meeting.protocol.date")}</label
					>
					{#if editable}
						<input
							type="date"
							class="metadata-date-input"
							value={protocol.date || ""}
							on:blur={handleDateChange}
							on:change={handleDateChange}
						/>
					{:else}
						<div class="metadata-value">
							{formatDate(protocol.date)}
						</div>
					{/if}
				</div>

				<div class="metadata-row attendees-row">
					<label class="metadata-label"
						>{$t("workflow.meeting.protocol.attendees")}</label
					>
					<div class="attendees-container">
						{#if editable}
							{#each protocol.attendees as attendee, idx}
								<span class="attendee-chip">
									<input
										type="text"
										class="attendee-input"
										value={attendee}
										on:blur={(e) =>
											handleAttendeeBlur(e, idx)}
										on:keydown={(e) =>
											handleAttendeeKeydown(e, idx)}
										placeholder="Name..."
									/>
									<button
										class="chip-remove"
										on:click={() => removeAttendee(idx)}
										title="Remove"
									>
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<line
												x1="18"
												y1="6"
												x2="6"
												y2="18"
											/>
											<line
												x1="6"
												y1="6"
												x2="18"
												y2="18"
											/>
										</svg>
									</button>
								</span>
							{/each}
							<button class="add-chip" on:click={addAttendee}>
								<svg
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<line x1="12" y1="5" x2="12" y2="19" />
									<line x1="5" y1="12" x2="19" y2="12" />
								</svg>
								Add
							</button>
						{:else}
							<div class="attendee-list">
								{protocol.attendees.join(", ")}
							</div>
						{/if}
					</div>
				</div>
			</div>

			<!-- Executive Summary -->
			<section class="content-section">
				<div class="section-header-row">
					<h2 class="section-heading">
						{$t("workflow.meeting.protocol.summary")}
					</h2>
					<span class="ai-badge" title="AI-generated content">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<circle cx="12" cy="12" r="10" />
							<line x1="12" y1="16" x2="12" y2="12" />
							<line x1="12" y1="8" x2="12.01" y2="8" />
						</svg>
						AI
					</span>
				</div>
				{#if editable}
					<textarea
						class="summary-textarea"
						value={protocol.executiveSummary || ""}
						on:input={autoGrow}
						on:blur={handleSummaryChange}
						placeholder="Summarize the key points..."
					></textarea>
				{:else}
					<p class="summary-text">
						{protocol.executiveSummary ||
							"No summary available for this meeting."}
					</p>
				{/if}
			</section>

			<!-- Action Items -->
			<section class="content-section">
				<div class="section-header-row">
					<h2 class="section-heading">
						{$t("workflow.meeting.protocol.actionItems")}
					</h2>
					<span class="ai-badge" title="AI-generated content">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<circle cx="12" cy="12" r="10" />
							<line x1="12" y1="16" x2="12" y2="12" />
							<line x1="12" y1="8" x2="12.01" y2="8" />
						</svg>
						AI
					</span>
					{#if editable}
						<button class="add-action-btn" on:click={addActionItem}>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<line x1="12" y1="5" x2="12" y2="19" />
								<line x1="5" y1="12" x2="19" y2="12" />
							</svg>
							Add task
						</button>
					{/if}
				</div>
				{#if protocol.actionItems && protocol.actionItems.length > 0}
					<div class="task-list">
						{#each protocol.actionItems as item, idx}
							<div
								class="task-item"
								class:completed={item.completed}
							>
								<button
									class="task-checkbox"
									on:click={() => toggleActionItem(idx)}
								>
									{#if item.completed}
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="3"
										>
											<polyline points="20 6 9 17 4 12" />
										</svg>
									{/if}
								</button>
								<div class="task-content">
									{#if editable}
										<input
											type="text"
											class="action-text-input"
											value={item.text || ""}
											on:blur={(e) =>
												handleActionItemTextBlur(
													e,
													idx,
												)}
											placeholder="Describe task..."
										/>
										<div class="task-meta-edit">
											<div class="meta-field">
												<svg
													viewBox="0 0 24 24"
													fill="none"
													stroke="currentColor"
													stroke-width="2"
												>
													<path
														d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"
													/>
													<circle
														cx="12"
														cy="7"
														r="4"
													/>
												</svg>
												<input
													type="text"
													class="meta-input"
													value={item.assignee || ""}
													on:blur={(e) =>
														handleActionItemAssigneeBlur(
															e,
															idx,
														)}
													placeholder="Assignee"
												/>
											</div>
											<div class="meta-field">
												<svg
													viewBox="0 0 24 24"
													fill="none"
													stroke="currentColor"
													stroke-width="2"
												>
													<rect
														x="3"
														y="4"
														width="18"
														height="18"
														rx="2"
														ry="2"
													/>
													<line
														x1="16"
														y1="2"
														x2="16"
														y2="6"
													/>
													<line
														x1="8"
														y1="2"
														x2="8"
														y2="6"
													/>
													<line
														x1="3"
														y1="10"
														x2="21"
														y2="10"
													/>
												</svg>
												<input
													type="date"
													class="meta-input"
													value={item.dueDate || ""}
													on:blur={(e) =>
														handleActionItemDueDateBlur(
															e,
															idx,
														)}
												/>
											</div>
										</div>
									{:else}
										<span
											class="task-text"
											class:strikethrough={item.completed}
											>{item.text ||
												"No description"}</span
										>
										{#if item.assignee || item.dueDate}
											<div class="task-meta">
												{#if item.assignee}
													<span class="assignee-tag"
														>@{item.assignee}</span
													>
												{/if}
												{#if item.dueDate}
													<span class="due-date">
														<svg
															viewBox="0 0 24 24"
															fill="none"
															stroke="currentColor"
															stroke-width="1.5"
														>
															<rect
																x="3"
																y="4"
																width="18"
																height="18"
																rx="2"
																ry="2"
															/>
															<line
																x1="16"
																y1="2"
																x2="16"
																y2="6"
															/>
															<line
																x1="8"
																y1="2"
																x2="8"
																y2="6"
															/>
															<line
																x1="3"
																y1="10"
																x2="21"
																y2="10"
															/>
														</svg>
														{item.dueDate}
													</span>
												{/if}
											</div>
										{/if}
									{/if}
								</div>
								{#if editable}
									<button
										class="remove-btn"
										on:click={() => removeActionItem(idx)}
										title="Remove"
									>
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<line
												x1="18"
												y1="6"
												x2="6"
												y2="18"
											/>
											<line
												x1="6"
												y1="6"
												x2="18"
												y2="18"
											/>
										</svg>
									</button>
								{/if}
							</div>
						{/each}
					</div>
				{:else if editable}
					<div class="empty-actions">
						<p>No action items yet</p>
						<button
							class="add-first-action"
							on:click={addActionItem}
						>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<line x1="12" y1="5" x2="12" y2="19" />
								<line x1="5" y1="12" x2="19" y2="12" />
							</svg>
							Add your first action item
						</button>
					</div>
				{:else}
					<p class="empty-section">No action items</p>
				{/if}
			</section>

			<!-- Decisions -->
			<section class="content-section">
				<div class="section-header-row">
					<h2 class="section-heading">
						{$t("workflow.meeting.protocol.decisions") ||
							"Decisions"}
					</h2>
					<span class="ai-badge" title="AI-generated content">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<circle cx="12" cy="12" r="10" />
							<line x1="12" y1="16" x2="12" y2="12" />
							<line x1="12" y1="8" x2="12.01" y2="8" />
						</svg>
						AI
					</span>
					{#if editable}
						<button class="add-action-btn" on:click={addDecision}>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<line x1="12" y1="5" x2="12" y2="19" />
								<line x1="5" y1="12" x2="19" y2="12" />
							</svg>
							Add
						</button>
					{/if}
				</div>
				{#if protocol.decisions && protocol.decisions.length > 0}
					<ul class="bullet-list">
						{#each protocol.decisions as decision, idx}
							<li class="bullet-item">
								{#if editable}
									<input
										type="text"
										class="decision-input bullet-input"
										value={decision}
										on:blur={(e) =>
											handleDecisionBlur(e, idx)}
										on:keydown={(e) =>
											handleDecisionKeydown(e, idx)}
										placeholder="Decision..."
									/>
									<button
										class="remove-btn"
										on:click={() => removeDecision(idx)}
										title="Remove"
									>
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<line
												x1="18"
												y1="6"
												x2="6"
												y2="18"
											/>
											<line
												x1="6"
												y1="6"
												x2="18"
												y2="18"
											/>
										</svg>
									</button>
								{:else}
									<span class="bullet-text">{decision}</span>
								{/if}
							</li>
						{/each}
					</ul>
				{:else if editable}
					<div class="empty-list">
						<p>No decisions yet</p>
						<button class="add-first-btn" on:click={addDecision}>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<line x1="12" y1="5" x2="12" y2="19" />
								<line x1="5" y1="12" x2="19" y2="12" />
							</svg>
							Add a decision
						</button>
					</div>
				{:else}
					<p class="empty-section">No decisions recorded</p>
				{/if}
			</section>

			<!-- Next Steps -->
			<section class="content-section">
				<div class="section-header-row">
					<h2 class="section-heading">
						{$t("workflow.meeting.protocol.nextSteps") ||
							"Next Steps"}
					</h2>
					<span class="ai-badge" title="AI-generated content">
						<svg
							viewBox="0 0 24 24"
							fill="none"
							stroke="currentColor"
							stroke-width="2"
						>
							<circle cx="12" cy="12" r="10" />
							<line x1="12" y1="16" x2="12" y2="12" />
							<line x1="12" y1="8" x2="12.01" y2="8" />
						</svg>
						AI
					</span>
					{#if editable}
						<button class="add-action-btn" on:click={addNextStep}>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<line x1="12" y1="5" x2="12" y2="19" />
								<line x1="5" y1="12" x2="19" y2="12" />
							</svg>
							Add
						</button>
					{/if}
				</div>
				{#if protocol.nextSteps && protocol.nextSteps.length > 0}
					<ul class="bullet-list">
						{#each protocol.nextSteps as nextStep, idx}
							<li class="bullet-item">
								{#if editable}
									<input
										type="text"
										class="next-step-input bullet-input"
										value={nextStep}
										on:blur={(e) =>
											handleNextStepBlur(e, idx)}
										on:keydown={(e) =>
											handleNextStepKeydown(e, idx)}
										placeholder="Next step..."
									/>
									<button
										class="remove-btn"
										on:click={() => removeNextStep(idx)}
										title="Remove"
									>
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<line
												x1="18"
												y1="6"
												x2="6"
												y2="18"
											/>
											<line
												x1="6"
												y1="6"
												x2="18"
												y2="18"
											/>
										</svg>
									</button>
								{:else}
									<span class="bullet-text">{nextStep}</span>
								{/if}
							</li>
						{/each}
					</ul>
				{:else if editable}
					<div class="empty-list">
						<p>No next steps yet</p>
						<button class="add-first-btn" on:click={addNextStep}>
							<svg
								viewBox="0 0 24 24"
								fill="none"
								stroke="currentColor"
								stroke-width="2"
							>
								<line x1="12" y1="5" x2="12" y2="19" />
								<line x1="5" y1="12" x2="19" y2="12" />
							</svg>
							Add a next step
						</button>
					</div>
				{:else}
					<p class="empty-section">No next steps defined</p>
				{/if}
			</section>

			<!-- Custom Sections (template-specific) -->
			{#if protocol.customSections && protocol.customSections.length > 0}
				{#each protocol.customSections as section, sectionIdx}
					<section
						class="content-section custom-section-{sectionIdx}"
					>
						<div class="section-header-row">
							<h2 class="section-heading">{section.label}</h2>
							<span class="ai-badge" title="AI-generated content">
								<svg
									viewBox="0 0 24 24"
									fill="none"
									stroke="currentColor"
									stroke-width="2"
								>
									<circle cx="12" cy="12" r="10" />
									<line x1="12" y1="16" x2="12" y2="12" />
									<line x1="12" y1="8" x2="12.01" y2="8" />
								</svg>
								AI
							</span>
							{#if editable && section.type === "list"}
								<button
									class="add-action-btn"
									on:click={() =>
										addCustomSectionListItem(sectionIdx)}
								>
									<svg
										viewBox="0 0 24 24"
										fill="none"
										stroke="currentColor"
										stroke-width="2"
									>
										<line x1="12" y1="5" x2="12" y2="19" />
										<line x1="5" y1="12" x2="19" y2="12" />
									</svg>
									Add
								</button>
							{/if}
						</div>

						{#if section.type === "text"}
							<!-- Text-type section -->
							{#if editable}
								<textarea
									class="summary-textarea custom-text-input"
									value={typeof section.content === "string"
										? section.content
										: ""}
									on:input={autoGrow}
									on:blur={(e) =>
										handleCustomSectionTextBlur(
											e,
											sectionIdx,
										)}
									placeholder="{section.label}..."
								></textarea>
							{:else}
								<p class="summary-text">
									{typeof section.content === "string"
										? section.content
										: "No content."}
								</p>
							{/if}
						{:else if section.type === "list"}
							<!-- List-type section -->
							{#if Array.isArray(section.content) && section.content.length > 0}
								<ul class="bullet-list">
									{#each section.content as item, itemIdx}
										<li class="bullet-item">
											{#if editable}
												<input
													type="text"
													class="custom-list-input bullet-input"
													value={item}
													on:blur={(e) =>
														handleCustomSectionListBlur(
															e,
															sectionIdx,
															itemIdx,
														)}
													on:keydown={(e) =>
														handleCustomSectionKeydown(
															e,
															sectionIdx,
															itemIdx,
														)}
													placeholder="Item..."
												/>
												<button
													class="remove-btn"
													on:click={() =>
														removeCustomSectionListItem(
															sectionIdx,
															itemIdx,
														)}
													title="Remove"
												>
													<svg
														viewBox="0 0 24 24"
														fill="none"
														stroke="currentColor"
														stroke-width="2"
													>
														<line
															x1="18"
															y1="6"
															x2="6"
															y2="18"
														/>
														<line
															x1="6"
															y1="6"
															x2="18"
															y2="18"
														/>
													</svg>
												</button>
											{:else}
												<span class="bullet-text"
													>{item}</span
												>
											{/if}
										</li>
									{/each}
								</ul>
							{:else if editable}
								<div class="empty-list">
									<p>No items yet</p>
									<button
										class="add-first-btn"
										on:click={() =>
											addCustomSectionListItem(
												sectionIdx,
											)}
									>
										<svg
											viewBox="0 0 24 24"
											fill="none"
											stroke="currentColor"
											stroke-width="2"
										>
											<line
												x1="12"
												y1="5"
												x2="12"
												y2="19"
											/>
											<line
												x1="5"
												y1="12"
												x2="19"
												y2="12"
											/>
										</svg>
										Add an item
									</button>
								</div>
							{:else}
								<p class="empty-section">No items recorded</p>
							{/if}
						{/if}
					</section>
				{/each}
			{/if}

			<!-- Full Transcript Section -->
			<section class="content-section">
				<div class="section-header-row">
					<h2 class="section-heading">Full Transcript</h2>
					<button
						class="toggle-edit-btn"
						on:click={() =>
							(isEditingTranscript = !isEditingTranscript)}
					>
						{isEditingTranscript ? "View Formatted" : "Edit Raw"}
					</button>
				</div>

				{#if isEditingTranscript && editable}
					<textarea
						class="transcript-edit-area"
						value={protocol.fullTranscript || ""}
						on:input={autoGrow}
						on:blur={handleTranscriptChange}
						placeholder="Raw transcript content..."
					></textarea>
				{:else}
					<div class="transcript-view">
						{#if protocol.transcriptSegments && protocol.transcriptSegments.length > 0}
							{#each protocol.transcriptSegments as segment}
								<div class="transcript-line">
									<span class="speaker-name"
										>{segment.speakerName}:</span
									>
									<span class="speaker-text"
										>{segment.text}</span
									>
								</div>
							{/each}
						{:else}
							<p class="summary-text whitespace-pre-wrap">
								{protocol.fullTranscript}
							</p>
						{/if}
					</div>
				{/if}
			</section>
		</div>
	{:else}
		<div class="empty-state">
			<div class="empty-icon">
				<svg
					viewBox="0 0 24 24"
					fill="none"
					stroke="currentColor"
					stroke-width="1"
				>
					<path
						d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5L14.5 2z"
					/>
					<polyline points="14 2 14 8 20 8" />
				</svg>
			</div>
			<h3>No protocol generated yet</h3>
			<p>
				Complete the previous steps to generate the draft meeting
				documentation.
			</p>
		</div>
	{/if}
</div>

<style>
	.preview-sidebar {
		height: 100%;
		display: flex;
		flex-direction: column;
		background: white;
		position: relative;
		overflow-y: auto;
	}

	.sidebar-content {
		padding: 40px;
		max-width: 900px;
		margin: 0 auto;
		width: 100%;
	}

	/* Empty State */
	.empty-state {
		flex: 1;
		display: flex;
		flex-direction: column;
		align-items: center;
		justify-content: center;
		padding: 40px;
		text-align: center;
		color: var(--slate-400, #94a3b8);
	}

	.empty-icon {
		width: 64px;
		height: 64px;
		margin-bottom: 20px;
		opacity: 0.5;
	}

	.empty-state h3 {
		color: var(--slate-700, #334155);
		font-size: 18px;
		font-weight: 600;
		margin-bottom: 8px;
	}

	.empty-state p {
		font-size: 15px;
		max-width: 300px;
	}

	/* Page Header */
	.page-header {
		margin-bottom: 32px;
	}

	.header-main {
		display: flex;
		align-items: flex-start;
		gap: 16px;
	}

	.icon-stack {
		width: 40px;
		height: 40px;
		display: flex;
		align-items: center;
		justify-content: center;
		background: var(--blue-50, #eff6ff);
		color: var(--blue-600, #2563eb);
		border-radius: 8px;
		flex-shrink: 0;
		margin-top: 4px;
	}

	.confluence-icon {
		width: 24px;
		height: 24px;
	}

	.title-area {
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: 4px;
	}

	.context-path {
		font-size: 13px;
		color: var(--slate-500, #64748b);
		font-weight: 500;
	}

	.page-title-input {
		width: 100%;
		font-size: 32px;
		font-weight: 700;
		color: var(--slate-900, #0f172a);
		border: 1px solid transparent;
		background: transparent;
		padding: 4px 0;
		margin: -4px 0;
		outline: none;
		border-radius: 4px;
		transition: all 0.2s;
	}

	.page-title-input:hover {
		background: var(--slate-50, #f8fafc);
	}

	.page-title-input:focus {
		background: white;
		border-color: var(--blue-200, #bfdbfe);
		box-shadow: 0 0 0 3px var(--blue-50, #eff6ff);
		padding-left: 8px;
	}

	.page-title {
		font-size: 32px;
		font-weight: 700;
		color: var(--slate-900, #0f172a);
		line-height: 1.2;
	}

	/* Metadata Grid */
	.metadata-grid {
		display: flex;
		flex-direction: column;
		gap: 0;
		border-top: 1px solid var(--slate-100, #f1f5f9);
		border-bottom: 1px solid var(--slate-100, #f1f5f9);
		margin-bottom: 40px;
	}

	.metadata-row {
		display: flex;
		align-items: flex-start;
		padding: 12px 0;
		min-height: 48px;
	}

	.metadata-label {
		width: 140px;
		font-size: 14px;
		font-weight: 600;
		color: var(--slate-500, #64748b);
		padding-top: 4px;
	}

	.metadata-value {
		flex: 1;
		font-size: 14px;
		color: var(--slate-700, #334155);
		padding-top: 4px;
	}

	.metadata-date-input {
		font-size: 14px;
		color: var(--slate-700, #334155);
		border: 1px solid transparent;
		background: transparent;
		padding: 4px 8px;
		margin: -4px -8px;
		border-radius: 4px;
		outline: none;
	}

	.metadata-date-input:hover {
		background: var(--slate-50, #f8fafc);
	}

	.metadata-date-input:focus {
		background: white;
		border-color: var(--blue-200, #bfdbfe);
	}

	.attendees-container {
		flex: 1;
		display: flex;
		flex-wrap: wrap;
		gap: 8px;
	}

	.attendee-chip {
		display: inline-flex;
		align-items: center;
		background: var(--slate-100, #f1f5f9);
		border-radius: 16px;
		padding: 2px 4px 2px 10px;
		gap: 4px;
	}

	.attendee-input {
		background: transparent;
		border: none;
		font-size: 13px;
		color: var(--slate-700, #334155);
		font-weight: 500;
		width: 100px;
		outline: none;
		padding: 2px 0;
	}

	.chip-remove {
		width: 20px;
		height: 20px;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 50%;
		border: none;
		background: transparent;
		color: var(--slate-400, #94a3b8);
		cursor: pointer;
	}

	.chip-remove:hover {
		background: var(--slate-200, #e2e8f0);
		color: var(--slate-600, #475569);
	}

	.chip-remove svg {
		width: 12px;
		height: 12px;
	}

	.add-chip {
		display: inline-flex;
		align-items: center;
		gap: 4px;
		background: transparent;
		border: 1px dashed var(--slate-300, #cbd5e1);
		border-radius: 16px;
		padding: 4px 12px;
		font-size: 13px;
		color: var(--slate-500, #64748b);
		cursor: pointer;
		transition: all 0.2s;
	}

	.add-chip:hover {
		background: var(--slate-50, #f8fafc);
		border-color: var(--slate-400, #94a3b8);
		color: var(--slate-700, #334155);
	}

	.add-chip svg {
		width: 14px;
		height: 14px;
	}

	.attendee-list {
		font-size: 14px;
		color: var(--slate-700, #334155);
		padding-top: 4px;
	}

	/* Content Sections */
	.content-section {
		margin-bottom: 48px;
	}

	.section-header-row {
		display: flex;
		align-items: center;
		gap: 12px;
		margin-bottom: 16px;
	}

	.section-heading {
		font-size: 20px;
		font-weight: 700;
		color: var(--slate-800, #1e293b);
	}

	.ai-badge {
		display: inline-flex;
		align-items: center;
		gap: 4px;
		padding: 2px 8px;
		background: var(--purple-50, #f5f3ff);
		color: var(--purple-600, #7c3aed);
		font-size: 11px;
		font-weight: 700;
		border-radius: 4px;
		text-transform: uppercase;
		letter-spacing: 0.05em;
	}

	.ai-badge svg {
		width: 12px;
		height: 12px;
	}

	.summary-textarea {
		width: 100%;
		min-height: 100px;
		font-size: 16px;
		line-height: 1.6;
		color: var(--slate-700, #334155);
		background: transparent;
		border: 1px solid transparent;
		border-radius: 8px;
		padding: 8px;
		margin-left: -8px;
		outline: none;
		resize: none;
		transition: all 0.2s;
	}

	.summary-textarea:hover {
		background: var(--slate-50, #f8fafc);
	}

	.summary-textarea:focus {
		background: white;
		border-color: var(--blue-200, #bfdbfe);
		box-shadow: 0 0 0 3px var(--blue-50, #eff6ff);
	}

	.summary-text {
		font-size: 16px;
		line-height: 1.6;
		color: var(--slate-700, #334155);
	}

	/* Task List */
	.task-list {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	.task-item {
		display: flex;
		align-items: flex-start;
		gap: 12px;
		padding: 12px;
		background: white;
		border: 1px solid var(--slate-100, #f1f5f9);
		border-radius: 12px;
		transition: all 0.2s;
		position: relative;
	}

	.task-item:hover {
		border-color: var(--slate-200, #e2e8f0);
		box-shadow: 0 2px 4px rgba(0, 0, 0, 0.02);
	}

	.task-checkbox {
		width: 20px;
		height: 20px;
		border-radius: 6px;
		border: 2px solid var(--slate-300, #cbd5e1);
		background: white;
		display: flex;
		align-items: center;
		justify-content: center;
		color: white;
		cursor: pointer;
		margin-top: 2px;
		flex-shrink: 0;
	}

	.task-item.completed .task-checkbox {
		background: var(--green-500, #22c55e);
		border-color: var(--green-500, #22c55e);
	}

	.task-content {
		flex: 1;
		display: flex;
		flex-direction: column;
		gap: 4px;
	}

	.action-text-input {
		width: 100%;
		font-size: 15px;
		color: var(--slate-800, #1e293b);
		font-weight: 500;
		border: none;
		background: transparent;
		outline: none;
		padding: 0;
	}

	.task-item.completed .action-text-input {
		text-decoration: line-through;
		color: var(--slate-400, #94a3b8);
	}

	.task-meta-edit {
		display: flex;
		gap: 16px;
		margin-top: 4px;
	}

	.meta-field {
		display: flex;
		align-items: center;
		gap: 6px;
		color: var(--slate-400, #94a3b8);
	}

	.meta-field svg {
		width: 14px;
		height: 14px;
	}

	.meta-input {
		font-size: 13px;
		color: var(--slate-500, #64748b);
		background: transparent;
		border: none;
		outline: none;
		padding: 0;
		width: 100px;
	}

	.task-text {
		font-size: 15px;
		color: var(--slate-800, #1e293b);
		font-weight: 500;
	}

	.strikethrough {
		text-decoration: line-through;
		color: var(--slate-400, #94a3b8);
	}

	.task-meta {
		display: flex;
		gap: 12px;
		margin-top: 4px;
	}

	.assignee-tag {
		font-size: 13px;
		color: var(--blue-600, #2563eb);
		font-weight: 600;
	}

	.due-date {
		display: flex;
		align-items: center;
		gap: 4px;
		font-size: 13px;
		color: var(--slate-500, #64748b);
	}

	.due-date svg {
		width: 14px;
		height: 14px;
	}

	.remove-btn {
		width: 28px;
		height: 28px;
		display: flex;
		align-items: center;
		justify-content: center;
		border-radius: 6px;
		border: none;
		background: transparent;
		color: var(--slate-300, #cbd5e1);
		cursor: pointer;
		opacity: 0;
		transition: all 0.2s;
	}

	.task-item:hover .remove-btn {
		opacity: 1;
	}

	.remove-btn:hover {
		background: var(--red-50, #fef2f2);
		color: var(--red-500, #ef4444);
	}

	.add-action-btn {
		display: inline-flex;
		align-items: center;
		gap: 6px;
		padding: 6px 12px;
		font-size: 14px;
		font-weight: 600;
		color: var(--blue-600, #2563eb);
		background: var(--blue-50, #eff6ff);
		border: none;
		border-radius: 6px;
		cursor: pointer;
		transition: all 0.2s;
	}

	.add-action-btn:hover {
		background: var(--blue-100, #dbeafe);
	}

	/* Bullet list */
	.bullet-list {
		list-style: none;
		padding: 0;
		margin: 0;
		display: flex;
		flex-direction: column;
		gap: 6px;
	}

	.bullet-item {
		display: flex;
		align-items: center;
		gap: 8px;
		padding: 6px 10px;
		background: white;
		border: 1px solid var(--slate-100, #f1f5f9);
		border-radius: 8px;
		transition: all 0.2s;
	}

	.bullet-item:hover {
		border-color: var(--slate-200, #e2e8f0);
	}

	.bullet-item::before {
		content: "";
		width: 5px;
		height: 5px;
		background: var(--slate-400, #94a3b8);
		border-radius: 50%;
		flex-shrink: 0;
	}

	.bullet-input {
		flex: 1;
		font-size: 15px;
		color: var(--slate-700, #334155);
		background: transparent;
		border: none;
		outline: none;
		padding: 2px 0;
	}

	.bullet-text {
		flex: 1;
		font-size: 15px;
		color: var(--slate-700, #334155);
	}

	/* Transcript area */
	.transcript-edit-area {
		width: 100%;
		min-height: 400px;
		max-height: 600px;
		overflow-y: auto;
		font-size: 14px;
		font-family:
			ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
		line-height: 1.6;
		color: var(--slate-700, #334155);
		background: var(--slate-50, #f8fafc);
		border: 1px solid var(--slate-200, #e2e8f0);
		border-radius: 12px;
		padding: 20px;
		outline: none;
		resize: none;
	}

	.transcript-view {
		display: flex;
		flex-direction: column;
		gap: 16px;
		padding: 24px;
		background: var(--slate-50, #f8fafc);
		border-radius: 12px;
		border: 1px solid var(--slate-100, #f1f5f9);
		max-height: 600px;
		overflow-y: auto;
	}

	.transcript-line {
		display: flex;
		flex-direction: column;
		gap: 4px;
	}

	.speaker-name {
		font-size: 13px;
		font-weight: 700;
		color: var(--slate-900, #0f172a);
		text-transform: uppercase;
		letter-spacing: 0.02em;
	}

	.speaker-text {
		font-size: 15px;
		line-height: 1.6;
		color: var(--slate-700, #334155);
	}

	.toggle-edit-btn {
		font-size: 13px;
		font-weight: 600;
		color: var(--slate-500, #64748b);
		background: transparent;
		border: 1px solid var(--slate-200, #e2e8f0);
		padding: 4px 12px;
		border-radius: 6px;
		cursor: pointer;
		transition: all 0.2s;
	}

	.toggle-edit-btn:hover {
		background: var(--slate-50, #f8fafc);
		color: var(--slate-800, #1e293b);
		border-color: var(--slate-300, #cbd5e1);
	}

	.whitespace-pre-wrap {
		white-space: pre-wrap;
	}
</style>
