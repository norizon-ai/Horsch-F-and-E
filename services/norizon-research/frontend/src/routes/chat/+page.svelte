<script lang="ts">
	import { onMount } from 'svelte';
	import { goto } from '$app/navigation';
	import { page } from '$app/stores';
	import { chatStore } from '$stores/chatStore';
	import { workflowStore } from '$stores/workflowStore';
	import type { ChatContext, ChatContextAction, ChatContextType } from '$lib/types';

	onMount(async () => {
		const contextType = $page.url.searchParams.get('context') as ChatContextType;
		const jobId = $page.url.searchParams.get('jobId');
		const action = $page.url.searchParams.get('action') as ChatContextAction;

		if (contextType === 'meeting-protocol' && jobId) {
			const workflowState = workflowStore.loadJob(jobId);

			if (workflowState?.protocol) {
				const context: ChatContext = {
					type: contextType,
					jobId,
					action: action || 'chat',
					protocol: workflowState.protocol,
					loadedAt: Date.now()
				};

				const sessionId = chatStore.createSessionWithContext(context);
				goto(`/chat/${sessionId}`, { replaceState: true });
				return;
			}
		}

		const sessionId = chatStore.createSession();
		goto(`/chat/${sessionId}`, { replaceState: true });
	});
</script>

<div class="flex items-center justify-center h-screen bg-slate-50">
	<div class="text-center">
		<div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto mb-4"></div>
		<p class="text-gray-600">Neue Sitzung wird erstellt...</p>
	</div>
</div>
