<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { chatStore } from '$stores/chatStore';
	import { workflowStore } from '$stores/workflowStore';
	import type { ChatContext, ChatContextAction, ChatContextType } from '$lib/types';

	onMount(async () => {
		// Parse context query parameters (from workflow completion)
		const contextType = $page.url.searchParams.get('context') as ChatContextType;
		const jobId = $page.url.searchParams.get('jobId');
		const action = $page.url.searchParams.get('action') as ChatContextAction;

		// If we have context params, load the workflow and create session with context
		if (contextType === 'meeting-protocol' && jobId) {
			// Load the protocol from the workflow store
			const workflowState = workflowStore.loadJob(jobId);

			if (workflowState?.protocol) {
				// Create context object with protocol data
				const context: ChatContext = {
					type: contextType,
					jobId,
					action: action || 'chat',
					protocol: workflowState.protocol,
					loadedAt: Date.now()
				};

				// Create session with context and redirect
				const sessionId = chatStore.createSessionWithContext(context);
				goto(`/chat/${sessionId}`, { replaceState: true });
				return;
			}
		}

		// Default: Create a new session without context
		const sessionId = chatStore.createSession();
		goto(`/chat/${sessionId}`, { replaceState: true });
	});
</script>

<div class="flex items-center justify-center h-screen bg-norizon-gray-50">
	<div class="text-center">
		<div class="animate-spin rounded-full h-12 w-12 border-b-2 border-norizon-blue mx-auto mb-4"></div>
		<p class="text-gray-600">Creating new research session...</p>
	</div>
</div>
