<script lang="ts">
	const { children } = $props();
	import { getUser } from '$lib/store.svelte';
	import { socket } from "$lib/socket";
    import { onMount } from 'svelte';

	onMount(async () => {
		const user = getUser();
		await user.get_me();
		socket.emit('join_party', { party_id: user.party_id });
	});
</script>

<div class="flex flex-col justify-between items-center h-full w-full">
	{@render children()}
</div>
